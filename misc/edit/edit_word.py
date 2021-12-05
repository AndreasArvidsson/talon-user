from talon import Context, Module, actions

key = actions.key
edit = actions.edit
user = actions.user

mod = Module()
ctx = Context()


@ctx.action_class("edit")
class EditActions:
    def word_left():
        key("ctrl-left")

    def word_right():
        key("ctrl-right")

    def select_word():
        key("ctrl-left ctrl-shift-right")

    def extend_word_left():
        key("ctrl-shift-left")

    def extend_word_right():
        key("ctrl-shift-right")

    def delete_word():
        edit.select_word()
        edit.delete()


@mod.action_class
class Actions:
    def select_word_right():
        """Select word to the right"""
        key("ctrl-right ctrl-shift-left")

    def cut_word():
        """Cut word under cursor"""
        edit.select_word()
        edit.cut()

    def copy_word():
        """Copy word under cursor"""
        edit.select_word()
        edit.copy()

    def delete_word_right():
        """Delete word to the right"""
        user.select_word_right()
        edit.delete()

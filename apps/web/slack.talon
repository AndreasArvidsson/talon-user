app: slack
-

edit last:               key(ctrl-up)
edit:                    key(e)

sidebar (show | hide):   key(ctrl-shift-d)
panel (show | hide):     key(ctrl-.)

all unreads:             key(ctrl-shift-a)
direct messages:         key(ctrl-shift-k)
go threads:
    key(ctrl-k)
    "Threads"
    sleep(300ms)
    key(enter)

jump to [<user.text>]:
    key(ctrl-k)
    sleep(100ms)
    "{text or ''}"

please [<user.text>]$:
    key(ctrl-k)
    sleep(100ms)
    edit.delete()
    sleep(100ms)
    "{text or ''}"

channel last:            key(alt-up)
channel next:            key(alt-down)
channel unread last:     key(alt-shift-up)
channel unread next:     key(alt-shift-down)
next unread:             key(alt-shift-down)

format code:             key(ctrl-shift-c)
format code block:       key(ctrl-alt-shift-c)
format quote:            key(ctrl-shift-9)
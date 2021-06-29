# Text: formatters + words, punctuation, numbers
<user.format_text>$:       user.insert_string(format_text)
<user.format_text> over:   user.insert_string(format_text)

# Only words, no symbols or numbers
words <user.words>$:       user.insert_string(words)
words <user.words> over:   user.insert_string(words)

# Single word
word <user.word>:          user.insert_string(word)
cap word <user.word>:      user.insert_formatted(word, "CAPITALIZE_FIRST_WORD")

# Select last
select last:               user.history_select_last_phrase()

# Show alternatives for selected
alt it:                    user.alternatives_selected(edit.selected_text())
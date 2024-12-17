from talon import Module

mod = Module()

mod.list("letter", "The spoken phonetic alphabet")
mod.list("digit", "All number/digit keys")
mod.list("key_function", "All function keys")
mod.list("key_arrow", "All arrow keys")
mod.list("key_special", "All special keys")
mod.list("key_modifier", "All modifier keys")

# Symbols available in command mode, but NOT during dictation.
mod.list("symbol", "All symbols from the keyboard")

# Symbols you want available BOTH in dictation and command mode.
mod.list("key_punctuation", "Symbols for inserting punctuation into text")

# Symbols you want available ONLY in code formatters.
mod.list(
    "key_punctuation_code",
    "Symbols for inserting punctuation into code formatters",
)


@mod.capture(rule="{user.key_modifier}+")
def key_modifiers(m) -> str:
    "One or more modifier keys"
    return "-".join(m)


@mod.capture(
    rule="{user.letter} | {user.digit} | {user.symbol} | {user.key_special} | {user.key_arrow} | {user.key_function}"
)
def key_unmodified(m) -> str:
    "A single key with no modifiers"
    if m[0] == " ":
        return "space"
    return m[0]


@mod.capture(rule="{user.key_modifier} | <user.key_unmodified>")
def key_any(m) -> str:
    "A single key"
    return m[0]


@mod.capture(rule="{user.letter} | {user.digit} | {user.symbol}")
def any_alphanumeric_key(m) -> str:
    "A single alphanumeric key"
    if m[0] == " ":
        return "space"
    return m[0]


@mod.capture(rule="{user.letter}+")
def letters(m) -> str:
    """One or more letters in the alphabet"""
    return "".join(m)

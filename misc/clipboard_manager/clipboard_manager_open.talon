mode: user.clipboard_manager
-

clippy:
    user.clipboard_manager_toggle()

clippy update:
    user.clipboard_manager_update()

clippy clear:
    user.clipboard_manager_remove()

clippy chuck <number_small> [and <number_small>]*:
    user.clipboard_manager_remove(number_small_list)

clippy split <number_small> [and <number_small>]*:
    user.clipboard_manager_split(number_small_list)

copy <number_small> [and <number_small>]*:
    user.clipboard_manager_copy(number_small_list)
paste <number_small> [and <number_small>]*:
    user.clipboard_manager_paste(number_small_list)
paste special <number_small> [and <number_small>]*:
    user.clipboard_manager_paste(number_small_list, 1)
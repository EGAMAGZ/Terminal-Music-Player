def local_player_help_popup(root):
    message="""Out of Focus Mode: p - Play previous song | n - Play next song | space - Pause and unpause song

    Queue Songs Menu:
    backspace - Remove song
    """
    root.show_message_popup("Help",message)

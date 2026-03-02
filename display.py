# display.py

def format_display(state, error):
    if error:
        return "Err"
    return str(state)
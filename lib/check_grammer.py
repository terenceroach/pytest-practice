def check_grammer(string):
    if type(string) is str:
        if string[0].isupper() and string[-1] in [".", "?", "!"]:
            return True
        else:
            return False
    else:
        raise Exception("You must provide a string")
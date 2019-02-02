import pyperclip
def p(amount, nights):
    result = amount * 19 / nights
    pyperclip.copy(result)
    return result

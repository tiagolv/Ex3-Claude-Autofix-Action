import re

def validar_password(password):
    if len(password) < 8:
        return False
    if not re.search(r'[A-Z]', password):
        return False
    if not re.search(r'[az]', password):
        return False
    if not re.search(r'[^A-Za-z0-9]', password):
        return False
    return True
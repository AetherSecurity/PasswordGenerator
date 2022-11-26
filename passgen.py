import random
import string
import pyperclip

def generate(Number: int, Symbols: str):
    return ''.join(random.SystemRandom().choice(string.ascii_letters + string.digits + Symbols) for _ in range(Number))

def copy(Variable: vars):
    pyperclip.copy(Variable)
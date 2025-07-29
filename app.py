# app.py program - updated program ( new 2025 )
def add(a, b):
    return a + b


def insecure_example():
    eval("print('This is insecure')")  # Semgrep will flag this
    eval("print('bad')")  # should trigger Semgrep


# added
import subprocess

def add(a, b):
    return a + b

def insecure():
    subprocess.call(f"ls {input('Enter something here: ')}", shell=True)

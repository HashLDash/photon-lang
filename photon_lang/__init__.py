import builtins
import ctypes
import os

pythonImport = builtins.__import__

def photonImport(name, py_globals={}, py_locals={}, fromlist=[], level=0):
    if f'{name}.so' in os.listdir():
        module = f'{os.getcwd()}/{name}.so'
        return ctypes.CDLL(module)
    return pythonImport(name, py_globals, py_locals, fromlist, level) 

builtins.__import__ = photonImport

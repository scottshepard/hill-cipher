import numpy as np
from scipy import linalg as LA
from sys import float_info

def message_formatter(message):
    if len(message) % 2 != 0:
        message = message + ' '
    return [message[i:i+2] for i in range(0, len(message), 2)]

def key_formatter(key_input):
    key = [int(i) for i in key_input.split(',')]
    return np.array([key[i:i+2] for i in range(0, len(key), 2)])

def is_invertible(key):
    return np.linalg.cond(key) < 1/float_info.epsilon

def simple_encrypt(message, key):
    message = [ord(c) for c in list(message)]
    convert = ""
    testd = key.dot(message)

    for i in range(0, len(testd)):
        convert = convert + chr(testd[i])
    return convert
    
def simple_decrypt(message, key):
    testd = [ord(c) for c in list(message)]
    keyinv = LA.inv(key)
    converted = keyinv.dot(testd)
    output = ''
    for i in range(0, len(converted)):
        z = int(round(converted[i]))
        output = output + chr(z)
    return output

def encryptor(message, key_matrix):
    return ''.join([simple_encrypt(chunk, key_matrix) for chunk in message_formatter(message)])
    
def decryptor(message, key_matrix):
    return ''.join([simple_decrypt(chunk, key_matrix) for chunk in message_formatter(message)])
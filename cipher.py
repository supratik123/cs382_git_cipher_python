#!/usr/bin/python3

def encrypt(text, key):
    return text * key

def decrypt(text, key):
    return text[:key]
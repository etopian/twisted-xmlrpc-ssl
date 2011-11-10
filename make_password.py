#!/usr/bin/env python

if __name__ == '__main__':
    from crypt import crypt
    password = 'ohmygod'
    salt = password[-2:]
    print crypt(password, salt)

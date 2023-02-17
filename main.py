#!/bin/python3

alphabet = 'abcdefghijklmnopqrstuvwxyz'
newMessage = ''
ed = int(input('Type 0 to encrypt or 1 to decrypt: '))
if ed == 0:
  message = input('Please enter a message: ')
  key = int(input('Please type a key from 0 to 26: '))
  for character in message:
    if character in alphabet:
      position = alphabet.find(character)
      newPosition = (position + key) % 26
      newCharacter = alphabet[newPosition]
      newMessage += newCharacter
    else:
      newMessage += character
  print('The encrypted message is', newMessage, 'with the key of', key, '.')
elif ed == 1:
    message = input('Please enter the message: ')
    key = int(input('Please type the key: '))
    for character in message:
      if character in alphabet:
        position = alphabet.find(character)
        newPosition = (position - key) % 26
        newCharacter = alphabet[newPosition]
        newMessage += newCharacter
      else:
        newMessage += character
    print('The decrypted message is', newMessage, '.')
else:
  print('You can only type 0 or 1. Nice try, though.')

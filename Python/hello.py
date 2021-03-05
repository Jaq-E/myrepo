print('hello world')

#test code from the edX course

alphabet = 'abcdefghijklmnopqrstuvwxyz'

newMessage = ''

message = input('Please enter a message: ')

key = input('Enter a key (1-26): ')

key = int(key)

for character in message:
    if character in alphabet:  
        position = alphabet.find(character) 
        newPosition = (position + key) % 26
        newCharacter = alphabet[newPosition] 
        newMessage += newCharacter
else: 
        newMessage += character

print('Your new message is: ', newMessage)


# example from ch2 part2 - py4e

inp = input('european floor?')
usf = int(inp) + 1
print('US floor', usf)












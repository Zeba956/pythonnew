dictionary = {
"cat":"chat",
"dog":"chien",
"horse":"cheval"        
}

phone_numbers={'boss':5551234567, 'Suzy':5559876543}
empty_dictionary={}

print(dictionary)
print(type(dictionary))
print(phone_numbers)
print(type(phone_numbers))
print(empty_dictionary)
print(type(empty_dictionary))


print(dictionary["cat"])
print(phone_numbers['boss'])

#print(phone_numbers['president'])#this will give error because president is not a key in the dictionary phone_numbers.KeyError: 'president'


words=['cat','lion','horse']
for word in words:
    if word in dictionary:
        print(word, "->", dictionary[word])
    else:
        print(word,"is not in dictionary")

print(dictionary.keys())

for key in dictionary.keys():
    print(key,"->", dictionary[key])
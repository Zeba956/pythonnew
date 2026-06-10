string = "Hello, How are you doing today"
count_vowel= 0
for ch in string:
    if ch in 'aeiouAEIOU':
        count_vowel += 1
print(count_vowel)
print(string.split()[3])
print(string[::-1])
non_palin,palin = 'abcdef','axttxa'
print(non_palin == non_palin[::-1])
print(palin == palin[::-1])
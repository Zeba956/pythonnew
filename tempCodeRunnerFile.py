pol_eng_dictionary={"kwist":"flower"}
pol_eng_dictionary.update(
    {
        "gleba":"soil"
    })
print(pol_eng_dictionary)

pol_eng_dictionary.popitem()#this will remove the last key value pair from the dictionary pol_eng_dictionary and return it as a tuple.
print(pol_eng_dictionary)
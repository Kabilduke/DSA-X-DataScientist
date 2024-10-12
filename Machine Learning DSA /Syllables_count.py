# NLP
def syllable_count(text):
    word = text.lower()
    count = 0
    vowels = "aeiouy"
    
    if word[0] in vowels:
        count += 1
    for index in range(1, len(word)):
        if word[index] in vowels and word[index - 1] not in vowels:
            count += 1
    if word.endswith('e'):
        count -= 1
    if count == 0:
        count += 1
    return count

word = " enable"
result = syllable_count(word)
print(result)


#Output: 2

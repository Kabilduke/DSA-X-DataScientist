from collections import Counter


def bag_of_words(s):
  text = s.lower()
  result = []
  
  for char in text:
    if char.isalpha() or char.isspace():
      result.append(char)
      
  words = ''.join(result).split()
  Bag = Counter(words)
  
  return Bag


s = 'Natural Language Processing is easy and fun to learn. Natural Language Processing help to understand the meaning of text.'
Bag_words = bag_of_words(s)
print("Bag of Words:", Bag_words)

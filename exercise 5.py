#exercise5
def reverse(words):
  
  words = words.split()
  rev_words = []
  for i in words:
    rev_words.append(i[::-1])
  sentence = " ".join(rev_words)
  print(sentence)
  
reverse("Hello World")

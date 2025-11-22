def RLE(text):
  compression = []
  for i in range(0,len(text)-1):
    #compression.append()
    #print(i)
    count = 1
    
    #print(text[i])
    while len(text) != 0: 
      if text[i] ==  text[i+1]:
        count += 1
        compression.append(count)
        text.remove(text[i+1])
      else:
        compression.append(text[i])
        compression.append(count)
        text.remove(text[i])
  print(compression)

    
    #compression.append()

text_input = input("Please enter some text: ")
text = []
for letter in text_input:
  text.append(letter)
print(RLE(text))

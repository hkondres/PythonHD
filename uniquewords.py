text_file = open('data.txt', 'r') # change data.txt for your text file or name your file, of course, data.txt... 
text = text_file.read()

#cleaning
text = text.lower()
words = text.split()
words = [word.strip('.,!;()[]') for word in words]
words = [word.replace("'s", '') for word in words]

#finding unique
unique = []
for word in words:
    if word not in unique:
        unique.append(word)

#sort
unique.sort()

#print
print(unique)

"""Word Finder: finds random words from a dictionary."""

import random
# opening the file in read mode
with open('words.txt', 'r') as file:
    text = file.read()
    words = list(map(str, text.split()))
    # printing out the random string
    print(random.choice(words))




# class WordFinder:
    # def open_file(self,file):
    #     self.file = open('words.txt','r')
    #     print(self.file.read())


# file = open('words.txt', 'r')
# for word in file:
#     print((word))
    



# f = file.readline()
# print(random.choice(f))



    # def __init__(self, file): 
    #     self.file = open(file)
    #     print(self.file.read())





# import random

# class WordFinder:

    

"""
Write a Python program to find the list of words 
that are longer than n from a given list of words.
"""

def lenth_word(n,str):
    wordlenght = []
    text = str.split()
    for x in text:
        if len(x)<=n:
            wordlenght.append(x)
    return wordlenght
n = int(input("Enter the size:"))
str = raw_input("Enter the sentence:")
print(lenth_word(n,str))
from cs50 import get_string

# takes input

text = get_string("text: ")

# intialising

lettercount = 0
wordcount = 1
sentcount = 0

# hecking for letters words and sentences

for i in text:
    if i.isalpha():
        lettercount += 1

    elif i.isspace():
        wordcount += 1

    elif (i == "." or i == "!" or i == "?"):
        sentcount += 1

L = lettercount/wordcount*100
S = sentcount/wordcount*100

# using formula

index = round(0.0588 * L - 0.296 * S - 15.8)

# cases possible

if index >= 16:
    print("Grade 16+")

elif index < 1:
    print("Before Grade 1")

else:
    print(f"Grade {index}")

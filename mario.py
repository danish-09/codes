# importing get_int from cs50

from cs50 import get_int

while True:
    # will prompt until correct height is provided

    value = get_int("height: ")

    if (1 <= value <= 8):
        break
# for row

for i in range(0, value, 1):

    # printing spaces inside row

    for j in range(0, value-i-1, 1):
        print(" ", end="")

    # printing hashes inside row

    for k in range(0, i+1, 1):
        print("#", end="")

    # for new line after one row is complete

    print()


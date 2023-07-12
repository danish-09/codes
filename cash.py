# importing function from cs50

from cs50 import get_float

while True:

    # prompt again if provided value is negative

    value = get_float("money owned: ")

    if (value >= 0):
        break
count = 0

# multiplying the input value by 100 to covert dollars into cents

actvalue = value*100

# use cases

while (actvalue >= 25):
    actvalue = actvalue - 25
    count += 1

while (actvalue >= 10):
    actvalue = actvalue - 10
    count += 1

while (actvalue >= 5):
    actvalue = actvalue - 5
    count += 1

while (actvalue >= 1):
    actvalue = actvalue - 1
    count += 1

# output the number of coins

print(+count)

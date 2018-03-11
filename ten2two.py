binary = str(input("Binary: "))
decimal = 0

multiplicator = 1
place = 1

while (place < (len(binary)+1)):
    decimal += int(binary[len(binary)-place])*multiplicator
    place += 1
    multiplicator = multiplicator * 2
print (decimal)
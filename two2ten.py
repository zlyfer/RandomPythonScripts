decimal = int(input("Decimal: "))
binary = ""
while decimal != 0:
    rest = decimal % 2
    binary = str(rest) + binary
    decimal = decimal // 2
print ("Binary:  %s" % binary)
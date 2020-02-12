def roundSolver(A, B, C, D, message, key, numShift):
    # bitwise or A and B
    BandC = binAndOpe(B, C)
    comB = complement(B)
    comBandD = binAndOpe(comB, D)
    F = binOrOpe(BandC, comBandD)
    temp = binAddOpe(A, F)
    temp = binAddOpe(temp, message)
    temp = binAddOpe(temp, key)
    temp = shiftLeft(temp, numShift)
    temp = binAddOpe(temp, B)

    return D, temp, B, C


def shiftLeft(a, numShift):
    return a[numShift:] + a[:numShift]


def complement(A):
    aComp = ""
    for a in A:
        aComp = (aComp + "1") if a == "0" else (aComp + "0")
    return aComp


def binAndOpe(A, B):
    AandB = ""
    for a, b in zip(A, B):
        AandB = (AandB + "1") if a == "1" and b == "1" else (AandB + "0")
    return AandB


def binOrOpe(A, B):
    temp = ""
    for a, b in zip(A, B):
        temp = temp + "1" if (a == "1" or b == "1") else temp + "0"
    return temp


def binAddOpe(A, B):
    result = ""
    remainder = False
    for a, b in zip(A[::-1], B[::-1]):
        if a == "1" and b == "1" and remainder:
            result += "1"
            remainder = True
        elif a == "1" and b == "1" and not remainder:
            result += "0"
            remainder = True
        elif (a == "1" or b == "1") and remainder:
            result += "0"
            remainder = True
        elif (a == "1" or b == "1") and not remainder:
            result += "1"
            remainder = False
        elif remainder:
            result += "1"
            remainder = False
        else:
            result += "0"
            remainder = False
    return result[::-1]


"""  A = input("Enter value for A:")
    B = input("Enter value for B:")
    C = input("Enter value for C:")
    D = input("Enter value for D:")
    message z= input("Enter message:")
    key = input("Enter key:") 
 """


def main():
    A = "10101011011100011101011010011011"
    B = "01010100010010100000110101010011"
    C = "10101010110010100101001101010010"
    D = "10101011011100011101011010011011"
    message = "10000000101010101010101010100101"
    key = "10001011010001001111011110101111"
    numShift = 12
    A, B, C, D = roundSolver(A, B, C, D, message, key, numShift)
    print(f"A = {A}\nB = {B}\nC = {C}\nD = {D}")


main()

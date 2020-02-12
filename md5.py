def roundSolver(A, B, C, D, message, key):
    # bitwise or A and B
    BandC = binAndOpe(A, B)
    comB = complement(B)
    comBandD = binAndOpe(comB, D)
    F = binOrOpe(BandC, comBandD)


def complement(A):
    aComp = ""
    for a in A:
        aComp = (aComp + "1") if a == "0" else (aComp + "0")
    return aComp


def binAndOpe(A, B):
    BandC = ""
    for b, c in zip(B, B):
        BandC = (BandC + "1") if b == "1" and c == "1" else (BandC + "0")
    return BandC


def binOrOpe(A, B):
    temp = ""
    for a, b in zip(A, B):
        temp = temp + "1" if (a == "1" or b == "1") else temp + "0"
    return temp


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
    roundSolver(A, B, C, D, message, key)


main()

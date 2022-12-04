
from math import expm1


mem = list(range(1, 1000))


PC = 0
MQ = 0
AC = 0


def fetch_dec(x):

    global PC
    global IBR
    global IR
    global MQ
    global MBR
    global MAR
    global AC

    MBR = x

    MAR = PC
    IR = MBR[0:8]
    MAR = MBR[8:20]
    IBR = MBR[20:40]

    for i in range(0, 2):

        # STOR M(X)
        if(IR == '00100001'):
            MBR = AC
            mem[(int(MAR, 2))] = MBR
            if(i == 0):
                MAR = IBR[8:20]
                IR = IBR[0:8]
                PC += 1
                continue

        # LOAD M(X)
        if(IR == '00000001'):
            MBR = mem[(int(MAR, 2))]
            AC = MBR
            if(i == 0):
                MAR = IBR[8:20]
                IR = IBR[0:8]
                PC += 1
                continue

        # SUB M(X)
        if(IR == '00000110'):
            MBR = mem[(int(MAR, 2))]
            AC = AC - MBR
            if(i == 0):
                MAR = IBR[8:20]
                IR = IBR[0:8]
                PC += 1
                continue

        # ADD M(X)
        if(IR == '00000101'):
            MBR = mem[(int(MAR, 2))]
            AC = AC + MBR
            if(AC > 2**40):
                print("OVERFLOW")
                quit()
            if(i == 0):
                MAR = IBR[8:20]
                IR = IBR[0:8]
                PC += 1
                continue

        # LOAD MQ
        if(IR == '00001010'):
            AC = MQ
            if(i == 0):
                MAR = IBR[8:20]
                IR = IBR[0:8]
                PC += 1
                continue

        # DIV M(X)
        if(IR == '00001100'):
            MBR = mem[int(MAR, 2)]
            MQ = AC//MBR
            AC = AC % MBR
            if(i == 0):
                MAR = IBR[8:20]
                IR = IBR[0:8]
                PC += 1
                continue

        # LOAD MQ,M(X)
        if(IR == '00001001'):
            MBR = mem[int(MAR, 2)]
            MQ = MBR
            if(i == 0):
                MAR = IBR[8:20]
                IR = IBR[0:8]
                PC += 1
                continue

        # HALT
        if(IR == '00000000'):
            if(i == 0):
                PC = PC+1
            return
    return


x = int(input("Choose one. \n 1. Addition  \n 2. Subtraction \n 3. Average of 10 numbers \n"))


if(x == 1):

    a = int(input("Enter 1st number \n"))
    b = int(input("Enter 2nd number \n"))
    c = int(input("Enter 3rd number \n"))
    d = int(input("Enter 4th number \n"))
    e = int(input("Enter 5th number \n"))
    f = int(input("Enter 6th number \n"))
    g = int(input("Enter 7th number \n"))
    h = int(input("Enter 8th number \n"))
    i = int(input("Enter 9th number \n"))
    j = int(input("Enter 10th number \n"))
    k = int(input("Enter 11th number \n"))
    l = int(input("Enter 12th number \n"))
    m = int(input("Enter 13th number \n"))
    n = int(input("Enter 14th number \n"))
    o = int(input("Enter 15th number \n"))

    mem[20] = a
    mem[21] = b
    mem[22] = c
    mem[23] = d
    mem[24] = e
    mem[25] = f
    mem[26] = g
    mem[27] = h
    mem[28] = i
    mem[29] = j
    mem[30] = k
    mem[31] = l
    mem[32] = m
    mem[33] = n
    mem[34] = o

    # LHS = LOAD M(20) AND RHS = ADD M(21)
    mem[0] = '0000000100000001010000000101000000010101'
    # LHS = ADD M(22) AND RHS = ADD M(23)
    mem[1] = '0000010100000001011000000101000000010111'
    # LHS = ADD M(24) AND RHS = ADD M(25)
    mem[2] = '0000010100000001100000000101000000011001'
    # LHS = ADD M(26) AND RHS = ADD M(27)
    mem[3] = '0000010100000001101000000101000000011011'
    # LHS = ADD M(28) AND RHS = ADD M(29)
    mem[4] = '0000010100000001110000000101000000011101'
    # LHS = ADD M(30) AND RHS = ADD M(31)
    mem[5] = '0000010100000001111000000101000000011111'
    # LHS = ADD M(32) AND RHS = ADD M(33)
    mem[6] = '0000010100000010000000000101000000100001'
    # LHS = ADD M(34) AND RHS = STOR M(35)
    mem[7] = '0000010100000010001000100001000000100011'

    fetch_dec(mem[0])
    fetch_dec(mem[1])
    fetch_dec(mem[2])
    fetch_dec(mem[3])
    fetch_dec(mem[4])
    fetch_dec(mem[5])
    fetch_dec(mem[6])
    fetch_dec(mem[7])

    print(mem[35])

if(x == 2):
    a = int(input("Enter 1st number \n"))
    b = int(input("Enter 2nd number \n"))
    c = int(input("Enter 3rd number \n"))
    d = int(input("Enter 4th number \n"))
    e = int(input("Enter 5th number \n"))
    f = int(input("Enter 6th number \n"))
    g = int(input("Enter 7th number \n"))
    h = int(input("Enter 8th number \n"))
    i = int(input("Enter 9th number \n"))
    j = int(input("Enter 10th number \n"))
    k = int(input("Enter 11th number \n"))
    l = int(input("Enter 12th number \n"))
    m = int(input("Enter 13th number \n"))
    n = int(input("Enter 14th number \n"))
    o = int(input("Enter 15th number \n"))

    mem[20] = a
    mem[21] = b
    mem[22] = c
    mem[23] = d
    mem[24] = e
    mem[25] = f
    mem[26] = g
    mem[27] = h
    mem[28] = i
    mem[29] = j
    mem[30] = k
    mem[31] = l
    mem[32] = m
    mem[33] = n
    mem[34] = o

    # LHS = LOAD M(20) AND RHS = SUB M(21)
    mem[0] = '0000000100000001010000000110000000010101'
    # LHS = SUB M(22) AND RHS = SUB M(23)
    mem[1] = '0000011000000001011000000110000000010111'
    # LHS = SUB M(24) AND RHS = SUB M(25)
    mem[2] = '0000011000000001100000000110000000011001'
    # LHS = SUB M(26) AND RHS = SUB M(27)
    mem[3] = '0000011000000001101000000110000000011011'
    # LHS = SUB M(28) AND RHS = SUB M(29)
    mem[4] = '0000011000000001110000000110000000011101'
    # LHS = SUB M(30) AND RHS = SUB M(31)
    mem[5] = '0000011000000001111000000110000000011111'
    # LHS = SUB M(32) AND RHS = SUB M(33)
    mem[6] = '0000011000000010000000000110000000100001'
    # LHS = SUB M(34) AND RHS = STOR M(35)
    mem[7] = '0000011000000010001000100001000000100011'

    fetch_dec(mem[0])
    fetch_dec(mem[1])
    fetch_dec(mem[2])
    fetch_dec(mem[3])
    fetch_dec(mem[4])
    fetch_dec(mem[5])
    fetch_dec(mem[6])
    fetch_dec(mem[7])

    print(mem[35])

if(x == 3):
    a = int(input("Enter 1st number \n"))
    b = int(input("Enter 2nd number \n"))
    c = int(input("Enter 3rd number \n"))
    d = int(input("Enter 4th number \n"))
    e = int(input("Enter 5th number \n"))
    f = int(input("Enter 6th number \n"))
    g = int(input("Enter 7th number \n"))
    h = int(input("Enter 8th number \n"))
    i = int(input("Enter 9th number \n"))
    j = int(input("Enter 10th number \n"))

    mem[20] = a
    mem[21] = b
    mem[22] = c
    mem[23] = d
    mem[24] = e
    mem[25] = f
    mem[26] = g
    mem[27] = h
    mem[28] = i
    mem[29] = j
    mem[30] = 10

    # LHS = LOAD M(20) AND RHS = ADD M(21)
    mem[0] = '0000000100000001010000000101000000010101'
    # LHS = ADD M(22) AND RHS = ADD M(23)
    mem[1] = '0000010100000001011000000101000000010111'
    # LHS = ADD M(24) AND RHS = ADD M(25)
    mem[2] = '0000010100000001100000000101000000011001'
    # LHS = ADD M(26) AND RHS = ADD M(27)
    mem[3] = '0000010100000001101000000101000000011011'
    # LHS = ADD M(28) AND RHS = ADD M(29)
    mem[4] = '0000010100000001110000000101000000011101'
    # LHS = DIV M(30) AND RHS = LOAD MQ
    mem[5] = '0000110000000001111000001010000000000000'
    # LHS = STOR M(31) AND RHS = HALT
    mem[6] = '0010000100000001111100000000000000000000'

    fetch_dec(mem[0])
    fetch_dec(mem[1])
    fetch_dec(mem[2])
    fetch_dec(mem[3])
    fetch_dec(mem[4])
    fetch_dec(mem[5])
    fetch_dec(mem[6])

    print(mem[31])
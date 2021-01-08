def binary_to_decimal(binary):
        dec=0
        reverselist=binary[::-1]
        for idx,bit in enumerate(reverselist):
            dec+=int(bit)*2**idx
        return dec

def decimal_tobin(decimal):
    if decimal==0:
        return 0
    binary=""
    while (decimal > 0):
        binary+= str(decimal%2)
        decimal = int(decimal//2)
    return binary[::-1]


def countOne(decimal):
    count=0
    if decimal==0:
        return 0
    binary=""
    while (decimal > 0):
        binary=decimal%2
        if binary==1:
            count+=1
        decimal = decimal//2
    return count

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        integer_a,integer_b =0,0

        #bin to decimal
        integer_a =binary_to_decimal(a)
        integer_b =binary_to_decimal(b)
        print(2, decimal_tobin(2))
        print(3, decimal_tobin(3))
        print(countOne(9))
        print(9, decimal_tobin(9))
        summ=integer_a+integer_b
        #print(decimal_tobin(summ))
        return bin(summ)[2:]

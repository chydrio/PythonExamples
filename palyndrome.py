def isPalyndrome():
    result=True
    inputString = input('Enter a string:')

    for i in range(len(inputString)//2):
        if inputString[i]!=inputString[len(inputString)-i-1]:
            result=False

    if result==True:
        print("it's a palyndrom")
    else:
        print("it's not a palyndrom")
def main():
    isPalyndrome()

if __name__ == '__main__':
    main()




def isPalyndrome(s):
        for i in range(len(s)//2):
            if s[i]!=s[len(s)-i-1]:
                return False
        return True
        
def isPalyndrome(s):
        return s == s[::-1]

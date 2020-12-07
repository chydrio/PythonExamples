import random

def estimatePi():
    n = int(input('Enter a number:'))

    insideCircle=0
    outsideCircle=0
    pi=0

    for i in range(n):
        x=random.uniform(0,1)
        y=random.uniform(0,1)
        if x**2+y**2>1:
            outsideCircle=outsideCircle+1
        else:
            insideCircle=insideCircle+1

    print('inside: ', insideCircle)
    print('outside: ', outsideCircle)
    pi= (insideCircle/(insideCircle+outsideCircle))*4
    print('pi: ', pi)


def main():
    estimatePi()


if __name__ == '__main__':
    main()

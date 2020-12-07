# Enter your code here. Read input from STDIN. Print output to STDOUT

exo1:
find-the-first-repeated-character-in-a-string/
A=abcdert
B=zoooa
->first common letter a


exo2:
8/12


def change_dir(x,y):
    new_dir=""

    y_split=y.split("/")
    x_split=x.split("/")
    count_direct=0
    if x=="/":
        new_dir="/"+y
    elif y=="..":
        x=x.split("/")[:-1]
        new_dir=("/").join(x)
    else:
        new_y=""
        for path in y_split:
            if path=="..":
                count_direct+=1
            else:
                new_y+="/"+path
        if count_direct>0:
            #print(count_direct)
            x=x.split("/")[:-count_direct]
            if new_y=="":
                new_dir=("/").join(x)
            else:
                new_dir=("/").join(x)+new_y
            if len(new_dir)==0:
                new_dir="/"
        else:
            new_dir=x+ "/" +y
    print(new_dir)

if __name__ == '__main__':
    x = input()
    y= input()
    change_dir(x,y)

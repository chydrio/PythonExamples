
"""// returns smallest integer value greater than 0 which is not present in "vals"
// ex 1: [1, 2, 3] -> 4
// ex 2: [1, 3, 5] -> 2
int SmallestIntNotIn(const vector<int> & vals)
{

}
"""

def findSmaller(array):
    result=1
    print(array)
    array.sort()
    previous=0
    for i in range(len(array)):
        #print(array[i],previous)
        if array[i]==previous:
            #print("previous==array[i]")
            continue
        if array[i]<0:
            continue
        if result!=array[i]:
            return result

        result+=1
        previous=array[i]
    return result

#array=[1,3,5]
#findSmaller(array)

def main():
    #array=[1,3,5]
    array=[1,2,3]
    array=[]
    print(findSmaller(array))
    array=[1,1,3]
    print(findSmaller(array))
    array=[-11, -2,3,5]
    print(findSmaller(array))

main()


#Hello

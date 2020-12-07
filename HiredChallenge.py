
def solution(maze, n):
    print(maze)
    if maze[0][0]==1 or maze[n-1][n-1]==1:
        print('BLOCKED')
        return False
    for col in range(n):
        for line in range(n):
            #going right"
            if maze[col][line]==1:
                print('hit wall, going down', col, line)
                if line+1 < n and maze[col-1][line+1]==1:
                    print('hit wall while going down', col, line)
                    return False
                else:
                    col= col-1
            else:
                print('clear path')
                if col== n-1 and line==n-1:
                    return True
    return False







from collections import Counter
def solution(numbers):
    result_array=[]
    length=len(numbers)
    if length==0:
        return result_array
    if length==1:
        result_array.append(numbers[0])

        return result_array
    myCount=Counter(numbers)
    print(myCount.most_common())
    occ=0
    occ=myCount.most_common()[-1][1]
    for i in range(len(myCount.most_common())):
        if myCount.most_common()[i][1]==occ:
            result_array.append(myCount.most_common()[i][0])
    return sorted(result_array)

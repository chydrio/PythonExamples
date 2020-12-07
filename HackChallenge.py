for i in range(length):
        if i+1<length:
            for j in range(i+1,length):
                print(i,j)
                print(arr[i])
                print(arr[j])
                bitwise=arr[i]&arr[j]
                print('i&j',bitwise, i, j)
                if powerOfTwo.count(bitwise)>0:
                    print('found')
                    result=result+1


    a= a.sort(reverse=True)
    print(a)
    for i in range(1,len(a)):
        sum_int=0
        for j in range(1,i):
            print(i,j)
            sum_int= sum_int+j*a[j-1]
        print(sum_int)


#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'stringAnagram' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. STRING_ARRAY dictionary
#  2. STRING_ARRAY query
#

def stringAnagram(dictionary, query):
    result=[]
    number_oftimes_word=0
    letter_in_word=True
    if 1>len(dictionary)>10**15 or 1>len(query)>10**15:
        return result
    for word in query:
        for word_dico in dictionary:
            if len(word)!=len(word_dico):
                print(word,' len(word)!=len(word_dico) ',word_dico)
                letter_in_word=False
                continue
            for letter in word:
                letter_in_word=True
                if letter not in word_dico or not letter.isalpha() or len(word)!=len(word_dico):
                    print(letter,' not in ',word_dico)
                    letter_in_word=False
                    break
            if letter_in_word and len(word)==len(word_dico):
                print(word,'is in ',word_dico)
                number_oftimes_word=number_oftimes_word+1
                letter_in_word=True
        result.append(number_oftimes_word)
        number_oftimes_word=0
    print(result)
    return result



Basic
def stringAnagram(dictionary, query):
    result=[]
    for query_word in query:
        count=0
        for dict_word in dictionary:
            if len(query_word)!=len(dict_word):
                continue
            elif "".join(sorted(dict_word))=="".join(sorted(query_word)):
                count+=1
        result.append(count)
    return result

    -->n**2

    better solutions with Counter (3N)so N as we drop the constant

    for i in range(len(dictionary)):
        dictionary[i]=="".join(sorted(dictionary[i]))
    for i in range(len(query)):
        query[i]=="".join(sorted(query[i]))
    cnt=Counter(dictionary)
    for i in range(len(query)):
        result.append(cnt[query[i]])


Intermediate

# Complete the 'maxPairs' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY skillLevel
#  2. INTEGER minDiff
#

def maxPairs(skillLevel, minDiff):
    skillLevel.sort()
    print(skillLevel)
    print("min",minDiff )
    pair=0
    diff=0
    for i in range(len(skillLevel)):
        for j in range(i+1,len(skillLevel)):
                if skillLevel[i]!='X' and skillLevel[j]!='X':
                    diff= skillLevel[i]-skillLevel[j]
                    if diff<0:
                        diff=-diff
                    if diff>=minDiff:
                        pair+=1
                        skillLevel[i]='X'
                        skillLevel[j]='X'
                        break
    return pair
10/15 passed

if __name__ == '__main__':

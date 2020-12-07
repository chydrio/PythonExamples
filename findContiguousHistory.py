"""
asked by Karat-Wayfair
We have some clickstream data that we gathered on our client's website. Using cookies, we collected snippets of users' anonymized URL histories while they browsed the site. The histories are in chronological order, and no URL was visited more than once per person.

Write a function that takes two users' browsing histories as input and returns the longest contiguous sequence of URLs that appears in both.

Sample input:

user0 = ["/start", "/green", "/blue", "/pink", "/register", "/orange", "/one/two"]
user1 = ["/start", "/pink", "/register", "/orange", "/red", "a"]
user2 = ["a", "/one", "/two"]
user3 = ["/pink", "/orange", "/yellow", "/plum", "/blue", "/tan", "/red", "/amber", "/HotRodPink", "/CornflowerBlue", "/LightGoldenRodYellow", "/BritishRacingGreen"]
user4 = ["/pink", "/orange", "/amber", "/BritishRacingGreen", "/plum", "/blue", "/tan", "/red", "/lavender", "/HotRodPink", "/CornflowerBlue", "/LightGoldenRodYellow"]
user5 = ["a"]
user6 = ["/pink","/orange","/six","/plum","/seven","/tan","/red", "/amber"]

Sample output:

findContiguousHistory(user0, user1) => ["/pink", "/register", "/orange"]
findContiguousHistory(user0, user2) => [] (empty)
findContiguousHistory(user2, user1) => ["a"]
findContiguousHistory(user5, user2) => ["a"]
findContiguousHistory(user3, user4) => ["/plum", "/blue", "/tan", "/red"]
findContiguousHistory(user4, user3) => ["/plum", "/blue", "/tan", "/red"]
findContiguousHistory(user3, user6) => ["/tan", "/red", "/amber"]

n: length of the first user's browsing history
m: length of the second user's browsing history

"""


user0 = ["/start", "/green", "/blue", "/pink", "/register", "/orange", "/one/two"]
user1 = ["/start", "/pink", "/register", "/orange", "/red", "a"]
user2 = ["a", "/one", "/two"]
user3 = ["/pink", "/orange", "/yellow", "/plum", "/blue", "/tan", "/red", "/amber", "/HotRodPink", "/CornflowerBlue", "/LightGoldenRodYellow", "/BritishRacingGreen"]
user4 = ["/pink", "/orange", "/amber", "/BritishRacingGreen", "/plum", "/blue", "/tan", "/red", "/lavender", "/HotRodPink", "/CornflowerBlue", "/LightGoldenRodYellow"]
user5 = ["a"]
user6 = ["/pink","/orange","/six","/plum","/seven","/tan","/red", "/amber"]

def findContiguousHistory(user1,user2):
    result=[]
    temp=[]
    index_2=0
    for i in range(len(user1)):
        if user1[i] in user2:
            #print(user1[i], "found in the other list",count_contiguous_seq,max)
            temp.append(user1[i])
            if len(temp)>len(result):
                #print("len(temp)>len(result)")
                result=temp
        else:
            count_contiguous_seq=0
            temp=[]
    print(result)
    return result

findContiguousHistory(user0,user1)
findContiguousHistory(user0, user2) #=> [] (empty)
findContiguousHistory(user2, user1) #=> ["a"]
findContiguousHistory(user5, user2) #=> ["a"]
findContiguousHistory(user3, user4) #=> ["/plum", "/blue", "/tan", "/red"]
#findContiguousHistory(user4, user3) #=> ["/plum", "/blue", "/tan", "/red"]
findContiguousHistory(user3, user6)# => ["/tan", "/red", "/amber"]




    result=[]
    temp=[]
    index_1=0
    index_2=0
    while index_1<len(user1):
        print("index1  __", user1[index_1]  )
        index_2=0
        while index_2<len(user2):
            #print(index_1 , "VS", index_2)
            if index_1<len(user1) and index_2<len(user2) and user1[index_1] == user2[index_2]:
                temp.append(user1[index_1])
                #print("temp",temp, index_1)
                if index_2==len(user2)-1:
                    if len(temp)>len(result):
                        result=temp
                        temp=[]
                        index_2=0

                #index_1+=1
                index_2+=1


            elif len(temp)>0:
                print("need to reset temp")
                if len(temp)>len(result):
                    result=temp
                    #print(result)
                #index_1+=1
                temp=[]
                index_2=0
                print(index_1)
                break

            else:
                #print("else")
                index_2+=1

        index_1+=1
        #print("index_1",index_1)
    print(result)
    return result

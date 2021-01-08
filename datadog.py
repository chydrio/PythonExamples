# Determine the number of repeated words in a paragraph.

# paragraph = "The Sun is the star at the center of the Solar System. It is a nearly perfect sphere of hot plasma, with internal convective motion that generates a magnetic field via a dynamo process. It is, by far, the most important source of energy for life on Earth."

# count_repeated(paragraph) => 11

# "the" is seen 5 times (i.e. 4 repetitions)
# "is" is seen 3 times (i.e. 2 repetitions)
# "of" is seen 3 times (i.e. 2 repetitions)
# "it" is seen 2 times (i.e. 1 repetition)
# "a" is seen 3 times (i.e. 2 repetitions)

# hence number of repeated words is 4+2+2+1+2 = 11

from collections import Counter

def count_repeated(paragraph):
    set=".,"
    array=paragraph.split()
    newarray=[x.lower() for x in array ]
    newarray2=[]
    #newarray=[x for x in newarray if x not in set]
    for word in newarray:
        word=word.replace(",","")
        word=word.replace(".","")
        newarray2.append(word)

    #print(newarray2)

    #print(array)
    #print(newarray)
    nbr=0
    count=Counter(newarray2)
    #print(count)
    for key,value in count.items():
        #print(key,value)
        if value>1:
            #print(key,value)
            nbr+=value-1
            #print(nbr)
    return nbr



paragraph = "The Sun is the star at the center of the Solar System. It is a nearly perfect sphere of hot plasma, with internal convective motion that generates a magnetic field via a dynamo process. It is, by far, the most important source of energy for life on Earth."

print(count_repeated(paragraph))



# jobs = [
#     # job_id, job_time, child_job_ids
#     [1, 30, [2, 4]],
#     [2, 10, [3]],
#     [4, 60, []],
#     [3, 20, []],
# ]

# find_total_job_time(jobs, 1) # 30 + (10+20) + 60 = 120
# find_total_job_time(jobs, 2) # 10 + 20 = 30
# find_total_job_time(jobs, 4) # 60


find_total_job_time

    return time1+ find_total_job_time(child1)

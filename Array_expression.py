def findStudents(k, a):
    """"
    nbrLate=0
    for time in a:
        if time>0:
            nbrLate+=1
    nbrPresent= len(a)- nbrLate
    if nbrPresent>=k:
        return "NO"
    else:
        return "YES"
        #class cancelled

    """""

    #oneliner:
    if len([time for time in a if time<=0])>=k: return "NO"
    else: return "YES"

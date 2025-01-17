def sommeList(l):
    s=0
    for i in l:
        s=s+i
    return s


def motsLongeur(n ,l):
    motLongeur=[]
    for i in l :
        if len(i)>=n :
            motLongeur.append(i)
    return motLongeur

l=['ghoutoub', 'Houssein-dev']

#print(motsLongeur(5,l))


def isHasCommun(l1,l2):
    for i in l1 :
        for j in l2 :
            if i==j:
               return True      
    return False

l1=[]
l2=[]        
def saisir(l):
    s=input("pour ajouter un element dans "+str(l)+" press \'A\' ,autre key pour arreter : ")

    while (s=='A'):
        l.append(input())
        s=input("pour ajouter un element press \'A\' ,autre key pour arreter")
    return l

saisir(l1)
saisir(l2)

print("list de mot log :" , motsLongeur(3,l1))
print(isHasCommun(l1,l2))     

#faire le somme 

#print(sommeList(saisir(l1),saisir(l2))) #decommenter ce ligne si vous avez listes contient nombres
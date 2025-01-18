
# ==========================================================
# ============= EXO :3       ===============================
# ==========================================================
def replaceAll(targrt_str , find_str ,replace_str):
    temp=''
    i=0
    for char in targrt_str :
        if char==find_str :
            temp+=replace_str
        else :
            temp+=char
    return temp
         
print("=============================================\n===========start l\execution d'exo 3=========\n=============================================")
        
print(replaceAll("Good","o","u"))  #===> Guud

# ==========================================================
# ============= EXO :4       ==============================
# ==========================================================
import uuid
class Person:
    
    #constructors
    def __init__(self,age , name , id=uuid.uuid4()):
        self.id=id
        self.name=name
        self.age=age
    
    
    def __str__(self):
        return f" Gtid :{self.id }\n Name :{self.name} \n age :{self.age}"    
    #getters
    def getId(self):
        return self.id
    
    def getName(self):
        return self.name 
    
    def getAge(self):
        return self.age
    
    #setters
    
    def setId(self, nv_id):
        self.id=nv_id
        
    def setName(self, nv_name):
        self.name=nv_name
        
    def setAge(self, nv_age):
        self.age=nv_age
        
        
    @staticmethod  
    def areEqualObj(obj1 , obj2):
        
        return obj1.id==obj2.id
    
print("=============================================\n===========start l\execution d'exo 4=========\n=============================================")
 
obj1=Person( "houssein",15)

obj2=Person( 2,"houssein",15)

print(obj1)
print(obj2)
print(f" resultat de compaireson entre le deux person :{Person.areEqualObj(obj1, obj2)}")


# ==========================================================
# ============= EXO :5       ==============================
# ==========================================================

class TodoItem:
    def __init__(self , title , description ,completed=False):
        self.title=title
        self.description=description
        self.completed=completed
        
    def __str__(self):
        return f"{self.title}\n {self.description}\n {self.completed}"
    
    def getTitle(self):
        return self.title
    
    def getDescription(self):
        return self.description
    
    def getCompletedStatus(self):
        return self.completed
    
    def setTitle(self , nv_title):
        
        if type(nv_title)==str :
           self.title=nv_title 
        else :
           self.title=None
        
    
    def setDescription(self ,nv_description):
       if type(nv_description)==str :
           self.description=nv_description 
       else :
           self.description=None
    def setCompletedStatus(self ,nv_completed):
       if type(nv_completed)==bool :
           self.completed=nv_completed 
       else :
           self.completed=None
print("=============================================\n===========start l\execution d'exo 5=========\n=============================================")
   
# for test decomment this under lines  

item1=TodoItem("frontend-menoter","this is a frontend community",False)
print(f"valeur title avant la modification :\n {item1}") 
item1.setTitle(1)      
print(f"valeur title apres la modification :\n {item1}") 

# ==========================================================
# ============= EXO :6       ==============================
# ==========================================================
class Pile:
    def __init__(self):
        self.pile_container=[]
    
    
    def __str__(self):
        return self.pile_container
    
    def est_vide(self):
        return self.pile_container==[]
    
    def depiler(self):
        return self.pile_container.pop(-1)
    
    def empiler(self,char):
        self.pile_container.append(char)
        

def reverseChain(chain):
    chain_reverse=''
    pile1=Pile()
    for char in chain :
        pile1.empiler(char)

    while(not pile1.est_vide()):
        chain_reverse+=pile1.depiler()
    return chain_reverse
print("=============================================\n===========start l\execution d'exo 6=========\n=============================================")

print(reverseChain("Houssein-dev"))

# ==========================================================
# ============= EXO :7        ==============================
# ==========================================================


def inversePileByRecursion(pile,pile_inversee):
    
    if pile.est_vide(): 
        return pile_inversee
    else :
        pile_inversee.empiler(pile.depiler())
        return inversePileByRecursion(pile,pile_inversee)
    # 
    
print("=============================================\n===========start l\execution d'exo 7=========\n=============================================")
pile_inversee=Pile()
pile1=Pile()
pile1.empiler("dARK")
pile1.empiler("light")
pile1.empiler("7mass")


p=inversePileByRecursion(pile1,pile_inversee)
print(p.pile_container)
# ==========================================================
# ============= EXO :8        ==============================
# ==========================================================
class File :
    def __init__(self):
        self.pile1=Pile()
        self.pile2=Pile()
    


            
    def switchFromPileToOther(self,pile2,pile1):# cette methode est cree pour eviter la repetition de cette boucle selon pile vide 
        while(not pile2.est_vide()):
            if (len(pile2.pile_container))==1:
                return pile2.depiler()
            pile1.empiler(pile2.depiler())    
            
            
    def deQueue(self):
        if self.pile1.est_vide() and self.pile2.est_vide() :
            return "le file est vide"
        elif not self.pile1.est_vide() or not self.pile2.est_vide():
            if self.pile1.est_vide() :
                return self.switchFromPileToOther(self.pile2,self.pile1)
                
            elif self.pile2.est_vide() :
                
                return self.switchFromPileToOther(self.pile1,self.pile2)
            else :
                #dans cette cas on consider que qu'il ya le plus grand taille plus ancien que l'autre
                if len(self.pile2.pile_container) >=len(self.pile1.pile_container):
                    return self.switchFromPileToOther(self.pile1,self.pile2)
                else:
                    return self.switchFromPileToOther(self.pile2,self.pile1)
                
                
                
                
    def enQueue(self,x):
            if self.pile1.est_vide :
                self.pile2.empiler(x)
            elif self.pile2.est_vide()  :
                self.pile1.empiler(x)  
        
print("=============================================\n===========start l\execution d'exo 8=========\n=============================================")
               
file=File()
file.pile2.empiler("houssein")
file.pile2.empiler("hamoudi")
file.pile2.empiler("dev")

# file.pile2.empiler("goal2") #decommenter pour le cas les piles pas vide

print(file.deQueue())
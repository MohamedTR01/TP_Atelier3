# classe Point :
class Point:
    def __init__(self,x=0.0,y=0.0):
        self.x = x
        self.y = y
    def Afficher(self):
        return "("+str(self.x)+","+str(self.y)+")"
# classe Segment :
class Segment():
    # constructeur qui prend 2 objects Point comme parametre :
    def __init__(self,org,ext):
            self.org = Point(org.x,org.y)
            self.ext = Point(ext.x,ext.y)
    # La méthode d'affichage :
    def Afficher_S(self):
        return "(org,ext) Segment = ["+ self.org.Afficher() + " , "+ self.ext.Afficher() + "]"

# Une instance de la classe Point :
P1 = Point(4,5)
P2 = Point(2,3)
print(P1.Afficher())

# Une instance de la classe Segment :
Seg1= Segment(P1,P2)
print(Seg1.Afficher_S())
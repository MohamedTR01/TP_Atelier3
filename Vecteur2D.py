class Vecteur2D:
    # constructeur de la classe Vecteur2D :
    def __init__(self , x=0 , y=0):
        self.x = x
        self.y = y
    # La méthode d'affichage :
    def Afficher(self):
        return "x= "+str(self.x)+" , y="+str(self.y)
    # ajouter un opérateur :
    def __add__(self,other):
        ax= self.x+other.x
        ay= self.y+other.y
        return Vecteur2D(ax,ay)
# créer des vecteurs (objet) sans et avec deux paramètres :
v1 = Vecteur2D()
v2 =Vecteur2D(10 , 9)
v3 =Vecteur2D(1  , 3)
# tester la méthode d'affichage() :
print(v1.Afficher())
print(v2.Afficher())
print(v3.Afficher())
# tester l'operation (+) avec 2 vecteurs :
SommeVa= v2 + v3
print(SommeVa.Afficher())   
class Rectangle:
    # Constructeur de la classe Rectangle:
    def __init__(self , longueur , largeur):
        self.nom = "rectangle"
        self.longueur = longueur
        self.largeur = largeur

    # La méthode d'affichage
    def Afficher(self):
        print("[ " + self.nom + " | longueur : " + str(self.longueur) + " , largeur : " + str(self.largeur) + " ]")
    # La méthode de la surface :
    def Surface(self):
        print("la surface est : " +str(self.longueur * self.largeur))

# La classe Carré hérité de la classe Rectangle (Héritage) :
class Carre(Rectangle):
    # Constructor de la classe Carré :
    def __init__(self , longueur):
        super().__init__(longueur , longueur)
        self.nom = "carré"
     # La méthode d'affichage :
    def Afficher(self):
        print("[ " + self.nom + " | longueur : " + str(self.longueur) + " ]")

# Une instance de la classe Rectangle :
R = Rectangle(6,3)
R.Afficher()
R.Surface()

# Une instance de la classe Carre :
C = Carre(3)
C.Afficher()
C.Surface()
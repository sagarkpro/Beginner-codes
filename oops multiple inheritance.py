class ActionAnime:
    def __init__(self, name, genre, numEp, numSeason, releaseDate, ):
        self.name = name
        self.genre = genre
        self.numEp = numEp
        self.numSeason = numSeason
        self.releaseDate = releaseDate

    def printAction(self):
        print(f"The name of the anime is : '{self.name}' it is a {self.genre} anime and it has {self.numEp} episodes {self.numSeason} seasons. This anime was aired/airing on {self.releaseDate}")

class SuperNatural:
    def __init__(self, name, genre, numEp, numSeason, releaseDate, ):
        self.name = name
        self.genre = genre
        self.numEp = numEp
        self.numSeason = numSeason
        self.releaseDate = releaseDate

    def printSuperNatural(self):
        print(
            f"The name of the anime is : '{self.name}' it is a {self.genre} anime and it has {self.numEp} episodes {self.numSeason} seasons. This anime was aired/airing on {self.releaseDate}")

class SuperDuper(ActionAnime, SuperNatural): #The class which is inherited first (ActionAnime in this case) will always be prioritised, i.e if a variable/function has the same name in both the classes imported then the variable/funtion of the first class will be executed if it is used in this class.

    def printSuperDuper(self):
        ActionAnime.printAction(self)
naruto = ActionAnime("Naruto: Shippuden", ["Action", "Drama", "Comedy", "Adventure", "Action fiction"], 500, 21, 2007)
bakemonogatari = SuperNatural("Bakemonogatari", ["Romance", "Drama", "Comedy", "Seinen manga", "Supernatural"], 15, 1, 2009)
jojo = SuperDuper("JoJo's Bizarre Adventure", ["Adventure", "Horror", "Action", "Drama", "Action fiction", "Suspense", "Adventure fiction", "Supernatural fiction"], 164, 5, 2012) #for e.g. here the init self funtion of the class ActionAnime is used instead of the class Supernatural because the class ActionAnime was inherited first
naruto.printAction()
bakemonogatari.printSuperNatural()
jojo.printSuperDuper()
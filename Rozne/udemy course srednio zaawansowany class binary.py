import pickle
import glob


class Cake:
    known_types = ['cake', 'muffin', 'meringue', 'biscuit', 'eclair', 'christmas', 'pretzel', 'other']
    bakery_offer = []

    def __init__(self, name, kind, taste, addictions, filling, gluten_free, text):
        self.name = name
        self.kind = kind
        self.taste = taste
        self.addictions = addictions
        self.filling = filling
        if self.kind in Cake.known_types:
            self.kind = kind
        else:
            Cake.known_types.append('other')
        Cake.bakery_offer.append(self)
        self.__gluten_free = gluten_free
        if self.kind == "cake" or text == " ":
            self.__text = text
        else:
            self.__text = None

    def show_info(self):
        print(f"Name: {self.name.upper()}")
        print(f"Kind: {self.kind}")
        print(f"Taste: {self.taste}")
        if self.addictions:
            print(f"Addictions: {self.addictions}")
        if self.filling:
            print(f"Filling: {self.filling}")
        print(f"Gluten free: {self.__gluten_free}")
        if self.__text:
            print(f"Text: {self.__text}")
        print("-" * 20)

    def set_filling(self, filling):
        self.filling = filling

    def new_filling(self):
        filling = input("New filling: ")
        self.filling = filling

    def add_additives(self, additives):
        self.addictions.extend(additives)

    def set_additives(self):
        additives = []
        how_many = int(input("How many additives: "))
        for f in range(how_many):
            add = input("Type of additive: ")
            additives.append(add)
        return self.addictions.extend(additives)

    def __get_text(self):
        return self.__text

    def __set_text(self, new_text):
       if self.kind == "cake":
            print(f"Changing Cake text from {self.__text} to {new_text}")
            self.__text = new_text
       else:
            print("Cannot change text!")

    Text = property(__get_text, __set_text, None, "If kind is Cake change text")

    def save_to_path(self, path):
        with open(path, 'wb') as f:
            pickle.dump(self, f)

    @classmethod
    def read_from_file(cls, path):
        with open(path, 'rb') as f:
            new_cake = pickle.load(f)
        cls.bakery_offer.append(new_cake)
        return new_cake

    @staticmethod
    def get_bakery_files(path):
        return glob.glob(path+'/*.bakery')


cake01 = Cake('Vanilla Cake', 'cake', 'vanilla', ['chocolade', 'nuts'], 'cream', False, "Whazaap")
cake02 = Cake('Chocolade Muffin', 'muffin', 'chocolade', ['chocolade'], '', False, "")
cake03 = Cake('Super Sweet Maringue', 'meringue', 'very sweet', [], '', True, "")
cake04 = Cake('Cocoa waffle', 'waffle', 'cocoa', [], 'cocoa', False, "")


cake01.save_to_path('D:/temp/cake01.bakery')
cake02.save_to_path('D:/temp/cake02.bakery')

cake05 = Cake.read_from_file('D:/temp/cake01.bakery')
cake05.show_info()

print(Cake.get_bakery_files('D:/temp/'))
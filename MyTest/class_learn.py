# # class Character:
# #     """
# #     This is a class that represents the player character.
# #     """
# #     def __init__(self):
# #         """ This is a method that sets up the variables in the object. """
# #         self.name = ""
# #         self.outfit = ""
# #         self.max_hit_points = 0
# #         self.current_hit_points = 0
# #         self.armor_amount = 0
# #         self.max_speed = 0
# # class Address:
# #     """ Hold all the fields for a mailing address. """
# #     def __init__(self):
# #         """ Set up the address fields. """
# #         self.char=""
# #         self.name = ""
# #         self.line1 = ""
# #         self.line2 = ""
# #         self.city = ""
# #         self.state = ""
# #         self.zip = ""
# #
# # def main():
# #     # Create an address
# #     my_address = Address()
# #
# #     # Alert! This does not set the address's name!
# #     name = "Dr. Smith"
# #
# #     # This doesn't set the name for the address either
# #     # print(Address.name)
# #     print("00000000")
# #     Address.name = "Dr. Smith"
# #     print(type(Address.name))
# #     your_addr=Address()
# #     # This runs, creates a new attribute but with the wrong name.
# #     my_address.name = "Dr. Smith"
# # #
# # #     # This does work:
# # #     my_address.name = "Dr. Smith"
# #
# # class Address:
# #     def __init__(self,
# #                  name: str = "",
# #                  line1: str = "",
# #                  line2: str = "",
# #                  city: str = "",
# #                  state: str = "",
# #                  zip_code: str = ""
# #                  ):
# #         self.name: str = name
# #         self.line1: str = line1
# #         self.line2: str = line2
# #         self.city: str = city
# #         self.state: str = state
# #         self.zip_code: str = zip_code
# #
# #
# #
# # def main():
# #     # This creates the address
# #     my_address = Address("701 N. C Street",
# #                          "Carver Science Building",
# #                          "Indiana",
# #                          "IA",
# #                          50125,
# #                          "USA")
# class Cat:
#    population = 0
#    def __init__(self, name):
#         self.name = name
#         Cat.population += 1
#
# def main():
#     cat1 = Cat("Pat")
#     cat1.population=99
#     print("The cat population is:", Cat.population)
#     print("The cat population is:", cat1.population)
#     cat2 = Cat("Pepper")
#     print("The cat population is:", Cat.population)
#     print("The cat population is:", cat1.population)
#     cat3 = Cat("Pounce")
#     print("The cat population is:", Cat.population)
#     print("The cat population is:", cat1.population)
#     print("--------------------------")
#
# if __name__ == '__main__':
#     main()
# def give_money1(person):
#     person.money += 100
#
#
# class Person:
#     def __init__(self):
#         self.name = ""
#         self.money = 0
#     # def give_money1(self,money):
#     #     self.money+=money

#
# def main():
#     bob = Person()
#     bob.name = "Bob"
#     bob.money = 100
#
#     give_money1(bob)
#     # bob.give_money1(100)
#     print(bob.money)

class Boat:
    def __init__(self):
        self.tonnage = 0
        self.name = ""
        self.is_docked = True

    def dock(self):
        if self.is_docked:
            print("You are already docked.")
        else:
            self.is_docked = True
            print("Docking")

    def undock(self):
        if not self.is_docked:
            print("You aren't docked.")
        else:
            self.is_docked = False
            print("Undocking")

class Submarine(Boat):
    def __init__(self):
        # super(Submarine,self).__init__()
        # Boat.__init__(self)
        super().__init__()
        print("Submerge!")
    def submerge(self):
        print("Submerge!")
    def download(self):
        print("Downloading")
class OXSubmarine(Submarine):
    def __init__(self):
        # super(Submarine,self).__init__()
        # Boat.__init__(self)
        super().__init__()
        print("OXSubmerge!")

def main():
    # b = Boat()
    #
    # b.dock()
    # b.undock()
    # b.undock()
    # b.dock()
    # b.dock()
    s=OXSubmarine()
    s.dock()


if __name__ == '__main__':
    main()

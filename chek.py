"""Task 1"""

from collections.abc import Iterable


class Auto:
    def ride(self):
        print("Riding on a ground")

class Boat:
    def swim(self):
        print("Floating on water")

class Amphibian(Auto, Boat):
    pass

obj = Amphibian()
obj.ride()
obj.swim()

"""Task 2"""

class ContactList(list):
    def __init__(self,lst) -> None:
        self.lst = lst
    def search_by_name(self,name):
        lst_ = []
        for i in self.lst:
           if name in i:
               lst_.append(i)
        return lst_
            
all_contacts = ContactList(['Ivan', 'Maris', 'Olga', 'Ivan Olya', 'Olya Ivan', 'ivan'])
print(all_contacts.search_by_name('Olya'))       
        
           
        

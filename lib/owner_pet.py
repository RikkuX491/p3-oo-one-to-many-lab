class Pet:

    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]

    all = []
    
    def __init__(self, name, pet_type, owner=None):
        self.name = name
        self.pet_type = pet_type
        self.owner = owner
        Pet.all.append(self)

    @property
    def pet_type(self):
        return self._pet_type
    
    @pet_type.setter
    def pet_type(self, pet_type_parameter):
        if(pet_type_parameter in Pet.PET_TYPES):
            self._pet_type = pet_type_parameter
        else:
            raise Exception

class Owner:
    
    def __init__(self, name):
        self.name = name

    def pets(self):
        return [pet for pet in Pet.all if pet.owner is self]
    
    def add_pet(self, pet):
        if(isinstance(pet, Pet)):
            pet.owner = self
        else:
            raise Exception("Input value for pet must be of type Pet!")
        
    def get_sorted_pets(self):
        return sorted(self.pets(), key = lambda p: p.name)
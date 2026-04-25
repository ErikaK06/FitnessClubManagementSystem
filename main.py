from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self, name, person_id):
        self.name = name
        self.person_id = person_id

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if isinstance(value, str) and len(value.strip()) > 0:
            self._name = value
        else:
            raise ValueError("Name cannot be empty")
        
    @abstractmethod
    def get_details(self) -> str:
        pass

    
class Member(Person):
    def __init__(self, name, member_id, sub_type):
        super().__init__(name, member_id)
        self.subscription_type = sub_type

    @property
    def person_id(self):
        return self.__person_id

    @person_id.setter
    def person_id(self, value):
        if len(value) == 6 and value.startswith('M') and value[1:].isdigit():
            self.__person_id = value
        else:
            raise ValueError("Member ID must start with 'M' followed by 5 digits")

    def get_details(self) -> str:
        return f"[Member] {self.name} (ID: {self.person_id}) - Sub: {self.subscription_type}"     
    

class Trainer(Person):
    def __init__(self, name, trainer_id, specialization, salary):
        super().__init__(name, trainer_id)
        self.specialization = specialization
        self.salary = salary

    @property
    def person_id(self):
        return self.__person_id

    @person_id.setter
    def person_id(self, value):
        if len(value) == 6 and value.startswith('T') and value[1:].isdigit():
            self.__person_id = value
        else:
            raise ValueError("Member ID must start with 'T' followed by 5 digits")

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, value):
        if value > 0:
            self.__salary = value
        else:
            raise ValueError("Salary must be a positive number") 
        
    def get_details(self) -> str:
        return f"[Trainer] {self.name} (ID: {self.person_id}) - Spec: {self.specialization}, Salary: €{self.salary}"
    

class FitnessClub:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(FitnessClub, cls).__new__(cls)
        return cls._instance

    def __init__(self, club_name: str):
        if not hasattr(self, 'initialized'):
            self.club_name = club_name
            self.initialized = True    


if __name__ == "__main__":
    club1 = FitnessClub("Super Gym")
    club2 = FitnessClub("Fake Gym")

    print(f"Club 1 name: {club1.club_name}")
    print(f"Club 2 name: {club2.club_name}")
    
    print(f"Are club1 and club2 the exact same object? {club1 is club2}")
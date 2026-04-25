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
            self.members = []
            self.trainers = []
            self.initialized = True

    def add_members(self, member: Member):
        if isinstance(member, Member):
            self.members.append(member)

    def add_trainers(self, trainer: Trainer):
        if isinstance(trainer, Trainer):
            self.trainers.append(trainer) 

    def show_everyone(self):
        print(f"Club: {self.club_name}")
        for person in self.members + self.trainers:
            print(person.get_details())   


if __name__ == "__main__":
    my_club = FitnessClub("Super Gym")
    
    m1 = Member("Erika", "M12345", "Annual")
    t1 = Trainer("Alex", "T55555", "Yoga", 1500)
    m2 = Member("Jessica", "M12345", "Monthly")

    my_club.add_members(m1)
    my_club.add_trainers(t1)
    my_club.add_members(m2)

    my_club.show_everyone()
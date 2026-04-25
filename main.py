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
            raise ValueError("Trainer ID must start with 'T' followed by 5 digits")

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
        return f"[Trainer] {self.name} (ID: {self.person_id}) - Spec: {self.specialization}, Salary: ${self.salary}"
    

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
            existing_ids = [p.person_id for p in self.members + self.trainers]
            if member.person_id in existing_ids:
                print(f"Error: ID {member.person_id} is already taken!")
            else:
                self.members.append(member)

    def add_trainers(self, trainer: Trainer):
        if isinstance(trainer, Trainer):
            existing_ids = [p.person_id for p in self.members + self.trainers]
            if trainer.person_id in existing_ids:
                print(f"Error: ID {trainer.person_id} is already taken!")
            else:
                self.trainers.append(trainer) 

    def show_everyone(self):
        print(f"Club: {self.club_name}")
        for person in self.members + self.trainers:
            print(person.get_details())

    def save_to_file(self, filename: str):
        with open(filename, 'w') as f:
            for person in self.members + self.trainers:
                f.write(person.get_details() + "\n")
        print(f"Data successfully saved to {filename}")

    def load_from_file(self, filename: str):
        try:
            print(f"\n Loading Data from {filename}")
            with open(filename, 'r') as f:
                for line in f:
                    print(line.strip())
        except FileNotFoundError:
            print(f"Error: The file {filename} was not found.")

    def interactive_menu(self):
        path = "FitnessClubManagementSystem/roster.txt"

        while True:
            print(f"\n {self.club_name} Menu")
            print("1. Add Member")
            print("2. Add Trainer")
            print("3. Show Everyone")
            print("4. Save to File")
            print("0. Exit") 

            choice = input("Select an option (0-4): ")

            if choice == "1":
                try:
                    name = input("Enter name: ")
                    member_id = input("Enter ID (M_____): ")
                    sub = input("Enter Subscription (Annual/Monthly): ")
                    self.add_members(Member(name, member_id, sub))
                except ValueError as e: 
                    print(f"-> Input Error: {e}")

            elif choice == "2":
                try:
                    name = input("Enter name: ")
                    trainer_id = input("Enter ID (T_____): ")
                    spec = input("Enter Specialization (Joga/Pilatess/Dance/Fitness/Cardio): ")
                    sal = input("Enter Salary (numbers only): ")
                    self.add_trainers(Trainer(name, trainer_id, spec, float(sal)))
                except ValueError as e: 
                    if "could not convert string to float" in str(e):
                        print("-> Error: Salary must be a number.")
                    else:
                        print(f"-> Input Error: {e}")

            elif choice == "3":
                self.show_everyone()
            elif choice == "4":
                self.save_to_file(path)
            elif choice == "0":  
                self.save_to_file(path)
                print("Exiting program. Goodbye!")
                break 
            else:
                print("-> Invalid choice. Please enter a number from 0 to 4.")

if __name__ == "__main__":
    my_club = FitnessClub("FIttnessClub")
    my_club.load_from_file("FitnessClubManagementSystem/roster.txt")
    my_club.interactive_menu()
# Fitness Club Management System

## Introduction

### What is your application?
The **Fitness Club Management System** is a professional console-based application written in Python. It is designed to help gym administrators manage their staff (Trainers) and clients (Members) in a single centralized system. The program ensures data integrity through strict validation rules and provides a persistent storage solution via local file synchronization.

### How to run the program?
To run the application, follow these steps:
1. Ensure you have **Python 3.8+** installed.
2. Clone the repository to your local machine.
3. Open your terminal or command prompt in the project folder.
4. Run the main script using the command:  
   `python main.py`

### How to use the program?
Once started, the program displays an interactive menu. You can navigate it by entering numbers:
* **Option 1**: Add a new Member (requires Name, ID starting with 'M', and Subscription type).
* **Option 2**: Add a new Trainer (requires Name, ID starting with 'T', Specialization, and Salary).
* **Option 3**: Display the full roster of the club.
* **Option 4**: Manually save all current data to `roster.txt`.
* **Option 0**: Safely exit the program (data is saved automatically upon exit).

---

## Body/Analysis

### Functional Requirements & OOP Pillars

The application is built on the four fundamental pillars of Object-Oriented Programming to ensure modularity and scalability.

**1. Abstraction**

I used the `ABC` module to create an abstract base class `Person`. It defines the essential structure for any individual in the system but cannot be instantiated itself. It forces all subclasses to implement the `get_details()` method.

```python
class Person(ABC):
    @abstractmethod
    def get_details(self) -> str:
        pass
```

**2. Inheritance**

The `Member` and `Trainer` classes inherit from `Person`. This allows them to reuse common attributes like `name` and `person_id` while extending the functionality with their own unique properties.

```python
class Member(Person):
    def __init__(self, name, member_id, sub_type):
        super().__init__(name, member_id)
        self.subscription_type = sub_type
```

**3. Encapsulation**

To protect data integrity, I implemented private attributes (prefixed with `__`) and used `@property` decorators. For instance, the system prevents entering negative salaries or incorrectly formatted IDs by raising a `ValueError`.

```python
@property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, value):
        if float(value) > 0:
            self.__salary = float(value)
        else:
            raise ValueError("Salary must be a positive number")
```

**4. Polymorphism**

Polymorphism is demonstrated through method overriding. Both `Member` and `Trainer` have their own implementation of `get_details()`. When the club displays the roster, it calls this method on every object in the list, and Python automatically executes the correct version based on the object's type.

### Design Patterns: Singleton

I implemented the Singleton pattern for the `FitnessClub` class. This ensures that only one instance of the club management system exists at any time, preventing data conflicts between different "club" objects.

```python

class FitnessClub:
    _instance = None
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(FitnessClub, cls).__new__(cls)
        return cls._instance
```
### Aggregation Principle
The program uses `Aggregation` to manage data. The `FitnessClub` class "has" lists of `Member` and `Trainer` objects. These objects are created independently and then added to the club's collection, meaning they can exist outside the club's context.

### File I/O
The system supports persistent data storage. It writes formatted data to `roster.txt` using the `save_to_file` method and attempts to load existing records upon startup using `load_from_file`, ensuring that no data is lost when the program is closed.

```python

def save_to_file(self, filename: str):
        with open(filename, 'w') as f:
            for person in self.members + self.trainers:
                f.write(person.get_details() + "\n")
        print(f"Data successfully saved to {filename}")
```

```python

def load_from_file(self, filename: str):
        try:
            print(f"\n Loading Data from {filename}")
            with open(filename, 'r') as f:
                for line in f:
                    print(line.strip())
        except FileNotFoundError:
            print(f"Error: The file {filename} was not found.")
```

### Testing
Core functionality is heavily covered by unit tests using the built-in `unittest` framework. The test suite ensures the reliability of the system by verifying the following scenarios:

**1. Encapsulation & Validation Tests:**
* `test_member_id_validation`: Verifies that a `ValueError` is raised when an invalid Member ID (e.g., missing 'M' or incorrect length) is provided.
* `test_trainer_id_validation`: Ensures Trainer IDs strictly follow the 'T' + 5 digits format.
* `test_salary_validation`: Checks that negative salaries or non-numeric inputs for a Trainer raise appropriate exceptions.

**2. Pattern & Structure Tests:**
* `test_singleton_instance`: Confirms that multiple instantiations of the `FitnessClub` class return the exact same object in memory, preserving data consistency.
* `test_aggregation_logic`: Verifies that `Member` and `Trainer` objects are independently created and correctly appended to the club's internal lists.

**3. Business Logic Tests:**
* `test_prevent_duplicate_ids`: Ensures the system successfully blocks the addition of a new person if their ID already exists in the club's roster.
* `test_polymorphism_output`: Checks that the `get_details()` method returns the correctly formatted string depending on the specific class of the object.

**4. File I/O Tests:**
* `test_save_and_load_data`: Verifies that the system can properly format data, write it to a text file, and read it back without data loss.

---

## Results and Summary
### Results
* The application successfully manages gym data through an interactive CLI.
* All four OOP pillars were correctly implemented and documented.
* **Challenges:** One major challenge was implementing robust error handling for user inputs (e.g., handling strings when numbers are expected). This was resolved using `try-except` blocks within the interactive menu.

### Conclusions
This coursework successfully achieved its goal of creating a scalable management system using Python and OOP principles. The project demonstrates a clear understanding of inheritance, encapsulation, and design patterns. The result is a reliable tool for basic gym administration.

**Future Prospects:**
* **GUI Extension:** Developing a graphical interface using the `tkinter` library for better user experience.
* **Database Integration:** Moving from text files to a proper SQL database (like SQLite) for more complex data queries.
* **Advanced Tracking:** Adding features for membership expiration dates and workout logs.

---

## 4. References
1. Python Documentation (unittest, abc).
2. PEP 8 – Style Guide for Python Code.
3. Design Patterns: Singleton Pattern Guidelines.

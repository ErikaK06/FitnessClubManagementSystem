import unittest
import os

from main import Member, Trainer, FitnessClub

class TestFitnessManagementSystem(unittest.TestCase):

    def setUp(self):
        """Reset the Singleton and prepare a fresh club instance before each test."""
        FitnessClub._instance = None
        self.club = FitnessClub("Validation Gym")

    def test_member_invalid_id_format(self):
        """Verify that IDs not starting with 'M' followed by 5 digits raise ValueError."""
        with self.assertRaises(ValueError):
            Member("User", "X12345", "Annual")
        with self.assertRaises(ValueError):
            Member("User", "M123", "Annual")

    def test_trainer_negative_salary(self):
        """Verify that negative salaries are caught by the setter validation."""
        with self.assertRaises(ValueError):
            Trainer("Coach", "T11111", "Yoga", -500)

    def test_singleton_instance_integrity(self):
        """Verify that multiple FitnessClub calls return the exact same object."""
        another_club = FitnessClub("Different Name")
        self.assertIs(self.club, another_club)
        self.assertEqual(self.club.club_name, "Validation Gym")

    def test_duplicate_id_prevention(self):
        """Verify that the club prevents adding different people with the same ID."""
        m1 = Member("Erika", "M12345", "Annual")
        m2 = Member("Jessica", "M12345", "Monthly")
        self.club.add_members(m1)
        self.club.add_members(m2)
        self.assertEqual(len(self.club.members), 1)

    def test_persistence_logic(self):
        """Verify the system can write data to a physical file."""
        m = Member("Erika", "M12345", "Annual")
        self.club.add_members(m)
    
        path = "FitnessClubManagementSystem/roster_test.txt"
        self.club.save_to_file(path)
        self.assertTrue(os.path.exists(path))
        
        if os.path.exists(path):
            os.remove(path)

if __name__ == "__main__":
    unittest.main()
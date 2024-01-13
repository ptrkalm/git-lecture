import unittest
from src.services import user_generator

class TestUserGenerator(unittest.TestCase):
    def test_should_generate_user(self):
        user = user_generator.generate_user()
        self.assertNotEqual(user.name, None)

    def test_should_generate_male_user(self):
        user = user_generator.generate_user('male')
        self.assertEqual(user.gender, 'male')

    def test_should_generate_female_user(self):
        user = user_generator.generate_user('female')
        self.assertEqual(user.gender, 'female')    

if __name__ == '__main__':
    unittest.main()
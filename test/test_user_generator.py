import unittest
from src.services import user_generator

class TestUserGenerator(unittest.TestCase):
    def test_should_generate_user(self):
        user = user_generator.generate_user()
        self.assertNotEqual(user.name, None)

if __name__ == '__main__':
    unittest.main()
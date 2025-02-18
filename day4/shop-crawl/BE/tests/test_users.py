import unittest
from app.repositories.user_repository import UserRepository

class TestUserRepository(unittest.TestCase):
    def test_create_user(self):
        """사용자 생성 테스트"""
        result = UserRepository.create_user("test_user@example.com", "hashed_password", "테스트 유저")
        self.assertTrue(result)

    def test_get_user_by_email(self):
        """이메일로 사용자 조회 테스트"""
        user = UserRepository.get_user_by_email("test_user@example.com")
        self.assertIsNotNone(user)
        self.assertEqual(user.email, "test_user@example.com")

if __name__ == "__main__":
    unittest.main()

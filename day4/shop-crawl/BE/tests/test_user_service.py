import unittest
from app.services.user_service import UserService

class TestUserService(unittest.TestCase):
    def test_register_user(self):
        """사용자 등록 테스트"""
        result = UserService.register_user("service_test@example.com", "hashed_password", "서비스 유저")
        self.assertTrue(result)
        
    def test_get_user_info(self):
        """사용자 정보 조회 테스트"""
        user = UserService.get_user_info("service_test@example.com")
        self.assertIsNotNone(user)
        self.assertEqual(user.email, "service_test@example.com")
        
if __name__ == "__main__":
    unittest.main()
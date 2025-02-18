from user.repositories.user_repository import UserRepository

class UserService:
    @staticmethod
    def register_user(email, password, name):
        """새로운 사용자 등록"""
        # 비밀번호 해싱 (추후 적용)
        return UserRepository.create_user(email, password, name)

    @staticmethod
    def get_user_info(email):
        """이메일로 사용자 정보 조회"""
        return UserRepository.get_user_by_email(email)

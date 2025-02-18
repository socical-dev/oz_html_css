from user.models.user import User
from connectDB import get_connection

class UserRepository:
    @staticmethod
    def create_user(email, password, name):
        """새로운 사용자 생성"""
        connection = get_connection()
        try:
            with connection.cursor() as cursor:
                sql = "INSERT INTO users (email, password, name) VALUES (%s, %s, %s)"
                cursor.execute(sql, (email, password, name))
            connection.commit()
            return True
        except Exception as e:
            print("UserRepository.create_user Error:", e)
            return False
        finally:
            connection.close()

    @staticmethod
    def get_user_by_email(email):
        """이메일로 사용자 조회"""
        connection = get_connection()
        try:
            with connection.cursor() as cursor:
                sql = "SELECT * FROM users WHERE email = %s"
                cursor.execute(sql, (email,))
                result = cursor.fetchone()
                if result:
                    return User(**result)  # User 객체로 변환
                return None
        finally:
            connection.close()
import os
import pymysql
from dotenv import load_dotenv
import pymysql.cursors

# .env 파일 로드
env_path = "/Volumes/socical/oz/project/oz_project/.env"
load_dotenv(env_path)

# 환경 변수에서 MySQL 연결 정보 가져오기
DB_HOST = os.getenv("DB_HOST")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")

# MySQL 연결 설정
def get_connection():
    return pymysql.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME,
        charset="utf8mb4",
        cursorclass=pymysql.cursors.DictCursor
    )
    
# 연결 테스트
if __name__ == "__main__":
    try:
        conn = get_connection()
        print("연결 성공!")
        conn.close()
    except Exception as e:
        print("MySQL 연결 실패", e)
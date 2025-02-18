from connectDB import get_connection

# 테이블 생성 함수
def create_tables():
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            # user 테이블 생성
            cursor.execute("""
                           CREATE TABLE IF NOT EXISTS users (
                               id INT AUTO_INCREMENT PRIMARY KEY,
                               email VARCHAR(255) UNIQUE NOT NULL,
                               password VARCHAR(255) NOT NULL,
                               name VARCHAR(100) NOT NULL,
                               created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                           )
                           """)
            
            
            # products 테이블 생성 (수정된 버전)
            cursor.execute("""
                           CREATE TABLE IF NOT EXISTS products (
                               id INT AUTO_INCREMENT PRIMARY KEY,
                               category VARCHAR(255) NOT NULL,
                               brand VARCHAR(255) NOT NULL,
                               name VARCHAR(255) NOT NULL,
                               price DECIMAL(10,2) NOT NULL,
                               created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)
            
            connection.commit()
            print("테이블 생성 완료!")
    finally:
        connection.close()

if __name__ == "__main__":
    create_tables()
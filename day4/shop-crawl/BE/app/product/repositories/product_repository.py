import pymysql
from connectDB import get_connection

class ProductRepository:
    @staticmethod
    def create_product(category, brand, name, price):
        """중복 확인 후 상품 추가"""
        connection = get_connection()
        try:
            with connection.cursor() as cursor:
                # 동일한 상품이 있는지 확인
                cursor.execute("SELECT id FROM products WHERE name = %s", (name,))
                existing_product = cursor.fetchone()

                if existing_product:
                    print(f"중복 상품 존재, 저장하지 않음: {name}")
                    return False

                # 중복이 없으면 상품 저장
                sql = "INSERT INTO products (category, brand, name, price) VALUES (%s, %s, %s, %s)"
                cursor.execute(sql, (category, brand, name, price))
                connection.commit()
                return True
        except Exception as e:
            print(f"DB 저장 오류: {e}")
            return False
        finally:
            connection.close()

    @staticmethod
    def get_products():
        """모든 상품 조회"""
        connection = get_connection()
        try:
            with connection.cursor(pymysql.cursors.DictCursor) as cursor:
                cursor.execute("SELECT * FROM products ORDER BY created_at DESC")
                return cursor.fetchall()
        except Exception as e:
            print(f"DB 조회 오류: {e}")
            return []
        finally:
            connection.close()

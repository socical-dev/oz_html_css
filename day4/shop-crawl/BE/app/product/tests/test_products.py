import unittest
from repositories.product_repository import ProductRepository

class TestProductRepository(unittest.TestCase):
    def test_create_product(self):
        """상품 생성 테스트"""
        result = ProductRepository.create_product("전자제품", "애플", "아이폰 15", 1450000)
        self.assertTrue(result)

    def test_get_products(self):
        """상품 목록 조회 테스트"""
        products = ProductRepository.get_products()
        self.assertGreater(len(products), 0)

if __name__ == "__main__":
    unittest.main()

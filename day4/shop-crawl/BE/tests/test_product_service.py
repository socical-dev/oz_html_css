import unittest
from app.services.product_service import ProductService

class TestProductService(unittest.TestCase):
    def test_add_product(self):
        """상품 추가 테스트"""
        result = ProductService.add_product("가전", "LG", "LG OLEF TV", 2500000)
        self.assertTrue(result)
        
    def test_get_all_products(self):
        """상품 목록 조회 테스트"""
        products = ProductService.get_all_products()
        self.assertGreater(len(products), 0)
        

if __name__ == "__main__":
    unittest.main()
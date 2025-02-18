from app.repositories.product_repository import ProductRepository

class ProductService:
    @staticmethod
    def add_product(category, brand, name, price):
        """상품 추가 (중복 검사 포함)"""
        return ProductRepository.create_product(category, brand, name, price)
    
    @staticmethod
    def get_all_products():
        """모든 상품 조회"""
        return ProductRepository.get_products()
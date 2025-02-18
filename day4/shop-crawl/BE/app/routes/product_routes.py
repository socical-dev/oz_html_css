from flask import Blueprint, request, jsonify
from flask_cors import CORS
from app.services.product_service import ProductService

product_routes = Blueprint("product_routes", __name__)
CORS(product_routes)  # ✅ Blueprint에도 CORS 적용 (OPTIONS 필요 없음)

@product_routes.route("/products", methods=["POST"])
def add_product():
    """상품 추가 API"""
    data = request.get_json()
    category = data.get("category")
    brand = data.get("brand")
    name = data.get("name")
    price = data.get("price")

    if not category or not brand or not name or not price:
        return jsonify({"error": "모든 필드를 입력해야 합니다."}), 400

    result = ProductService.add_product(category, brand, name, price)
    if result:
        return jsonify({"message": "상품 추가 성공!"}), 201
    return jsonify({"error": "상품 추가 실패"}), 500

@product_routes.route("/products", methods=["GET"])
def get_products():
    """상품 목록 조회 API"""
    products = ProductService.get_all_products()
    return jsonify([
        {
            "id": p["id"],
            "category": p["category"],
            "brand": p["brand"],
            "name": p["name"],
            "price": p["price"],
            "created_at": p["created_at"]
        } for p in products
    ])

from flask import Blueprint, jsonify
from app.crawler.crawler import scrape_product

crawler_routes = Blueprint("crawler_routes", __name__)

@crawler_routes.route("/crawl", methods=["POST"])
def start_crawling():
    """크롤링 실행 API"""
    try:
        scrape_product()
        return jsonify({"message": "크롤링 완료!"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
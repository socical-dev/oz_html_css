### [[KREAM 상품 미니 프로젝트]](https://github.com/socical-dev/oz_html_css_js/tree/8c0920f24d84f363f0fc19d7ad8c988380f34cbe/day4/shop-crawl)

# 🛍️ KREAM 상품 크롤러 API

KREAM 사이트에서 최신 상품 데이터를 크롤링하여 MySQL 데이터베이스에 저장하고,  
저장된 상품을 Flask API를 통해 조회할 수 있는 서비스입니다.

---

## 🔥 주요 기능
✔️ **KREAM에서 상품 자동 크롤링 (Selenium 사용)**  
✔️ **Flask API를 통해 상품 데이터 조회 가능**  
✔️ **MySQL 데이터베이스 연동 (중복 상품 방지 로직 포함)**  

---

## 📌 폴더별 역할 정리

✅ 모델 (Model) → models/

app/product/models/product.py

app/user/models/user.py

=> DB 스키마를 정의

✅ 서비스 (Service) → services/

app/product/services/product_service.py

app/user/services/user_service.py

=> 비즈니스 로직을 담당

✅ 라우트 (Routes) → routes/

app/product/routes/product_routes.py

app/user/routes/user_routes.py

=> HTTP 요청을 처리하는 부분으로, Flask에서 Controller 역할

✅ 데이터 접근 계층 (Repository) → repositories/

app/product/repositories/product_repository.py

app/user/repositories/user_repository.py

=> DB 접근을 캡슐화한 계층

---

## 📌 프로젝트 구조
<div class="tree">
            <ul>
                <li>BE
                    <ul>
                        <li>app
                            <ul>
                                <li class="file">connectDB.py 🛠️ DB 연결 설정</li>
                                <li>crawler
                                    <ul>
                                        <li>routes
                                            <ul>
                                                <li class="file">crawler_routes.py 🚀 크롤링 API 라우트</li>
                                            </ul>
                                        </li>
                                        <li>services
                                            <ul>
                                                <li class="file">crawler.py 🕷️ KREAM 크롤러 (Selenium)</li>
                                            </ul>
                                        </li>
                                    </ul>
                                </li>
                                <li class="file">init_db.py 🗄️ 데이터베이스 초기화</li>
                                <li class="file">main.py 🌐 Flask 앱 실행</li>
                                <li>product
                                    <ul>
                                        <li>models
                                            <ul>
                                                <li class="file">product.py 📦 상품 모델 정의</li>
                                            </ul>
                                        </li>
                                        <li>repositories
                                            <ul>
                                                <li class="file">product_repository.py 🛢️ 상품 DB 연동</li>
                                            </ul>
                                        </li>
                                        <li>routes
                                            <ul>
                                                <li class="file">product_routes.py 🌐 상품 API 라우트</li>
                                            </ul>
                                        </li>
                                        <li>services
                                            <ul>
                                                <li class="file">product_service.py ⚙️ 상품 서비스 로직</li>
                                            </ul>
                                        </li>
                                        <li>tests
                                            <ul>
                                                <li class="file">test_product_service.py ✅ 상품 서비스 테스트</li>
                                                <li class="file">test_products.py ✅ 상품 API 테스트</li>
                                            </ul>
                                        </li>
                                    </ul>
                                </li>
                                <li>user
                                    <ul>
                                        <li>models
                                            <ul>
                                                <li class="file">user.py 👤 사용자 모델 정의</li>
                                            </ul>
                                        </li>
                                        <li>repositories
                                            <ul>
                                                <li class="file">user_repository.py 🗄️ 사용자 DB 연동</li>
                                            </ul>
                                        </li>
                                        <li>routes
                                            <ul>
                                                <li class="file">user_routes.py 🔗 사용자 API 라우트</li>
                                            </ul>
                                        </li>
                                        <li>services
                                            <ul>
                                                <li class="file">user_service.py 🔧 사용자 서비스 로직</li>
                                            </ul>
                                        </li>
                                        <li>tests
                                            <ul>
                                                <li class="file">test_user_service.py ✅ 사용자 서비스 테스트</li>
                                                <li class="file">test_users.py ✅ 사용자 API 테스트</li>
                                            </ul>
                                        </li>
                                    </ul>
                                </li>
                            </ul>
                        </li>
                    </ul>
                </li>
            </ul>
        </div>

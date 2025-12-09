# 🐍 Python REST API Proje Şablonu

Bu şablonu kullanarak Python Flask/FastAPI ile profesyonel bir REST API oluşturabilirsiniz.

## 📋 Talep Şablonu

Issue'da şu formatı kullanın:

```
Python ile REST API oluştur.

Framework: Flask / FastAPI (seçiminizi belirtin)
Veritabanı: SQLite / PostgreSQL / MongoDB

Özellikler:
- Kullanıcı kimlik doğrulama (JWT)
- CRUD operasyonları (Create, Read, Update, Delete)
- Input validasyonu
- Hata yönetimi (error handling)
- API dokümantasyonu (Swagger/OpenAPI)
- Rate limiting
- CORS desteği

Endpoints:
- POST /api/auth/register (Kayıt)
- POST /api/auth/login (Giriş)
- GET /api/users (Kullanıcı listesi)
- GET /api/users/{id} (Kullanıcı detay)
- PUT /api/users/{id} (Güncelleme)
- DELETE /api/users/{id} (Silme)

Klasör yapısı:
- src/api/routes/ (endpoint tanımları)
- src/api/models/ (veritabanı modelleri)
- src/api/schemas/ (validasyon şemaları)
- src/api/middleware/ (auth, error handling)
- src/config/ (yapılandırma)
- src/utils/ (yardımcı fonksiyonlar)
- tests/ (unit ve integration testler)
- docs/ (API dokümantasyonu)

Ek dosyalar:
- requirements.txt (bağımlılıklar)
- .env.example (ortam değişkenleri)
- Dockerfile
- docker-compose.yml
- README.md (kurulum ve kullanım)
- .gitignore
```

## 🎯 Beklenen Çıktı

Bot size şu dosya yapısını oluşturacaktır:

```
proje/
├── src/
│   ├── __init__.py
│   ├── main.py
│   ├── api/
│   │   ├── __init__.py
│   │   ├── routes/
│   │   │   ├── __init__.py
│   │   │   ├── auth.py
│   │   │   └── users.py
│   │   ├── models/
│   │   │   ├── __init__.py
│   │   │   └── user.py
│   │   ├── schemas/
│   │   │   ├── __init__.py
│   │   │   └── user_schema.py
│   │   └── middleware/
│   │       ├── __init__.py
│   │       ├── auth_middleware.py
│   │       └── error_handler.py
│   ├── config/
│   │   ├── __init__.py
│   │   └── settings.py
│   └── utils/
│       ├── __init__.py
│       └── helpers.py
├── tests/
│   ├── __init__.py
│   ├── test_auth.py
│   └── test_users.py
├── docs/
│   └── API.md
├── requirements.txt
├── .env.example
├── Dockerfile
├── docker-compose.yml
├── README.md
└── .gitignore
```

## 💡 Özelleştirme Örnekleri

### Özel Endpoint Ekleme
```
Ayrıca şu endpoint'leri de ekle:
- GET /api/products (Ürün listesi)
- POST /api/products (Ürün oluşturma)
- GET /api/orders (Sipariş listesi)
```

### Gelişmiş Özellikler
```
Şu özellikleri de ekle:
- Email doğrulama (SMTP)
- Redis cache
- Celery ile background tasks
- WebSocket desteği
- File upload
- Pagination
```

### Test Gereksinimleri
```
Testler için:
- Pytest kullan
- %90+ code coverage
- Mock kullanarak dış servisleri taklit et
- Fixture'lar ile test data
```

## 📚 Ek Kaynaklar

- [Flask Dokümantasyonu](https://flask.palletsprojects.com/)
- [FastAPI Dokümantasyonu](https://fastapi.tiangolo.com/)
- [SQLAlchemy ORM](https://www.sqlalchemy.org/)
- [PyJWT](https://pyjwt.readthedocs.io/)

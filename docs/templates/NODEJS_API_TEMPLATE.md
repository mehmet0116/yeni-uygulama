# 🟢 Node.js Backend API Proje Şablonu

Bu şablonu kullanarak Node.js ile profesyonel bir backend API oluşturabilirsiniz.

## 📋 Talep Şablonu

Issue'da şu formatı kullanın:

```
Node.js ile REST API oluştur.

Framework: Express / NestJS / Fastify (seçiminizi belirtin)
Veritabanı: MongoDB / PostgreSQL / MySQL
ORM/ODM: Mongoose / Sequelize / TypeORM / Prisma

Özellikler:
- RESTful API yapısı
- JWT Authentication
- Input validation (Joi / express-validator)
- Error handling middleware
- Logging (Winston / Morgan)
- API documentation (Swagger)
- Rate limiting
- CORS configuration
- Environment variables (.env)
- Security headers (Helmet)

Modüller:
- User Management
- Authentication (register, login, logout, refresh token)
- Authorization (role-based access control)
- [Diğer modüller...]

Klasör yapısı:
- src/controllers/ (business logic)
- src/routes/ (endpoint definitions)
- src/models/ (database models)
- src/middleware/ (custom middleware)
- src/services/ (business services)
- src/utils/ (helper functions)
- src/config/ (configuration files)
- src/validators/ (input validation)
- tests/ (unit & integration tests)

Ek:
- package.json
- .env.example
- .eslintrc.js
- .prettierrc
- Dockerfile
- docker-compose.yml (app + database)
- README.md
- .gitignore
```

## 🎯 Beklenen Çıktı

```
nodejs-api/
├── src/
│   ├── controllers/
│   │   ├── authController.js
│   │   └── userController.js
│   ├── routes/
│   │   ├── index.js
│   │   ├── authRoutes.js
│   │   └── userRoutes.js
│   ├── models/
│   │   └── User.js
│   ├── middleware/
│   │   ├── authMiddleware.js
│   │   ├── errorHandler.js
│   │   └── rateLimiter.js
│   ├── services/
│   │   ├── authService.js
│   │   └── userService.js
│   ├── utils/
│   │   ├── jwt.js
│   │   └── helpers.js
│   ├── config/
│   │   ├── database.js
│   │   └── config.js
│   ├── validators/
│   │   └── userValidator.js
│   ├── app.js
│   └── server.js
├── tests/
│   ├── unit/
│   │   └── user.test.js
│   └── integration/
│       └── auth.test.js
├── .env.example
├── .eslintrc.js
├── .prettierrc
├── package.json
├── Dockerfile
├── docker-compose.yml
├── README.md
└── .gitignore
```

## 💡 API Türü Örnekleri

### 1. E-Ticaret API
```
Node.js Express ile e-ticaret backend API yap.

Modüller:
- Product Management (CRUD)
- Category Management
- Shopping Cart
- Order Management
- Payment Integration (Stripe)
- Inventory Management
- Review & Rating System

Features:
- Image upload (Multer + Cloudinary)
- Email notifications (Nodemailer)
- Search & filtering
- Pagination
- Admin dashboard endpoints
```

### 2. Sosyal Medya API
```
Node.js ile sosyal medya backend oluştur.

Özellikler:
- User profiles
- Post CRUD (text, image, video)
- Like & comment system
- Follow/unfollow
- News feed algorithm
- Real-time notifications (Socket.io)
- Direct messaging
- Story feature (24h expiry)

Database: MongoDB (Mongoose)
File storage: AWS S3 / Cloudinary
```

### 3. Blog CMS API
```
Node.js ile blog yönetim sistemi API'si yap.

Endpoints:
- Post management (CRUD, draft, publish)
- Category & tag system
- Comment moderation
- Media library
- SEO meta tags
- Multi-author support
- Analytics tracking

Features:
- Markdown editor support
- Scheduled publishing
- RSS feed
- Sitemap generation
```

### 4. Task Management API
```
Node.js ile görev yönetim API'si oluştur.

Özellikler:
- Project management
- Task CRUD (title, description, priority, due date)
- Team management
- Task assignment
- File attachments
- Activity log
- Time tracking
- Notifications

Database: PostgreSQL + Redis (caching)
```

## 🔒 Güvenlik Özellikleri

```
Güvenlik için:
- Helmet.js (security headers)
- Express rate limit (DDoS protection)
- XSS protection
- SQL injection prevention
- CSRF protection
- Password hashing (bcrypt)
- JWT refresh tokens
- Input sanitization
- HTTPS enforcement
```

## 🧪 Test Gereksinimleri

```
Testing:
- Mocha + Chai / Jest
- Supertest (HTTP testing)
- MongoDB Memory Server (DB mocking)
- %85+ code coverage
- Unit tests (services, utilities)
- Integration tests (API endpoints)
- Load testing (Artillery)
```

## 📊 Monitoring & Logging

```
Ekle:
- Winston logger (file & console)
- Morgan (HTTP logging)
- PM2 (process management)
- Health check endpoint (/health)
- Performance monitoring
- Error tracking (Sentry)
```

## 🐳 DevOps

```
DevOps için:
- Dockerfile (multi-stage build)
- docker-compose.yml (app + db + redis)
- .dockerignore
- GitHub Actions CI/CD
- Kubernetes deployment files (optional)
```

## 📚 Dokümantasyon

```
Dokümantasyon:
- Swagger/OpenAPI spec
- Postman collection
- API usage examples
- Environment setup guide
- Deployment guide
```

# 🌐 Full-Stack Web Uygulaması Şablonu

Bu şablonu kullanarak frontend ve backend içeren tam özellikli web uygulaması oluşturabilirsiniz.

## 📋 Talep Şablonu

Issue'da şu formatı kullanın:

```
Full-stack web uygulaması oluştur.

Proje: [E-Ticaret / Blog / Dashboard / Sosyal Medya / vb.]

BACKEND:
Framework: Express.js / NestJS / Flask / Django
Database: MongoDB / PostgreSQL / MySQL
Authentication: JWT / Session / OAuth2

Backend Özellikler:
- RESTful API
- User authentication
- CRUD operations
- File upload
- Email notifications
- API documentation (Swagger)

Backend Klasör Yapısı:
backend/
├── src/
│   ├── controllers/
│   ├── routes/
│   ├── models/
│   ├── middleware/
│   ├── services/
│   └── config/
├── tests/
├── .env.example
└── README.md

FRONTEND:
Framework: React / Vue / Angular
State Management: Redux / Context API / Vuex
Styling: Tailwind / Material-UI / Bootstrap
Build Tool: Vite / Create React App / Next.js

Frontend Özellikler:
- Responsive design
- Authentication flow
- Data fetching & caching
- Form validation
- Error handling
- Loading states
- Toast notifications

Frontend Klasör Yapısı:
frontend/
├── src/
│   ├── components/
│   ├── pages/
│   ├── hooks/
│   ├── services/
│   ├── store/
│   └── utils/
├── public/
├── tests/
└── README.md

SHARED:
- Docker compose (backend + frontend + database)
- .gitignore
- Project README (root)
- API integration dokumentasyonu

DATABASE:
- Schema/Model tanımları
- Seed data (örnek veriler)
- Migration files
```

## 🎯 Proje Türü Örnekleri

### 1. E-Ticaret Platformu

```
Full-stack e-ticaret uygulaması yap.

BACKEND (Node.js + Express + MongoDB):
Modüller:
- Auth (register, login, JWT)
- Products (CRUD, image upload)
- Categories
- Shopping Cart
- Orders
- Reviews & Ratings
- Admin panel endpoints

FRONTEND (React + Redux + Tailwind):
Sayfalar:
- Home (ürün listesi, kategoriler)
- Product Detail (resimler, açıklama, yorumlar)
- Cart (sepet yönetimi)
- Checkout (adres, ödeme)
- User Profile
- Admin Dashboard

Özellikler:
- Ürün filtreleme & arama
- Sepete ekleme/çıkarma
- Sipariş takibi
- Yorum yapma
- Admin: ürün yönetimi

DOCKER:
- Backend container
- Frontend container
- MongoDB container
- Nginx reverse proxy

API Entegrasyonu:
- Stripe (ödeme)
- Cloudinary (resim upload)
```

### 2. Blog Platformu

```
Full-stack blog uygulaması oluştur.

BACKEND (Python Django + PostgreSQL):
Features:
- User authentication
- Post CRUD (create, read, update, delete)
- Comment system
- Category & tags
- Media library
- Rich text editor support
- Admin panel (Django admin)

API Endpoints:
- /api/posts/ (list, create)
- /api/posts/{id}/ (detail, update, delete)
- /api/comments/
- /api/categories/
- /api/tags/
- /api/users/profile/

FRONTEND (Vue 3 + Vuex + Vuetify):
Pages:
- Home (post listesi, grid layout)
- Post Detail (markdown render, comments)
- Create/Edit Post (rich editor)
- User Profile
- Category/Tag filter pages

Features:
- Markdown support
- Syntax highlighting (code blocks)
- Social share buttons
- Reading time estimation
- Related posts

DEPLOYMENT:
- Docker compose
- Environment variables
- Static files serving
```

### 3. Real-Time Chat Application

```
Full-stack real-time chat uygulaması yap.

BACKEND (Node.js + Express + Socket.io + Redis + MongoDB):
Features:
- JWT authentication
- User profiles
- Direct messaging
- Group chats
- Real-time messaging (Socket.io)
- Message history (MongoDB)
- Online status (Redis)
- Typing indicators
- Message read receipts

FRONTEND (React + Socket.io-client + Material-UI):
Components:
- Chat list (conversations)
- Message thread
- User search
- Group creation
- User profile modal
- Settings panel

Features:
- Real-time message updates
- Message notifications
- Emoji support
- File/image sharing
- Voice messages
- Message search

INFRASTRUCTURE:
- Docker compose (app + MongoDB + Redis)
- WebSocket configuration
- CORS setup
```

### 4. Task Management System

```
Full-stack task/project yönetim uygulaması yap.

BACKEND (NestJS + TypeORM + PostgreSQL):
Modules:
- Authentication (JWT)
- Users & Teams
- Projects
- Tasks (title, description, priority, due date, status)
- Comments
- File attachments
- Activity log
- Notifications

FRONTEND (React + TypeScript + Redux Toolkit + Ant Design):
Pages:
- Dashboard (overview, statistics)
- Projects list & detail
- Kanban board (drag & drop)
- Task detail modal
- Team management
- Calendar view
- Reports & analytics

Features:
- Drag & drop tasks (react-beautiful-dnd)
- Gantt chart (task timeline)
- Real-time updates (optional: Socket.io)
- File upload
- User assignments
- Activity tracking

TESTING:
- Backend: Jest + Supertest
- Frontend: Jest + React Testing Library
- E2E: Cypress

DEVOPS:
- Docker compose
- GitHub Actions CI/CD
- Environment configs
```

## 🏗️ Klasör Yapısı Örneği

```
fullstack-app/
├── backend/
│   ├── src/
│   │   ├── controllers/
│   │   ├── routes/
│   │   ├── models/
│   │   ├── middleware/
│   │   ├── services/
│   │   ├── config/
│   │   └── utils/
│   ├── tests/
│   ├── .env.example
│   ├── package.json
│   ├── Dockerfile
│   └── README.md
├── frontend/
│   ├── public/
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── hooks/
│   │   ├── services/
│   │   ├── store/
│   │   ├── utils/
│   │   ├── App.jsx
│   │   └── index.js
│   ├── tests/
│   ├── .env.example
│   ├── package.json
│   ├── Dockerfile
│   └── README.md
├── docker-compose.yml
├── .gitignore
└── README.md (root - setup instructions)
```

## 🔧 API Entegrasyonu

Frontend'in Backend'e bağlanması:

```
BACKEND (.env):
PORT=5000
DB_URL=mongodb://localhost:27017/myapp
JWT_SECRET=your_secret_key

FRONTEND (.env):
REACT_APP_API_URL=http://localhost:5000/api
```

## 🐳 Docker Setup

```
Şunları ekle:
- backend/Dockerfile (Node/Python image)
- frontend/Dockerfile (Node + Nginx)
- docker-compose.yml (orchestration)
- .dockerignore files

docker-compose.yml içinde:
- backend service
- frontend service  
- database service
- redis service (opsiyonel)
- network configuration
- volume mounts
```

## 📊 Database Schema

```
Database schema ekle:
- User (id, email, password, role, createdAt)
- [Diğer modeller...]

İlişkiler belirt:
- One-to-Many
- Many-to-Many
- Foreign keys
```

## 🧪 Testing

```
Backend tests:
- Unit tests (services, utilities)
- Integration tests (API endpoints)
- Authentication tests

Frontend tests:
- Component tests
- Page tests
- User interaction tests
- API mock'ları
```

## 📚 Dokümantasyon

```
README.md içinde:
- Proje açıklaması
- Tech stack
- Installation (backend + frontend)
- Environment variables
- Running with Docker
- API endpoints
- Features
- Screenshots (opsiyonel)
```

## 💡 İpuçları

1. **Aşamalı geliştirme**: Önce temel auth ve CRUD, sonra ileri özellikler
2. **API-first**: Backend API'yi önce oluştur, test et, sonra frontend
3. **Error handling**: Her iki tarafta da kapsamlı hata yönetimi
4. **Security**: Input validation, XSS protection, CSRF tokens
5. **Performance**: Caching, pagination, lazy loading

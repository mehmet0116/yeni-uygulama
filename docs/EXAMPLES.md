# 💼 Gerçek Kullanım Örnekleri

Bu dokümanda, kullanıcıların yazdığı gerçek istekleri ve botun oluşturduğu projeleri görebilirsiniz.

## 🐍 Örnek 1: Python CLI Aracı

### Kullanıcı İsteği:
```
Python ile dosya organizasyon aracı yap.

Özellikler:
- Belirtilen klasördeki dosyaları uzantılarına göre sınıflandır
- images/, documents/, videos/, audio/, others/ klasörlerine taşı
- Dry-run modu (sadece göster, taşıma)
- Progress bar göster
- Log dosyası oluştur

Kullanım:
python organizer.py --path /downloads --dry-run
python organizer.py --path /downloads --execute

src/organizer.py
tests/test_organizer.py
README.md
requirements.txt
```

### Bot Çıktısı:
```
✅ src/organizer.py oluşturuldu
✅ tests/test_organizer.py oluşturuldu
✅ README.md oluşturuldu
✅ requirements.txt oluşturuldu
```

**Oluşturulan Dosyalar:**
- `src/organizer.py` - Ana CLI aracı (argparse, tqdm, shutil)
- `tests/test_organizer.py` - Pytest testleri
- `README.md` - Kurulum ve kullanım talimatları
- `requirements.txt` - colorama, tqdm

---

## ⚛️ Örnek 2: React Todo App

### Kullanıcı İsteği:
```
React ile modern todo uygulaması yap.

Özellikler:
- Todo ekleme, silme, düzenleme
- Tamamlama checkbox
- Local storage ile kaydetme
- Filtreleme (Tümü, Aktif, Tamamlanan)
- Dark mode toggle
- Responsive design

Tailwind CSS kullan.
TypeScript ile yaz.
Component testleri ekle.
```

### Bot Çıktısı:
```
✅ src/App.tsx oluşturuldu
✅ src/components/TodoList.tsx oluşturuldu
✅ src/components/TodoItem.tsx oluşturuldu
✅ src/components/TodoForm.tsx oluşturuldu
✅ src/components/FilterButtons.tsx oluşturuldu
✅ src/hooks/useTodos.ts oluşturuldu
✅ src/hooks/useDarkMode.ts oluşturuldu
✅ src/types/todo.ts oluşturuldu
✅ src/__tests__/TodoList.test.tsx oluşturuldu
✅ tailwind.config.js güncellendi
✅ package.json güncellendi
✅ README.md oluşturuldu
```

---

## 🟢 Örnek 3: Node.js Express API

### Kullanıcı İsteği:
```
Node.js Express ile basit blog API'si yap.

Endpoints:
- POST /api/auth/register
- POST /api/auth/login
- GET /api/posts (tüm postlar)
- GET /api/posts/:id (tek post)
- POST /api/posts (yeni post - auth gerekli)
- PUT /api/posts/:id (güncelle - auth gerekli)
- DELETE /api/posts/:id (sil - auth gerekli)

MongoDB + Mongoose kullan.
JWT authentication.
Input validation (express-validator).
Error handling middleware.
.env.example ekle.
```

### Bot Çıktısı:
```
✅ src/app.js oluşturuldu
✅ src/server.js oluşturuldu
✅ src/config/database.js oluşturuldu
✅ src/models/User.js oluşturuldu
✅ src/models/Post.js oluşturuldu
✅ src/routes/authRoutes.js oluşturuldu
✅ src/routes/postRoutes.js oluşturuldu
✅ src/controllers/authController.js oluşturuldu
✅ src/controllers/postController.js oluşturuldu
✅ src/middleware/authMiddleware.js oluşturuldu
✅ src/middleware/errorHandler.js oluşturuldu
✅ src/validators/authValidator.js oluşturuldu
✅ src/validators/postValidator.js oluşturuldu
✅ tests/auth.test.js oluşturuldu
✅ tests/posts.test.js oluşturuldu
✅ .env.example oluşturuldu
✅ package.json oluşturuldu
✅ README.md oluşturuldu
```

---

## 🎨 Örnek 4: Static Website

### Kullanıcı İsteği:
```
HTML/CSS/JavaScript ile portfolyo web sitesi yap.

Sayfalar:
- index.html (Ana sayfa - Hero section, about, projects, contact)
- Tek sayfa scroll design

Özellikler:
- Smooth scrolling
- Responsive (mobil uyumlu)
- Modern ve minimal tasarım
- Contact form (validation)
- Social media links
- Dark blue tema

Klasör:
- css/style.css
- js/script.js
- images/ (placeholder'lar)
```

### Bot Çıktısı:
```
✅ index.html oluşturuldu
✅ css/style.css oluşturuldu
✅ js/script.js oluşturuldu
✅ images/.gitkeep oluşturuldu
✅ README.md oluşturuldu
```

---

## 🤖 Örnek 5: Python Data Analysis

### Kullanıcı İsteği:
```
Python ile veri analiz pipeline'ı yap.

Özellikler:
- CSV okuma (pandas)
- Veri temizleme (null values, duplicates)
- İstatistiksel analiz (mean, median, std)
- Görselleştirmeler (histogram, scatter, box plot)
- HTML rapor oluşturma

Klasör yapısı:
- src/data_loader.py
- src/data_cleaner.py
- src/analyzer.py
- src/visualizer.py
- src/report_generator.py
- notebooks/example_analysis.ipynb
- tests/
- requirements.txt
```

### Bot Çıktısı:
```
✅ src/data_loader.py oluşturuldu
✅ src/data_cleaner.py oluşturuldu
✅ src/analyzer.py oluşturuldu
✅ src/visualizer.py oluşturuldu
✅ src/report_generator.py oluşturuldu
✅ notebooks/example_analysis.ipynb oluşturuldu
✅ tests/test_data_loader.py oluşturuldu
✅ tests/test_analyzer.py oluşturuldu
✅ requirements.txt oluşturuldu
✅ README.md oluşturuldu
```

---

## 🔄 Örnek 6: Güncelleme İsteği

### İlk İstek:
```
Python Flask ile basit API yap.
- GET /api/hello endpoint
- JSON response döndürsün
```

### Bot Çıktısı:
```
✅ src/app.py oluşturuldu
✅ README.md oluşturuldu
```

### Güncelleme İsteği (Issue Yorumu):
```
src/app.py dosyasına şunları ekle:
- POST /api/users endpoint (user ekleme)
- GET /api/users endpoint (user listesi)
- SQLite database kullan
- Input validation ekle
```

### Bot Güncelleme Çıktısı:
```
✅ src/app.py güncellendi
✅ src/database.py oluşturuldu
✅ src/models.py oluşturuldu
✅ requirements.txt güncellendi
```

---

## 🗑️ Örnek 7: Dosya Silme

### Kullanıcı İsteği:
```
sil: src/old_app.py
sil: tests/old_test.py
sil: deprecated/
```

### Bot Çıktısı:
```
🗑️ src/old_app.py silindi
🗑️ tests/old_test.py silindi
⚠️ deprecated/: Directory silme desteklenmiyor (sadece dosyalar)
```

---

## 🎯 Örnek 8: Full-Stack Proje

### Kullanıcı İsteği:
```
Full-stack e-ticaret başlangıç projesi oluştur.

Backend (Node.js + Express + MongoDB):
- Auth (register, login)
- Products CRUD
- Basic struktur

Frontend (React):
- Login/Register pages
- Product list
- Product detail
- Basit styling

Docker compose ile birlikte çalıştır.
```

### Bot Çıktısı:
```
Backend:
✅ backend/src/app.js oluşturuldu
✅ backend/src/routes/authRoutes.js oluşturuldu
✅ backend/src/routes/productRoutes.js oluşturuldu
✅ backend/src/controllers/authController.js oluşturuldu
✅ backend/src/controllers/productController.js oluşturuldu
✅ backend/src/models/User.js oluşturuldu
✅ backend/src/models/Product.js oluşturuldu
✅ backend/.env.example oluşturuldu
✅ backend/package.json oluşturuldu
✅ backend/Dockerfile oluşturuldu

Frontend:
✅ frontend/src/App.jsx oluşturuldu
✅ frontend/src/pages/Login.jsx oluşturuldu
✅ frontend/src/pages/Register.jsx oluşturuldu
✅ frontend/src/pages/ProductList.jsx oluşturuldu
✅ frontend/src/pages/ProductDetail.jsx oluşturuldu
✅ frontend/src/services/api.js oluşturuldu
✅ frontend/package.json oluşturuldu
✅ frontend/Dockerfile oluşturuldu

Root:
✅ docker-compose.yml oluşturuldu
✅ README.md oluşturuldu
✅ .gitignore oluşturuldu

📊 Toplam: 24 dosya başarıyla oluşturuldu
```

---

## 💡 Başarı İpuçları

### ✅ İyi Talep Özellikleri:
1. **Spesifik**: Hangi özellikleri istediğiniz açık
2. **Detaylı**: Klasör yapısı, dosya isimleri belirtilmiş
3. **Teknoloji**: Framework ve kütüphaneler netleştirilmiş
4. **Yapısal**: Modüler ve organize istek

### ❌ Kaçınılması Gerekenler:
1. "Güzel bir şey yap" gibi belirsiz istekler
2. Teknoloji belirtmeden istek
3. Çok fazla özellik tek seferde (aşamalı ilerleyin)
4. Klasör yapısı olmadan karmaşık projeler

---

## 🎓 Öğrenme Yolu

1. **Başlangıç**: Basit projelerle başlayın (hesap makinesi, todo)
2. **Orta**: API'ler ve React uygulamaları yapın
3. **İleri**: Full-stack projeler ve mikroservisler
4. **Uzman**: Karmaşık mimariler ve DevOps entegrasyonu

---

**💡 Kendi projenizi oluşturmaya hazır mısınız? Hemen bir Issue açın!**

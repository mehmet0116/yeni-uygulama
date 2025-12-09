# 📚 Detaylı Kullanım Kılavuzu

Bu kılavuz, DeepSeek ULTRA Enterprise Architect botunu en etkili şekilde kullanmanız için hazırlanmıştır.

## 🎯 Temel Kullanım Akışı

### Adım 1: Issue Oluşturma
1. GitHub repo sayfasında **Issues** sekmesine gidin
2. **New Issue** butonuna tıklayın
3. Başlık ve açıklama yazın
4. **Submit new issue** ile gönderin

### Adım 2: Talebinizi Formüle Etme

#### ✅ İyi Talep Örnekleri:

**Örnek 1: Python Web API**
```
Python Flask ile REST API oluştur.

Özellikler:
- Kullanıcı kayıt ve giriş (JWT authentication)
- SQLite veritabanı
- CRUD operasyonları
- Hata yönetimi
- API dokümantasyonu

Klasör yapısı:
- src/api/ (route'lar)
- src/models/ (veritabanı modelleri)
- src/utils/ (yardımcı fonksiyonlar)
- tests/ (unit testler)
- docs/ (API dokümantasyonu)
```

**Örnek 2: React Dashboard**
```
React ile admin dashboard oluştur.

Gereksinimler:
- TypeScript kullan
- Material-UI komponenti
- Grafik gösterimi (Chart.js)
- Responsive tasarım
- Dark/Light tema
- Router ile sayfa yönetimi

Sayfalar:
- Login
- Dashboard (istatistikler)
- Kullanıcı listesi
- Ayarlar

Testler ve Storybook da ekle.
```

**Örnek 3: Node.js Mikroservis**
```
Node.js ile mikroservis mimarisi kur.

Servisler:
1. Auth Service (kimlik doğrulama)
2. User Service (kullanıcı yönetimi)
3. Product Service (ürün kataloğu)

Teknolojiler:
- Express.js
- MongoDB (Mongoose)
- Redis (cache)
- JWT tokens
- Docker ve docker-compose
- .env.example ile yapılandırma

Her servis için:
- Ayrı klasör
- API endpoint'leri
- Test dosyaları
- README
```

**Örnek 4: Machine Learning Projesi**
```
Python ile makine öğrenimi modeli eğitim pipeline'ı oluştur.

İhtiyaçlar:
- Veri yükleme ve ön işleme
- Model eğitimi (scikit-learn)
- Model değerlendirme
- Sonuçların görselleştirilmesi
- Jupyter notebook örnekleri

Dosya yapısı:
- src/data_processing.py
- src/model_training.py
- src/evaluation.py
- notebooks/example.ipynb
- requirements.txt
- README.md (kullanım talimatları)
```

#### ❌ Kötü Talep Örnekleri:

```
❌ "Bir şey yap"
✅ "Python ile hesap makinesi yap, GUI olsun"

❌ "Web sitesi"
✅ "React ile blog sitesi, markdown desteği, yorum sistemi"

❌ "API"
✅ "Node.js Express ile e-ticaret API, ürün, sepet ve sipariş yönetimi"
```

## 🔄 Güncelleme ve Değişiklik İsteme

### Issue Yorumları ile Güncelleme

Oluşturulan dosyalarda değişiklik yapmak için issue'ya **yorum ekleyin**:

**Örnek Güncelleme Talepleri:**

```
src/app.py dosyasına logging özelliği ekle.
Winston logger kullan, info, error ve debug seviyeleri olsun.
```

```
API'ye rate limiting ekle.
Express-rate-limit kullan, dakikada 100 istek limiti.
```

```
Testlere yeni senaryolar ekle:
- Edge case testleri
- Integration testler
- Mock data kullan
```

### Dosya Silme

Dosya silmek için özel format kullanın:

```
sil: src/old_file.py
sil: tests/deprecated_test.js
sil: configs/old_config.yaml
```

⚠️ **Dikkat**: Korumalı dosyalar silinemez (README.md, .github/workflows/deepseek.yml, vb.)

## 🏗️ Proje Türlerine Göre Örnekler

### 1. Web Uygulaması (Full-Stack)

```
Full-stack blog uygulaması oluştur.

Backend (Node.js + Express):
- REST API
- MongoDB veritabanı
- JWT authentication
- Post CRUD, yorum sistemi
- Resim upload (multer)

Frontend (React):
- Ana sayfa (post listesi)
- Post detay sayfası
- Yönetim paneli
- Responsive design
- Axios ile API entegrasyonu

Ek:
- Docker compose
- .env.example
- API dokümantasyonu
- README (kurulum ve çalıştırma)
```

### 2. CLI Uygulaması

```
Python CLI aracı yap.

Özellikler:
- Komut satırı argümanları (argparse)
- Renkli çıktı (colorama)
- Progress bar (tqdm)
- Config dosyası (YAML)
- Logging

Komutlar:
- init (proje başlatma)
- process (veri işleme)
- report (rapor oluşturma)

Tests ve setup.py da ekle.
```

### 3. Veri Analiz Projesi

```
Veri analizi pipeline'ı oluştur.

Araçlar:
- Pandas (veri işleme)
- NumPy (matematiksel işlemler)
- Matplotlib + Seaborn (görselleştirme)
- Jupyter notebooks

İşlevler:
- CSV/Excel okuma
- Veri temizleme
- İstatistiksel analiz
- Görselleştirmeler
- HTML rapor oluşturma

Klasörler:
- data/raw (ham veri)
- data/processed (işlenmiş)
- notebooks/ (analizler)
- src/ (yardımcı fonksiyonlar)
- reports/ (HTML raporlar)
```

### 4. DevOps Otomasyon

```
DevOps otomasyon scriptleri yaz.

Bash ve Python:
- Sunucu health check
- Otomatik backup
- Log rotasyonu
- Deployment scripti
- Monitoring (CPU, RAM, disk)

Docker:
- Multi-stage Dockerfile
- Docker compose (app, db, redis)
- .dockerignore

CI/CD:
- GitHub Actions workflow
- Test, build, deploy aşamaları
```

## 💡 En İyi Pratikler

### 1. Açık ve Spesifik Olun
```
❌ "Güzel bir uygulama yap"
✅ "React ile hava durumu uygulaması, OpenWeather API kullan, 5 günlük tahmin göster"
```

### 2. Teknoloji Stack Belirtin
```
✅ "Python Django, PostgreSQL, Redis cache"
✅ "Vue.js 3, Composition API, Vuex"
✅ "Go fiber framework, GORM, PostgreSQL"
```

### 3. Klasör Yapısını Açıklayın
```
✅ "src/components/ için:
    - Button.jsx
    - Card.jsx
    - Navbar.jsx
   Her biri için .test.jsx dosyası da ekle"
```

### 4. Testleri Unutmayın
```
✅ "Unit testler (Jest)
    Integration testler (Supertest)
    En az %80 coverage"
```

### 5. Dokümantasyon İsteyin
```
✅ "README.md'de:
    - Kurulum adımları
    - Kullanım örnekleri
    - API endpoint listesi
    - Katkıda bulunma rehberi"
```

## 🔍 Sorun Giderme

### Bot Yanıt Vermiyorsa
1. API key doğru mu kontrol edin (repo secrets)
2. Workflow dosyası aktif mi kontrol edin
3. Issue'yu bot oluşturmadıysa (github-actions[bot] değil)

### Dosyalar Oluşturulmuyorsa
1. Bot yanıtındaki raporu kontrol edin
2. Dosya yolu geçerli mi kontrol edin (.. veya / içermemeli)
3. GitHub permissions kontrol edin

### Yanlış Kod Üretildiyse
1. Issue yorumuna düzeltme isteği yazın
2. Daha detaylı açıklama yapın
3. Örnek kod parçası verin

## 📞 Destek ve İletişim

- **Hata Bildirimi**: Yeni issue açın, "BUG" etiketi ekleyin
- **Özellik İsteği**: Issue açın, detayları açıklayın
- **Soru**: Issue'da "@mehmet0116" mention edin

---

## 🎓 Öğrenme Kaynakları

Bot şu yapıları en iyi şekilde destekler:
- **Backend**: Python (Flask, Django), Node.js (Express, NestJS), Go (Fiber, Gin)
- **Frontend**: React, Vue, Angular, Svelte
- **Mobil**: React Native, Flutter
- **DevOps**: Docker, Kubernetes, CI/CD
- **Data Science**: Python (Pandas, NumPy, Scikit-learn, TensorFlow)
- **Database**: SQL, NoSQL, Redis

---

*Son güncelleme: 2025-12-09*
*Version: 2.3*

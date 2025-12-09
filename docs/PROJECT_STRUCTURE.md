# 📁 Proje Yapısı

Bu dokuman, repository'nin organizasyonunu ve her bir dosyanın amacını açıklar.

## 🌳 Dosya Ağacı

```
yeni-uygulama/
├── 📄 README.md                          # Proje ana sayfası ve genel bakış
├── 📄 USAGE_GUIDE.md                     # Detaylı kullanım kılavuzu
├── 📄 CONTRIBUTING.md                    # Katkıda bulunma rehberi
├── 📄 .gitignore                         # Git ignore dosyası
│
├── 📁 .github/
│   └── workflows/
│       └── 📄 deepseek.yml              # Ana bot workflow dosyası
│
└── 📁 docs/                              # Dokümantasyon klasörü
    ├── 📄 INDEX.md                       # Dokümantasyon indeksi
    ├── 📄 QUICK_START.md                 # 5 dakikalık başlangıç
    ├── 📄 FAQ.md                         # Sık sorulan sorular
    ├── 📄 EXAMPLES.md                    # Gerçek kullanım örnekleri
    ├── 📄 PROJECT_STRUCTURE.md           # Bu dosya
    │
    └── 📁 templates/                     # Proje şablonları
        ├── 📄 PYTHON_API_TEMPLATE.md     # Python REST API şablonu
        ├── 📄 NODEJS_API_TEMPLATE.md     # Node.js API şablonu
        ├── 📄 REACT_APP_TEMPLATE.md      # React App şablonu
        └── 📄 FULLSTACK_TEMPLATE.md      # Full-stack şablonu
```

## 📋 Dosya Açıklamaları

### Kök Dizin Dosyaları

#### 📄 README.md
**Amaç**: Projenin ana giriş sayfası
**İçerik**:
- Projeye genel bakış
- Temel kullanım talimatları
- Özellikler listesi
- Güvenlik bilgileri
- Hızlı başlangıç linkleri

**Hedef Kitle**: Yeni kullanıcılar, proje hakkında bilgi almak isteyenler

#### 📄 USAGE_GUIDE.md
**Amaç**: Detaylı ve kapsamlı kullanım kılavuzu
**İçerik**:
- Adım adım kullanım talimatları
- İyi ve kötü talep örnekleri
- Güncelleme ve silme işlemleri
- Proje türlerine göre örnekler
- En iyi pratikler
- Sorun giderme

**Hedef Kitle**: Sistemin tüm özelliklerini öğrenmek isteyen kullanıcılar

#### 📄 CONTRIBUTING.md
**Amaç**: Katkıda bulunma rehberi
**İçerik**:
- Katkı türleri
- Katkı süreci
- Kod standartları
- Commit mesaj formatı
- Pull request şablonu

**Hedef Kitle**: Projeye katkıda bulunmak isteyen geliştiriciler

#### 📄 .gitignore
**Amaç**: Git'in görmezden geleceği dosyaları tanımlar
**İçerik**:
- Derleme çıktıları
- Bağımlılık klasörleri (node_modules, venv)
- IDE dosyaları
- Log dosyaları
- Ortam değişkenleri (.env)

### GitHub Workflows

#### 📄 .github/workflows/deepseek.yml
**Amaç**: Ana otomasyon workflow'u
**Tetikleyiciler**:
- Issue açıldığında (`issues: opened`)
- Issue yorumu eklendiğinde (`issue_comment: created`)

**İşlevler**:
1. Issue içeriğini okur
2. DeepSeek AI'a gönderir
3. AI yanıtını parse eder
4. Dosyaları oluşturur/günceller/siler
5. Sonuç raporunu issue'ya yazar

**Önemli Özellikler**:
- Korumalı dosya listesi
- Hata yönetimi
- Güvenlik kontrolleri
- Detaylı logging

### Dokümantasyon Klasörü

#### 📄 docs/INDEX.md
**Amaç**: Tüm dokümantasyonun merkezi indeksi
**İçerik**:
- Dokümantasyon haritası
- Hızlı linkler
- Öğrenme yolu
- Versiyon geçmişi

**Hedef Kitle**: Dokümantasyonda gezinmek isteyenler

#### 📄 docs/QUICK_START.md
**Amaç**: Yeni kullanıcılar için hızlı başlangıç
**İçerik**:
- 3 adımda proje oluşturma
- Basit örnekler
- İpuçları
- İlk adım senaryoları

**Hedef Kitle**: Hemen başlamak isteyen yeni kullanıcılar

#### 📄 docs/FAQ.md
**Amaç**: Sık sorulan soruların cevaplanması
**İçerik**:
- Genel sorular
- Kullanım soruları
- Teknik sorular
- Sorun giderme
- Güvenlik soruları

**Hedef Kitle**: Sorunla karşılaşan veya merak eden kullanıcılar

#### 📄 docs/EXAMPLES.md
**Amaç**: Gerçek kullanım örnekleri
**İçerik**:
- Kullanıcı istekleri
- Bot çıktıları
- Farklı proje türleri
- Başarılı senaryolar

**Hedef Kitle**: Örnek görerek öğrenmek isteyenler

### Şablon Klasörü

#### 📄 docs/templates/*.md
**Amaç**: Proje türlerine göre hazır şablonlar

**Mevcut Şablonlar**:

1. **PYTHON_API_TEMPLATE.md**
   - Python Flask/FastAPI API projesi
   - Database entegrasyonu
   - JWT authentication
   - Testing stratejisi

2. **NODEJS_API_TEMPLATE.md**
   - Node.js Express/NestJS API
   - MongoDB/PostgreSQL
   - Middleware yapısı
   - DevOps entegrasyonu

3. **REACT_APP_TEMPLATE.md**
   - Modern React uygulaması
   - TypeScript desteği
   - State management
   - Component yapısı

4. **FULLSTACK_TEMPLATE.md**
   - Frontend + Backend
   - Docker entegrasyonu
   - API entegrasyonu
   - Deployment stratejisi

**Hedef Kitle**: Belirli bir proje türü oluşturmak isteyenler

## 🔄 Dosya İlişkileri

```
README.md
    ↓
    ├─→ QUICK_START.md (Hızlı başlangıç için)
    ├─→ USAGE_GUIDE.md (Detaylı bilgi için)
    └─→ FAQ.md (Sorular için)

USAGE_GUIDE.md
    ↓
    └─→ templates/*.md (Şablonlar için)

templates/*.md
    ↓
    └─→ EXAMPLES.md (Örnekler için)

INDEX.md
    ↓
    └─→ TÜM DOSYALAR (Merkezi erişim)
```

## 📊 Kullanım Akışı

### Yeni Kullanıcı
```
1. README.md oku
2. QUICK_START.md ile başla
3. İlk projeyi oluştur
4. FAQ.md'ye bak (sorun varsa)
```

### Deneyimli Kullanıcı
```
1. templates/*.md seç
2. Şablonu özelleştir
3. Issue oluştur
4. EXAMPLES.md'den referans al
```

### Katkıda Bulunan
```
1. CONTRIBUTING.md oku
2. Issue aç
3. Değişiklik yap
4. Pull Request gönder
```

## 🎯 Dosya Sorumluluğu

| Dosya | Sorumlu | Güncelleme Sıklığı |
|-------|---------|-------------------|
| README.md | Maintainer | Her major değişiklik |
| USAGE_GUIDE.md | Maintainer | Yeni özellikler |
| CONTRIBUTING.md | Maintainer | Proje politikası değişikliği |
| deepseek.yml | Maintainer | Bug fix ve yeni özellikler |
| FAQ.md | Community | Yeni sorular eklendiğinde |
| EXAMPLES.md | Community | Yeni örnekler eklendiğinde |
| templates/*.md | Community | Yeni şablonlar veya güncellemeler |

## 🔒 Korumalı Dosyalar

Bu dosyalar bot tarafından **asla silinemez**:

- `.gitignore`
- `README.md`
- `.github/workflows/deepseek.yml`
- `package.json`, `package-lock.json`
- `requirements.txt`
- `Gemfile`, `Gemfile.lock`
- `go.mod`, `go.sum`
- `Cargo.toml`, `Cargo.lock`

## 📈 Gelecek Yapı

Planlanan eklemeler:

```
yeni-uygulama/
├── docs/
│   ├── templates/
│   │   ├── VUE_APP_TEMPLATE.md (🔜)
│   │   ├── DJANGO_API_TEMPLATE.md (🔜)
│   │   ├── FLUTTER_APP_TEMPLATE.md (🔜)
│   │   └── NEXTJS_TEMPLATE.md (🔜)
│   ├── guides/
│   │   ├── DEPLOYMENT.md (🔜)
│   │   └── BEST_PRACTICES.md (🔜)
│   └── CHANGELOG.md (🔜)
```

## 🛠️ Bakım

### Düzenli Güncellemeler
- ✅ FAQ'ye yeni sorular ekleyin
- ✅ EXAMPLES.md'ye yeni örnekler ekleyin
- ✅ Şablonları güncel tutun
- ✅ Workflow'u optimize edin

### Yeni Özellik Eklerken
- ✅ README.md'yi güncelleyin
- ✅ Uygun şablonu ekleyin/güncelleyin
- ✅ Örnek ekleyin
- ✅ FAQ güncelleyin (gerekirse)

---

**📁 İyi organize edilmiş bir proje, başarılı bir projedir!**

*Son güncelleme: 2025-12-09*

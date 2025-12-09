# 🧪 Test Örnekleri - Hemen Deneyin!

Bu dosyadaki örnekleri **birebir kopyalayıp** GitHub Issue'larında test edebilirsiniz.

## 🎯 Basit Başlangıç Testleri

### Test 1: Python Hesap Makinesi (2 dakika)

Issue'ya şunu yazın:
```
Python ile basit hesap makinesi yap.

Özellikler:
- Toplama, çıkarma, çarpma, bölme fonksiyonları
- Komut satırından kullanım
- Input validasyonu

Dosyalar:
- src/calculator.py
- README.md (kullanım talimatları)
```

**Beklenen Sonuç**: Bot 2 dosya oluşturacak
- ✅ `src/calculator.py`
- ✅ `README.md`

---

### Test 2: HTML Portfolyo Sayfası (3 dakika)

Issue'ya şunu yazın:
```
HTML/CSS ile basit portfolyo sayfası yap.

İçerik:
- Header (isim, title)
- About section
- Projects section (3 örnek proje)
- Contact section (email, sosyal medya)

Dosyalar:
- index.html
- css/style.css
- README.md
```

**Beklenen Sonuç**: Bot 3 dosya oluşturacak
- ✅ `index.html`
- ✅ `css/style.css`
- ✅ `README.md`

---

### Test 3: Node.js Basit Server (4 dakika)

Issue'ya şunu yazın:
```
Node.js ile basit HTTP server yap.

Endpoints:
- GET / (Ana sayfa mesajı)
- GET /api/time (şu anki zaman)
- GET /api/random (rastgele sayı)

Dosyalar:
- src/server.js
- package.json
- README.md
```

**Beklenen Sonuç**: Bot 3 dosya oluşturacak
- ✅ `src/server.js`
- ✅ `package.json`
- ✅ `README.md`

---

## 🔄 Güncelleme Testi

### Test 4: Var Olan Dosyayı Güncelleme

**Adım 1**: İlk olarak yukarıdaki Test 1'i çalıştırın

**Adım 2**: Aynı issue'ya **yorum** olarak şunu ekleyin:
```
src/calculator.py dosyasına üs alma (power) fonksiyonu ekle.
```

**Beklenen Sonuç**: Bot `src/calculator.py` dosyasını güncelleyecek
- ✅ Üs alma fonksiyonu eklenmiş olacak

---

## 🗑️ Silme Testi

### Test 5: Dosya Silme

**Adım 1**: Herhangi bir test ile dosya oluşturun

**Adım 2**: Issue'ya **yorum** olarak şunu yazın:
```
sil: src/calculator.py
```

**Beklenen Sonuç**: Bot dosyayı silecek
- 🗑️ `src/calculator.py` silinmiş olacak

⚠️ **Not**: README.md gibi korumalı dosyalar silinemez

---

## 🎓 Orta Seviye Testler

### Test 6: React Todo App (10 dakika)

```
React ile Todo List uygulaması yap.

Özellikler:
- Todo ekleme
- Todo silme
- Todo tamamlama (checkbox)
- Local storage ile kaydetme

Componentler:
- App.jsx (ana component)
- TodoList.jsx (liste)
- TodoItem.jsx (tek item)
- TodoForm.jsx (ekleme formu)

Dosyalar:
- src/App.jsx
- src/components/TodoList.jsx
- src/components/TodoItem.jsx
- src/components/TodoForm.jsx
- src/App.css
- package.json
- README.md
```

**Beklenen Sonuç**: 7 dosya oluşacak

---

### Test 7: Python Flask API (15 dakika)

```
Python Flask ile basit REST API yap.

Endpoints:
- GET /api/items (tüm items)
- POST /api/items (yeni item)
- DELETE /api/items/:id (item sil)

Özellikler:
- In-memory storage (liste)
- JSON response
- CORS enabled
- Error handling

Dosyalar:
- src/app.py
- src/routes.py
- requirements.txt
- README.md
```

**Beklenen Sonuç**: 4 dosya oluşacak

---

### Test 8: Node.js + Express + MongoDB (20 dakika)

```
Node.js Express ile kullanıcı yönetim API'si yap.

Database: MongoDB (Mongoose)

Endpoints:
- POST /api/users (kullanıcı oluştur)
- GET /api/users (tüm kullanıcılar)
- GET /api/users/:id (tek kullanıcı)
- PUT /api/users/:id (güncelle)
- DELETE /api/users/:id (sil)

Klasör yapısı:
- src/app.js
- src/routes/userRoutes.js
- src/controllers/userController.js
- src/models/User.js
- src/config/database.js
- .env.example
- package.json
- README.md
```

**Beklenen Sonuç**: 8 dosya oluşacak

---

## 🚀 İleri Seviye Test

### Test 9: Full-Stack Mini Proje (30 dakika)

```
Full-stack basit blog uygulaması yap.

BACKEND (Node.js + Express):
Endpoints:
- GET /api/posts (tüm postlar)
- POST /api/posts (yeni post)
- In-memory storage

Dosyalar:
- backend/src/app.js
- backend/src/routes.js
- backend/package.json

FRONTEND (React):
Sayfalar:
- PostList (post listesi)
- CreatePost (yeni post formu)

Dosyalar:
- frontend/src/App.jsx
- frontend/src/components/PostList.jsx
- frontend/src/components/CreatePost.jsx
- frontend/package.json

ROOT:
- README.md (kurulum talimatları)
- .gitignore
```

**Beklenen Sonuç**: 9 dosya oluşacak

---

## ✅ Test Sonuçlarını Doğrulama

Her test sonrası kontrol edin:

1. **Bot Yanıtı**:
   - ✅ Issue'da bot yorumu geldi mi?
   - ✅ Raporda dosyalar listeleniyor mu?
   - ✅ Hata var mı?

2. **Dosyalar**:
   - ✅ Belirtilen dosyalar oluştu mu?
   - ✅ Dosya içerikleri doğru mu?
   - ✅ Klasör yapısı doğru mu?

3. **İçerik**:
   - ✅ Kod çalışır durumda mı?
   - ✅ Yorumlar açıklayıcı mı?
   - ✅ README talimatları net mi?

## 🎯 Başarı Kriterleri

Test başarılı sayılır eğer:
- ✅ Bot 2 dakika içinde yanıt verdi
- ✅ Tüm dosyalar oluşturuldu
- ✅ Kod syntax hatası yok
- ✅ README açıklayıcı

## 🐛 Sorun mu Yaşadınız?

Test sırasında sorun yaşarsanız:

1. **Bot yanıt vermiyorsa**:
   - DEEPSEEK_API_KEY secret kontrolü
   - Workflow aktif mi kontrol edin
   - 5 dakika bekleyin

2. **Dosyalar oluşmadıysa**:
   - Bot raporunu okuyun
   - Hata mesajlarını kontrol edin
   - Issue'yı tekrar yazın

3. **Kod hatalıysa**:
   - Issue yorumuna düzeltme isteği yazın
   - Daha detaylı açıklama yapın

## 💡 Test İpuçları

1. **Küçük Başlayın**: İlk önce basit testleri yapın
2. **Adım Adım**: Her testten sonra sonucu doğrulayın
3. **Sabırlı Olun**: Bot'un yanıt vermesi 1-3 dakika sürebilir
4. **Detaylı Yazın**: Ne kadar detaylı talep, o kadar iyi sonuç
5. **Örneklere Bakın**: Şablonları ve örnekleri kullanın

## 🎉 Başarı Mesajları

Test başarılı olduğunda göreceğiniz mesajlar:

```
✅ src/app.py oluşturuldu
✅ README.md oluşturuldu
✅ package.json oluşturuldu

📊 İşlem Özeti
- ✅ Başarılı: 3 işlem
- ❌ Hatalı: 0 işlem
- 📁 Oluşturulan/Güncellenen: 3 dosya
- 🗑️ Silinen: 0 dosya
```

---

## 📚 Sonraki Adımlar

Testleri başarıyla tamamladıktan sonra:

1. ✅ `USAGE_GUIDE.md` - Detaylı kullanım
2. ✅ `docs/templates/` - Proje şablonları
3. ✅ `EXAMPLES.md` - Gerçek örnekler
4. ✅ Kendi projelerinizi oluşturun!

---

**🚀 Hemen bir test seçin ve Issue açın! Başarılar!**

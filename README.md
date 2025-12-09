# 🤖 DeepSeek ULTRA Enterprise Architect

Bu repo, **GitHub Issues** üzerinden verdiğiniz taleplere göre otomatik olarak proje dosyaları oluşturan, güncelleyen ve silen akıllı bir sistemdir.

## 🚀 Nasıl Kullanılır?

### 1. Issue Oluşturun
GitHub'da bu repo için yeni bir **Issue** açın.

### 2. Talebinizi Yazın
Issue içeriğinde ne istediğinizi **açık ve detaylı** bir şekilde yazın:

#### Örnek Talepler:
```
Bana basit bir Python hesap makinesi uygulaması yap. 
Toplama, çıkarma, çarpma ve bölme işlemleri olsun.
src/ klasöründe olsun ve testleri de ekle.
```

```
Node.js ile bir REST API oluştur. 
Express kullan, kullanıcı CRUD işlemleri olsun.
MongoDB bağlantısı ve .env.example dosyası da ekle.
```

```
React ile basit bir Todo uygulaması yap.
Modern tasarım, localStorage kullan.
src/components/, src/pages/ klasör yapısı olsun.
```

### 3. Sistem Otomatik Çalışır
- Bot talebinizi analiz eder
- Gerekli tüm dosyaları oluşturur
- Klasör yapısını düzenler
- Test dosyalarını ekler
- Dokümantasyon hazırlar
- Size rapor gönderir

### 4. Yorum Yaparak Güncelleme İsteyin
Oluşturulan dosyalarda değişiklik istiyorsanız, aynı issue'ya **yorum** ekleyin:

```
src/app.py dosyasında logaritma özelliği de ekle
```

```
sil: src/old_file.py
tests/ klasöründeki dosyaları güncelle
```

## 📁 Oluşturulacak Dosya Yapısı

Bot her proje için profesyonel bir klasör yapısı oluşturur:

```
proje/
├── src/                 # Ana kaynak kodlar
├── tests/               # Test dosyaları
├── docs/                # Dokümantasyon
├── configs/             # Yapılandırma dosyaları
├── .env.example         # Ortam değişkenleri örneği
├── README.md            # Proje açıklaması
├── requirements.txt     # Python bağımlılıkları (eğer Python projesi ise)
├── package.json         # Node.js bağımlılıkları (eğer Node.js projesi ise)
└── Dockerfile          # Docker yapılandırması (uygunsa)
```

## ✨ Özellikler

- ✅ **Otomatik Kod Üretimi**: Talebinize göre tüm dosyaları oluşturur
- ✅ **Modüler Yapı**: Profesyonel klasör organizasyonu
- ✅ **Test Dahil**: Test dosyaları otomatik eklenir
- ✅ **Dokümantasyon**: Açıklayıcı README ve yorumlar
- ✅ **Güvenli Silme**: Kritik dosyalar korunur
- ✅ **Çoklu Dil Desteği**: Python, Node.js, Go, Java, React, vb.
- ✅ **Türkçe ve İngilizce**: Kod yorumları her iki dilde

## 🛡️ Güvenlik

Aşağıdaki kritik dosyalar **asla silinmez**:
- `.gitignore`
- `README.md`
- `.github/workflows/deepseek.yml`
- `package.json`, `package-lock.json`
- `requirements.txt`
- `Gemfile`, `Gemfile.lock`
- `go.mod`, `go.sum`
- `Cargo.toml`, `Cargo.lock`

## 📋 İpuçları

1. **Net Olun**: "Web sitesi yap" yerine "React ile e-ticaret sitesi yap, ürün listesi ve sepet olsun"
2. **Detay Verin**: Hangi teknolojileri, hangi özellikleri istediğinizi belirtin
3. **Aşama Aşama**: Büyük projeler için önce temel yapıyı isteyin, sonra özellik ekleyin
4. **Silme İçin**: "sil: dosya/yolu" formatını kullanın

## 🔧 Teknik Detaylar

- **AI Motor**: DeepSeek AI
- **Otomasyon**: GitHub Actions
- **Tetikleyici**: Issue ve Issue Comment olayları
- **Maksimum Token**: 4000
- **Sıcaklık**: 0.15 (tutarlı sonuçlar için)

## 📞 Destek

Herhangi bir sorun yaşarsanız:
1. Yeni bir Issue açın ve sorununuzu açıklayın
2. Bot otomatik olarak yardımcı olmaya çalışacaktır
3. Issue'da "@mehmet0116" etiketleyerek doğrudan yardım isteyebilirsiniz

---

**🎯 Hedef**: Size mükemmel, temiz, sürdürülebilir ve ölçeklenebilir kod üretmek!

*Powered by DeepSeek ULTRA Enterprise Architect v2.3*

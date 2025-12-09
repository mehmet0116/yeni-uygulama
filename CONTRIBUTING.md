# 🤝 Katkıda Bulunma Rehberi

DeepSeek ULTRA Enterprise Architect projesine katkıda bulunmak istediğiniz için teşekkürler!

## 🎯 Katkı Türleri

### 1. 📝 Dokümantasyon
- Yeni şablonlar ekleyin
- Mevcut dokümantasyonu geliştirin
- Örnekler ve kullanım senaryoları ekleyin
- Türkçe ve İngilizce çeviriler

### 2. 🐛 Bug Raporları
- Hataları detaylı açıklayın
- Yeniden üretme adımlarını ekleyin
- Beklenen ve gerçek davranışı belirtin
- Ekran görüntüleri ekleyin

### 3. 💡 Özellik Önerileri
- Yeni özellik fikirleri
- Workflow iyileştirmeleri
- Yeni dil/framework desteği
- Performans optimizasyonları

### 4. 🔧 Kod Katkıları
- Workflow geliştirmeleri
- Yeni özellikler
- Bug düzeltmeleri
- Test coverage artırımı

## 📋 Nasıl Katkıda Bulunulur?

### Adım 1: Issue Açın
Herhangi bir değişiklik yapmadan önce bir issue açın:

```
Başlık: [TÜR] Kısa açıklama

Türler:
- [BUG] Hata bildirimi
- [FEATURE] Yeni özellik
- [DOCS] Dokümantasyon
- [TEMPLATE] Yeni şablon

Açıklama:
- Ne yapılacak?
- Neden gerekli?
- Nasıl yapılacak? (opsiyonel)
```

### Adım 2: Tartışın
- Issue'da tartışın
- Onay alın
- Yaklaşım üzerinde anlaşın

### Adım 3: Geliştirin
1. Fork yapın
2. Yeni branch oluşturun: `git checkout -b feature/your-feature`
3. Değişikliklerinizi yapın
4. Test edin
5. Commit edin: `git commit -m "Add: your feature"`
6. Push edin: `git push origin feature/your-feature`

### Adım 4: Pull Request
- Detaylı açıklama yazın
- Issue'yu referans gösterin
- Değişiklikleri listeleyin
- Screenshot ekleyin (UI değişiklikleri için)

## 📝 Dokümantasyon Katkıları

### Yeni Şablon Ekleme

1. `docs/templates/` klasörüne yeni dosya ekleyin
2. Şablon formatını takip edin:

```markdown
# 🔸 [Teknoloji] Proje Şablonu

## 📋 Talep Şablonu
[Issue'da kullanılacak format]

## 🎯 Beklenen Çıktı
[Oluşturulacak dosya yapısı]

## 💡 Örnekler
[Kullanım senaryoları]
```

3. `docs/INDEX.md` dosyasını güncelleyin
4. Örnek kullanım ekleyin

### Mevcut Dokümanı Geliştirme

- Açıklık ekleyin
- Örnekler ekleyin
- Görsel ekleyin (gerekirse)
- Hataları düzeltin

## 🐛 Bug Raporu Formatı

```markdown
### Hata Açıklaması
[Hatayı kısa ve net açıklayın]

### Yeniden Üretme Adımları
1. [İlk adım]
2. [İkinci adım]
3. [Üçüncü adım]

### Beklenen Davranış
[Ne olmasını bekliyordunuz?]

### Gerçek Davranış
[Ne oldu?]

### Ekran Görüntüleri
[Varsa ekleyin]

### Ortam
- İşletim Sistemi: [Windows/Mac/Linux]
- Bot Version: [v2.3]
- Browser: [Chrome/Firefox/Safari]
```

## 💡 Özellik İsteği Formatı

```markdown
### Özellik Açıklaması
[Özelliği detaylı açıklayın]

### Motivasyon
[Neden bu özellik gerekli?]

### Önerilen Çözüm
[Nasıl implement edilebilir?]

### Alternatifler
[Başka çözümler var mı?]

### Ek Bağlam
[Diğer bilgiler, örnekler]
```

## 🔧 Kod Katkıları

### Workflow Değişiklikleri

`.github/workflows/deepseek.yml` dosyasını değiştiriyorsanız:

1. Mevcut davranışı bozmayın
2. Geriye dönük uyumluluğu koruyun
3. Değişiklikleri test edin
4. Dokümantasyonu güncelleyin

### Commit Mesajları

Format:
```
Type: Kısa açıklama (50 karakter max)

Detaylı açıklama (72 karakter max satır genişliği)

- Değişiklik 1
- Değişiklik 2
- Değişiklik 3
```

Types:
- `Add`: Yeni özellik
- `Fix`: Bug düzeltmesi
- `Update`: Mevcut özellik güncellemesi
- `Remove`: Kaldırma
- `Refactor`: Kod iyileştirme
- `Docs`: Dokümantasyon değişikliği
- `Test`: Test ekleme/değiştirme

Örnekler:
```
Add: Python Django template

Docs: Update FAQ with common errors

Fix: Workflow event filtering logic
```

## ✅ Kontrol Listesi

Pull Request göndermeden önce:

- [ ] Issue açıldı ve onaylandı
- [ ] Kod değişiklikleri test edildi
- [ ] Dokümantasyon güncellendi
- [ ] Commit mesajları anlamlı
- [ ] README günceldir (gerekirse)
- [ ] Örnekler eklendi (yeni özellik için)
- [ ] Geriye dönük uyumluluk korundu

## 🎨 Stil Rehberi

### Markdown
- Başlıklar için emoji kullanın
- Liste için tire (-) kullanın
- Kod blokları için backtick (```) kullanın
- Türkçe karakterleri doğru kullanın

### Kod
- Okunabilir ve temiz kod
- Anlamlı değişken isimleri
- Yorum ekleyin (Türkçe ve İngilizce)
- Tutarlı formatlamaya uyun

## 📞 İletişim

### Soru Sormak
- Issue açın, "Question" etiketi ekleyin
- @mehmet0116 mention edin

### Tartışma
- Issue'da tartışın
- Discord/Slack (varsa) kullanın

### Yardım
- Başlarken yardım isteyebilirsiniz
- "good first issue" etiketli issue'lara bakın

## 🏆 Katkıda Bulunanlar

Tüm katkıda bulunanlara teşekkür ederiz! 🙏

(Buraya otomatik olarak contributor listesi eklenecek)

## 📄 Lisans

Bu projeye katkıda bulunarak, katkılarınızın proje lisansı altında yayınlanmasını kabul edersiniz.

---

**Katkılarınız projeyi daha iyi hale getirir! Teşekkürler! 🎉**

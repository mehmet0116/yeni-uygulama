# ❓ Sık Sorulan Sorular (FAQ)

## Genel Sorular

### Bot nasıl çalışır?
Bot, GitHub Issues'da yazdığınız talepleri DeepSeek AI ile analiz eder ve otomatik olarak kod dosyaları oluşturur.

### Hangi dilleri destekliyor?
- **Backend**: Python, Node.js, Go, Java, PHP, Ruby
- **Frontend**: React, Vue, Angular, Svelte, HTML/CSS/JS
- **Mobile**: React Native, Flutter
- **Data Science**: Python (Pandas, NumPy, TensorFlow)
- **DevOps**: Bash, Docker, Kubernetes

### Ücretsiz mi?
Evet! GitHub Actions üzerinde çalışır ve repo sahibi API key'i sağladığında kullanılabilir.

## Kullanım Soruları

### Nasıl başlarım?
1. GitHub Issues'da yeni bir issue aç
2. Ne istediğini detaylı yaz
3. Bot otomatik dosyaları oluşturacak

### Bot yanıt vermiyor?
Kontrol listesi:
- [ ] DEEPSEEK_API_KEY secret'ı eklenmiş mi?
- [ ] Workflow dosyası aktif mi (.github/workflows/deepseek.yml)?
- [ ] Issue'yu github-actions[bot] oluşturmadı değil mi?
- [ ] Issue body'si boş değil mi?

### Dosyalar oluşturulmadı?
- Bot yanıtındaki raporu kontrol edin
- Dosya yollarının geçerli olduğundan emin olun (.. veya / içermemeli)
- Hata mesajlarını okuyun

### Yanlış kod üretildi?
- Issue'ya yorum ekleyerek düzeltme isteyin
- Daha detaylı açıklama yapın
- Örnek kod veya referans gösterin

## Teknik Sorular

### Maksimum dosya boyutu nedir?
DeepSeek API response limiti nedeniyle tek seferde ~4000 token (yaklaşık 15-20 dosya).

### Çok fazla dosya oluşturmam gerekirse?
Projeyi aşamalara bölün:
1. İlk issue: Temel yapı
2. İkinci issue: Ek özellikler
3. Üçüncü issue: Test ve dokümantasyon

### Var olan dosyayı güncelleyebilir miyim?
Evet! Aynı dosya yolunu tekrar belirtirseniz, bot dosyayı günceller.

### Dosya silebilir miyim?
Evet, issue'da şu formatı kullanın:
```
sil: dosya/yolu.ext
```

⚠️ Korumalı dosyalar silinemez (.gitignore, README.md, workflow dosyası, vb.)

### Özel dependency'ler ekleyebilir miyim?
Evet! Talebinizde belirtin:
```
package.json'a şu paketleri ekle:
- express
- mongoose
- dotenv
```

## Özellik Soruları

### Database işlemleri yapabilir mi?
Evet, database model ve connection kodları oluşturabilir. Ancak actual database'i kendiniz ayarlamanız gerekir.

### API entegrasyonu yapabilir mi?
Evet, 3rd party API'lere istek yapan kod yazabilir (fetch, axios, vb.)

### Test yazabilir mi?
Evet, unit test ve integration test dosyaları oluşturabilir. Jest, pytest, Mocha gibi framework'leri destekler.

### Docker file oluşturabilir mi?
Evet, Dockerfile ve docker-compose.yml oluşturabilir.

### GitHub Actions workflow oluşturabilir mi?
Evet, ancak mevcut deepseek.yml workflow'u korur. Başka workflow'lar oluşturabilir.

## Güvenlik Soruları

### Bot repo'ma zarar verebilir mi?
Hayır. Bot sadece belirtilen dosyaları oluşturur/günceller. Kritik dosyalar korumalıdır.

### Hangi dosyalar korunuyor?
- .gitignore
- README.md
- .github/workflows/deepseek.yml
- package.json, package-lock.json
- requirements.txt
- Gemfile, Gemfile.lock
- go.mod, go.sum
- Cargo.toml, Cargo.lock

### API key'im güvende mi?
Evet, API key GitHub Secrets'ta saklanır ve workflow dışında erişilemez.

### Bot kötü kod yazabilir mi?
Bot en iyi pratikleri takip eder, ancak üretilen kodu gözden geçirmeniz önerilir.

## Performans Soruları

### Ne kadar sürede tamamlanır?
Genelde 1-3 dakika. Karmaşık projeler 5 dakika alabilir.

### Aynı anda birden fazla işlem yapabilir miyim?
Evet, farklı issue'lar paralel işlenebilir.

### Rate limit var mı?
DeepSeek API'nin limitleri vardır. Çok fazla istek göndermekten kaçının.

## Sorun Giderme

### "API hatası" mesajı alıyorum
- API key doğru mu kontrol edin
- DeepSeek API quota'nızı kontrol edin
- İnternet bağlantısını kontrol edin

### "Geçersiz dosya adı" hatası
- Dosya yolu ".." veya "/" içermemeli
- Geçerli karakter kullanın
- Örnek: `src/app.js` ✅, `../hack.js` ❌

### Workflow çalışmıyor
```bash
# Workflow dosyasını kontrol edin
cat .github/workflows/deepseek.yml

# Git log kontrol edin
git log --oneline -5
```

### Bot eski dosyayı silmedi
Korumalı dosya olabilir. Listeyi kontrol edin.

## İleri Seviye

### Özel prompt ekleyebilir miyim?
Hayır, system prompt workflow içinde sabitlenmiştir. Ancak issue içeriğinizde detaylı talimatlar verebilirsiniz.

### Birden fazla AI model kullanabilir miyim?
Şu anda sadece DeepSeek destekleniyor.

### Kendi AI key'im olmadan kullanabilir miyim?
Hayır, repo owner'ının DEEPSEEK_API_KEY secret'ı eklemesi gerekir.

### Başka GitHub Action'larla entegre edebilir miyim?
Evet, standart GitHub Actions workflow'u olduğu için diğer action'larla birlikte kullanılabilir.

## Destek

### Daha fazla yardım almak için?
1. Yeni bir issue açın, sorununuzu açıklayın
2. `@mehmet0116` mention edin
3. [USAGE_GUIDE.md](USAGE_GUIDE.md) detaylı kılavuzu okuyun
4. [docs/templates/](templates/) şablonlara göz atın

### Feature request nasıl yapılır?
Issue açın, "Feature Request" başlığı kullanın, özelliği detaylı anlatın.

### Bug nasıl bildirilir?
Issue açın, "Bug Report" başlığı kullanın, şunları ekleyin:
- Hata açıklaması
- Adımlar (reproduce)
- Beklenen davranış
- Gerçek davranış
- Screenshots (varsa)

---

**Sorunuz cevap bulamadı mı? Yeni bir Issue açın! 🤝**

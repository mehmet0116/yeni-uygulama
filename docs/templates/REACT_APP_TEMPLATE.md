# ⚛️ React Uygulama Proje Şablonu

Bu şablonu kullanarak modern React uygulaması oluşturabilirsiniz.

## 📋 Talep Şablonu

Issue'da şu formatı kullanın:

```
React ile [uygulama türü] oluştur.

Özellikler:
- TypeScript / JavaScript (seçiminizi belirtin)
- State Management: Redux / Context API / Zustand
- Styling: CSS Modules / Styled Components / Tailwind CSS
- Routing: React Router v6
- Form Management: React Hook Form
- API iletişimi: Axios / Fetch

Sayfalar:
- Ana sayfa (/)
- Hakkında (/about)
- İletişim (/contact)
- [Diğer sayfalar...]

Bileşenler:
- Header (navigation)
- Footer
- Button
- Card
- Modal
- Form inputs
- [Diğer bileşenler...]

Özellikler:
- Responsive tasarım (mobil uyumlu)
- Dark mode / Light mode
- Loading states
- Error handling
- Form validation
- Local storage
- SEO optimizasyonu

Klasör yapısı:
- src/components/ (yeniden kullanılabilir bileşenler)
- src/pages/ (sayfa bileşenleri)
- src/hooks/ (custom hooks)
- src/context/ veya src/store/ (state management)
- src/services/ (API çağrıları)
- src/utils/ (yardımcı fonksiyonlar)
- src/styles/ (global stiller)
- src/assets/ (resimler, iconlar)
- src/types/ (TypeScript tipleri)
- tests/ (component testleri)

Ek:
- Jest + React Testing Library
- ESLint + Prettier
- Storybook (bileşen dokümantasyonu)
- .env.example
- README.md
```

## 🎯 Beklenen Çıktı

```
react-app/
├── public/
│   ├── index.html
│   └── favicon.ico
├── src/
│   ├── components/
│   │   ├── common/
│   │   │   ├── Button/
│   │   │   │   ├── Button.jsx
│   │   │   │   ├── Button.module.css
│   │   │   │   └── Button.test.jsx
│   │   │   ├── Card/
│   │   │   └── Modal/
│   │   ├── layout/
│   │   │   ├── Header/
│   │   │   └── Footer/
│   ├── pages/
│   │   ├── Home/
│   │   │   ├── Home.jsx
│   │   │   └── Home.module.css
│   │   ├── About/
│   │   └── Contact/
│   ├── hooks/
│   │   ├── useAuth.js
│   │   └── useFetch.js
│   ├── context/
│   │   └── AuthContext.jsx
│   ├── services/
│   │   └── api.js
│   ├── utils/
│   │   └── helpers.js
│   ├── styles/
│   │   └── global.css
│   ├── App.jsx
│   ├── App.test.jsx
│   └── index.js
├── tests/
│   └── setup.js
├── .env.example
├── .eslintrc.js
├── .prettierrc
├── package.json
├── README.md
└── .gitignore
```

## 💡 Uygulama Türü Örnekleri

### 1. Todo List Uygulaması
```
React ile Todo List uygulaması yap.

Özellikler:
- Todo ekleme, düzenleme, silme
- Todo tamamlama (checkbox)
- Filtreleme (Tümü, Aktif, Tamamlanan)
- Local storage ile kaydetme
- Sürükle-bırak ile sıralama (react-beautiful-dnd)
- Dark mode
```

### 2. E-Ticaret Sitesi
```
React ile e-ticaret sitesi frontend'i oluştur.

Sayfalar:
- Ana sayfa (ürün listesi)
- Ürün detay
- Sepet
- Checkout
- Kullanıcı profili

Özellikler:
- Ürün filtreleme ve arama
- Sepete ekleme
- Miktar artırma/azaltma
- Favori ürünler
- Responsive design
```

### 3. Dashboard / Admin Panel
```
React ile admin dashboard oluştur.

Bileşenler:
- Sidebar navigation
- Top bar (search, notifications)
- Dashboard (charts, statistics)
- Tablo (sorting, filtering, pagination)
- Form sayfaları

Kütüphaneler:
- Chart.js veya Recharts (grafikler)
- Material-UI veya Ant Design
- React Table
```

### 4. Blog Platform
```
React ile blog okuma platformu yap.

Özellikler:
- Yazı listesi (grid layout)
- Yazı detay sayfası
- Markdown desteği
- Yorum sistemi
- Arama ve filtreleme
- Kategori/tag sistemi
- Okuma süresi hesaplama
```

## 🧪 Test Örnekleri

```
Test gereksinimleri:
- Her component için test dosyası
- Snapshot testleri
- User interaction testleri
- API mock'ları
- %80+ code coverage
```

## 📚 Ek Özellikler İsteme

```
Ayrıca şunları da ekle:
- PWA (Progressive Web App)
- Internationalization (i18n)
- Analytics entegrasyonu
- Error boundary
- Lazy loading
- Code splitting
```

## 🎨 Tasarım İstekleri

```
Tasarım:
- Minimal ve modern
- Mavi-beyaz renk paleti
- Google Fonts (Roboto)
- Animasyonlar (Framer Motion)
- Glassmorphism efektleri
```

#!/usr/bin/env python3
"""
Proje dosya kontrol sistemi
DeepSeek ULTRA Enterprise Architect v4.0 tarafından oluşturuldu
"""

import os
import sys
import json
from pathlib import Path
from datetime import datetime
import hashlib

class ProjectFileChecker:
    def __init__(self, root_dir="."):
        self.root_dir = Path(root_dir)
        self.file_info = {}
        self.stats = {
            "total_files": 0,
            "total_size": 0,
            "by_extension": {},
            "by_type": {
                "code": 0,
                "config": 0,
                "documentation": 0,
                "test": 0,
                "other": 0
            }
        }
        
    def get_file_type(self, extension):
        """Dosya uzantısına göre türünü belirle"""
        code_extensions = {
            '.py', '.js', '.ts', '.jsx', '.tsx', '.java', '.cpp', '.c', '.h',
            '.go', '.rs', '.php', '.rb', '.swift', '.kt', '.scala', '.cs'
        }
        
        config_extensions = {
            '.json', '.yaml', '.yml', '.toml', '.ini', '.cfg', '.conf',
            '.env', '.properties', '.xml'
        }
        
        documentation_extensions = {
            '.md', '.txt', '.rst', '.pdf', '.doc', '.docx'
        }
        
        test_extensions = {
            '_test.py', '.spec.js', '.test.js', '.spec.ts', '.test.ts'
        }
        
        if extension in code_extensions:
            return "code"
        elif extension in config_extensions:
            return "config"
        elif extension in documentation_extensions:
            return "documentation"
        elif any(extension.endswith(ext) for ext in test_extensions):
            return "test"
        else:
            return "other"
    
    def calculate_file_hash(self, file_path):
        """Dosyanın MD5 hash'ini hesapla"""
        try:
            with open(file_path, 'rb') as f:
                file_hash = hashlib.md5()
                chunk = f.read(8192)
                while chunk:
                    file_hash.update(chunk)
                    chunk = f.read(8192)
                return file_hash.hexdigest()
        except Exception as e:
            return f"ERROR: {str(e)}"
    
    def scan_directory(self, directory=None, depth=0, max_depth=10):
        """Dizini tarayarak dosya bilgilerini topla"""
        if directory is None:
            directory = self.root_dir
        
        if depth > max_depth:
            return
        
        try:
            for item in directory.iterdir():
                if item.is_file():
                    # Dosya bilgilerini topla
                    try:
                        stat = item.stat()
                        size = stat.st_size
                        extension = item.suffix.lower()
                        file_type = self.get_file_type(extension)
                        
                        file_info = {
                            "path": str(item.relative_to(self.root_dir)),
                            "size": size,
                            "extension": extension,
                            "type": file_type,
                            "modified": datetime.fromtimestamp(stat.st_mtime).isoformat(),
                            "created": datetime.fromtimestamp(stat.st_ctime).isoformat(),
                            "hash": self.calculate_file_hash(item)
                        }
                        
                        self.file_info[str(item.relative_to(self.root_dir))] = file_info
                        
                        # İstatistikleri güncelle
                        self.stats["total_files"] += 1
                        self.stats["total_size"] += size
                        
                        # Uzantı istatistikleri
                        if extension in self.stats["by_extension"]:
                            self.stats["by_extension"][extension]["count"] += 1
                            self.stats["by_extension"][extension]["size"] += size
                        else:
                            self.stats["by_extension"][extension] = {
                                "count": 1,
                                "size": size
                            }
                        
                        # Tür istatistikleri
                        self.stats["by_type"][file_type] += 1
                        
                    except Exception as e:
                        print(f"⚠️  {item} okunurken hata: {e}")
                
                elif item.is_dir():
                    # .git dizinini atla
                    if item.name == '.git' or item.name == '__pycache__':
                        continue
                    
                    # Alt dizini tarayın
                    self.scan_directory(item, depth + 1, max_depth)
                    
        except PermissionError:
            print(f"⚠️  {directory} dizinine erişim izni yok")
        except Exception as e:
            print(f"⚠️  {directory} taranırken hata: {e}")
    
    def generate_report(self):
        """Detaylı rapor oluştur"""
        report = {
            "scan_date": datetime.now().isoformat(),
            "project_root": str(self.root_dir.absolute()),
            "stats": self.stats,
            "files": self.file_info,
            "analysis": {}
        }
        
        # Analiz ekle
        report["analysis"]["largest_files"] = sorted(
            self.file_info.items(),
            key=lambda x: x[1]["size"],
            reverse=True
        )[:10]
        
        report["analysis"]["recently_modified"] = sorted(
            self.file_info.items(),
            key=lambda x: x[1]["modified"],
            reverse=True
        )[:10]
        
        report["analysis"]["by_type_summary"] = {}
        for file_type, count in self.stats["by_type"].items():
            if count > 0:
                report["analysis"]["by_type_summary"][file_type] = {
                    "count": count,
                    "percentage": round((count / self.stats["total_files"]) * 100, 2)
                }
        
        return report
    
    def print_summary(self):
        """Konsola özet bilgi yazdır"""
        print("=" * 60)
        print("📁 PROJE DOSYA KONTROL RAPORU")
        print("=" * 60)
        print(f"📂 Proje Dizini: {self.root_dir.absolute()}")
        print(f"📅 Tarama Tarihi: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"📊 Toplam Dosya: {self.stats['total_files']}")
        print(f"💾 Toplam Boyut: {self.stats['total_size'] / 1024:.2f} KB")
        print()
        
        print("📈 DOSYA TÜRLERİNE GÖRE DAĞILIM:")
        for file_type, count in self.stats["by_type"].items():
            if count > 0:
                percentage = (count / self.stats["total_files"]) * 100
                print(f"  • {file_type.upper()}: {count} dosya (%{percentage:.1f})")
        
        print()
        print("🔤 UZANTILARA GÖRE DAĞILIM:")
        for ext, data in sorted(self.stats["by_extension"].items(), 
                               key=lambda x: x[1]["count"], reverse=True):
            print(f"  • {ext or '(uzantısız)'}: {data['count']} dosya")
        
        print()
        print("🏆 EN BÜYÜK 5 DOSYA:")
        largest_files = sorted(self.file_info.items(), 
                              key=lambda x: x[1]["size"], 
                              reverse=True)[:5]
        for path, info in largest_files:
            size_kb = info["size"] / 1024
            print(f"  • {path} - {size_kb:.2f} KB")
        
        print()
        print("🔄 SON GÜNCELLENEN 5 DOSYA:")
        recent_files = sorted(self.file_info.items(), 
                             key=lambda x: x[1]["modified"], 
                             reverse=True)[:5]
        for path, info in recent_files:
            mod_date = datetime.fromisoformat(info["modified"]).strftime("%d.%m.%Y %H:%M")
            print(f"  • {path} - {mod_date}")
        
        print("=" * 60)
    
    def save_report(self, output_file="project_analysis.json"):
        """Raporu JSON dosyasına kaydet"""
        report = self.generate_report()
        
        try:
            with open(output_file, 'w', encoding='utf-8') as f:
                json.dump(report, f, indent=2, ensure_ascii=False)
            print(f"✅ Rapor kaydedildi: {output_file}")
        except Exception as e:
            print(f"❌ Rapor kaydedilemedi: {e}")
    
    def check_critical_files(self):
        """Kritik dosyaların varlığını kontrol et"""
        critical_files = [
            "README.md",
            ".gitignore",
            "requirements.txt",
            "package.json",
            "Dockerfile",
            ".env.example"
        ]
        
        print("🔍 KRİTİK DOSYA KONTROLÜ:")
        print("-" * 40)
        
        missing_files = []
        for file in critical_files:
            file_path = self.root_dir / file
            if file_path.exists():
                print(f"✅ {file} - MEVCUT")
            else:
                print(f"❌ {file} - EKSİK")
                missing_files.append(file)
        
        if missing_files:
            print(f"\n⚠️  UYARI: {len(missing_files)} kritik dosya eksik!")
            print("Eksik dosyalar:", ", ".join(missing_files))
        else:
            print("\n🎉 Tüm kritik dosyalar mevcut!")
        
        print("-" * 40)

def main():
    """Ana fonksiyon"""
    print("🚀 DeepSeek ULTRA Enterprise Architect v4.0")
    print("📁 Proje Dosya Kontrol Sistemi Başlatılıyor...\n")
    
    # Kontrol edilecek dizin
    root_dir = Path(".")
    
    if not root_dir.exists():
        print(f"❌ Dizin bulunamadı: {root_dir}")
        sys.exit(1)
    
    # Kontrolcüyü oluştur
    checker = ProjectFileChecker(root_dir)
    
    # Dizini tara
    print("🔍 Proje dosyaları taranıyor...")
    checker.scan_directory()
    
    # Özeti göster
    checker.print_summary()
    
    # Kritik dosyaları kontrol et
    print()
    checker.check_critical_files()
    
    # Raporu kaydet
    print()
    checker.save_report()
    
    # HTML raporu da oluştur
    generate_html_report(checker)
    
    print("\n✅ Dosya kontrolü tamamlandı!")

def generate_html_report(checker):
    """HTML formatında rapor oluştur"""
    report = checker.generate_report()
    
    html_content = f"""
<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Proje Dosya Analizi Raporu</title>
    <style>
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            line-height: 1.6;
            color: #333;
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
            background-color: #f5f5f5;
        }}
        .header {{
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 30px;
            border-radius: 10px;
            margin-bottom: 30px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        }}
        .stats-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 20px;
            margin-bottom: 30px;
        }}
        .stat-card {{
            background: white;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            text-align: center;
        }}
        .stat-card h3 {{
            margin-top: 0;
            color: #667eea;
        }}
        .stat-number {{
            font-size: 2.5em;
            font-weight: bold;
            color: #764ba2;
            margin: 10px 0;
        }}
        .file-list {{
            background: white;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            margin-bottom: 20px;
        }}
        table {{
            width: 100%;
            border-collapse: collapse;
            margin-top: 20px;
        }}
        th, td {{
            padding: 12px;
            text-align: left;
            border-bottom: 1px solid #ddd;
        }}
        th {{
            background-color: #f8f9fa;
            font-weight: bold;
        }}
        tr:hover {{
            background-color: #f5f5f5;
        }}
        .badge {{
            display: inline-block;
            padding: 4px 8px;
            border-radius: 4px;
            font-size: 0.8em;
            font-weight: bold;
        }}
        .badge-code {{ background: #e3f2fd; color: #1976d2; }}
        .badge-config {{ background: #f3e5f5; color: #7b1fa2; }}
        .badge-doc {{ background: #e8f5e9; color: #388e3c; }}
        .badge-test {{ background: #fff3e0; color: #f57c00; }}
        .footer {{
            text-align: center;
            margin-top: 40px;
            padding: 20px;
            color: #666;
            font-size: 0.9em;
        }}
    </style>
</head>
<body>
    <div class="header">
        <h1>📁 Proje Dosya Analizi Raporu</h1>
        <p>DeepSeek ULTRA Enterprise Architect v4.0 tarafından oluşturuldu</p>
        <p>Tarama Tarihi: {report['scan_date']}</p>
        <p>Proje Dizini: {report['project_root']}</p>
    </div>
    
    <div class="stats-grid">
        <div class="stat-card">
            <h3>📊 Toplam Dosya</h3>
            <div class="stat-number">{report['stats']['total_files']}</div>
        </div>
        <div class="stat-card">
            <h3>💾 Toplam Boyut</h3>
            <div class="stat-number">{(report['stats']['total_size'] / 1024):.2f} KB</div>
        </div>
        <div class="stat-card">
            <h3>📅 Son Tarama</h3>
            <div class="stat-number">{datetime.fromisoformat(report['scan_date']).strftime('%d.%m.%Y')}</div>
        </div>
    </div>
    
    <div class="file-list">
        <h2>📈 Dosya Türleri Dağılımı</h2>
        <table>
            <thead>
                <tr>
                    <th>Tür</th>
                    <th>Dosya Sayısı</th>
                    <th>Yüzde</th>
                </tr>
            </thead>
            <tbody>
"""

    # Dosya türleri tablosu
    for file_type, data in report['analysis']['by_type_summary'].items():
        html_content += f"""
                <tr>
                    <td><span class="badge badge-{file_type}">{file_type.upper()}</span></td>
                    <td>{data['count']}</td>
                    <td>%{data['percentage']}</td>
                </tr>
"""

    html_content += """
            </tbody>
        </table>
    </div>
    
    <div class="file-list">
        <h2>🏆 En Büyük Dosyalar</h2>
        <table>
            <thead>
                <tr>
                    <th>Dosya</th>
                    <th>Boyut</th>
                    <th>Tür</th>
                    <th>Son Değişiklik</th>
                </tr>
            </thead>
            <tbody>
"""

    # En büyük dosyalar tablosu
    for path, info in report['analysis']['largest_files']:
        size_kb = info['size'] / 1024
        mod_date = datetime.fromisoformat(info['modified']).strftime('%d.%m.%Y %H:%M')
        html_content += f"""
                <tr>
                    <td>{path}</td>
                    <td>{size_kb:.2f} KB</td>
                    <td><span class="badge badge-{info['type']}">{info['type'].upper()}</span></td>
                    <td>{mod_date}</td>
                </tr>
"""

    html_content += """
            </tbody>
        </table>
    </div>
    
    <div class="file-list">
        <h2>🔄 Son Güncellenen Dosyalar</h2>
        <table>
            <thead>
                <tr>
                    <th>Dosya</th>
                    <th>Son Değişiklik</th>
                    <th>Boyut</th>
                    <th>Hash (MD5)</th>
                </tr>
            </thead>
            <tbody>
"""

    # Son güncellenen dosyalar tablosu
    for path, info in report['analysis']['recently_modified'][:10]:
        mod_date = datetime.fromisoformat(info['modified']).strftime('%d.%m.%Y %H:%M')
        size_kb = info['size'] / 1024
        html_content += f"""
                <tr>
                    <td>{path}</td>
                    <td>{mod_date}</td>
                    <td>{size_kb:.2f} KB</td>
                    <td><code>{info['hash'][:8]}...</code></td>
                </tr>
"""

    html_content += """
            </tbody>
        </table>
    </div>
    
    <div class="footer">
        <p>Generated by DeepSeek ULTRA Enterprise Architect v4.0</p>
        <p>© 2024 - Tüm hakları saklıdır</p>
    </div>
</body>
</html>
"""
    
    try:
        with open("project_analysis.html", "w", encoding="utf-8") as f:
            f.write(html_content)
        print("✅ HTML raporu oluşturuldu: project_analysis.html")
    except Exception as e:
        print(f"❌ HTML raporu oluşturulamadı: {e}")

if __name__ == "__main__":
    main()
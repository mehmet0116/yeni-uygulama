"""
Proje ayarları ve konfigürasyon dosyası.
Bu dosya, uygulama ayarlarını merkezi olarak yönetir.
"""

# Dosya yönetimi ayarları
DEFAULT_DIRECTORY = "./"
LOG_FILE = "file_operations.log"

# Uygulama ayarları
APP_NAME = "File Manager Pro"
VERSION = "1.0.0"
DEBUG = True

# Güvenlik ayarları
MAX_FILE_SIZE = 10485760  # 10MB
ALLOWED_EXTENSIONS = ['.txt', '.pdf', '.doc', '.jpg', '.png']
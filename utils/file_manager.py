"""
Dosya yönetimi için yardımcı fonksiyonlar.
Bu modül, dosya işlemlerini yönetmek için kullanılır.
"""

import os

def delete_file(file_path):
    """
    Belirtilen dosyayı siler.
    
    Args:
        file_path (str): Silinecek dosyanın yolu
        
    Returns:
        bool: Silme işlemi başarılı ise True, aksi halde False
    """
    try:
        if os.path.exists(file_path):
            os.remove(file_path)
            print(f"{file_path} dosyası başarıyla silindi.")
            return True
        else:
            print(f"{file_path} dosyası bulunamadı.")
            return False
    except Exception as e:
        print(f"Dosya silinirken hata oluştu: {e}")
        return False

def list_files(directory):
    """
    Belirtilen dizindeki dosyaları listeler.
    
    Args:
        directory (str): Listelenecek dizin yolu
        
    Returns:
        list: Dosya isimleri listesi
    """
    try:
        files = os.listdir(directory)
        return files
    except Exception as e:
        print(f"Dizin listelenirken hata oluştu: {e}")
        return []
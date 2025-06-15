# Project: WiFi Password Viewer

Berikut adalah proyek sederhana untuk melihat password WiFi yang terhubung dan yang pernah terhubung ke perangkat Anda menggunakan Python. Project ini akan bekerja di Windows.

## Struktur Project
```
wifi-password-viewer/
├── main.py
├── requirements.txt
└── README.md
```

## File 1: main.py
```python
import subprocess
import re
import os
from datetime import datetime

def get_wifi_profiles():
    try:
        # Mendapatkan daftar profil WiFi
        profiles_output = subprocess.run(['netsh', 'wlan', 'show', 'profiles'], 
                                       capture_output=True, text=True, check=True)
        profiles = re.findall(r':\s(.*?)\r', profiles_output.stdout)
        return profiles
    except subprocess.CalledProcessError as e:
        print(f"Error mendapatkan profil WiFi: {e}")
        return []

def get_wifi_password(profile_name):
    try:
        # Mendapatkan detail profil termasuk password
        profile_output = subprocess.run(['netsh', 'wlan', 'show', 'profile', 
                                       f'name="{profile_name}"', 'key=clear'], 
                                      capture_output=True, text=True, check=True)
        
        # Mencari password dalam output
        password_match = re.search(r'Key Content\s*:\s(.*?)\r', profile_output.stdout)
        password = password_match.group(1) if password_match else "No Password"
        
        # Mencari informasi koneksi terakhir
        auth_match = re.search(r'Authentication\s*:\s(.*?)\r', profile_output.stdout)
        auth = auth_match.group(1) if auth_match else "Unknown"
        
        return password, auth
    except subprocess.CalledProcessError as e:
        print(f"Error mendapatkan password untuk {profile_name}: {e}")
        return "Error", "Error"

def save_to_file(results):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"wifi_passwords_{timestamp}.txt"
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write("Daftar WiFi dan Password:\n")
        f.write("="*50 + "\n")
        for profile, password, auth in results:
            f.write(f"SSID: {profile}\n")
            f.write(f"Password: {password}\n")
            f.write(f"Authentication: {auth}\n")
            f.write("-"*50 + "\n")
    
    print(f"\nHasil telah disimpan ke {filename}")
    os.startfile(filename)  # Membuka file secara otomatis (Windows)

def main():
    print("WiFi Password Viewer")
    print("Mengambil daftar WiFi dan password...\n")
    
    profiles = get_wifi_profiles()
    results = []
    
    for profile in profiles:
        password, auth = get_wifi_password(profile)
        results.append((profile, password, auth))
        print(f"SSID: {profile}")
        print(f"Password: {password}")
        print(f"Authentication: {auth}")
        print("-"*50)
    
    save_to_file(results)

if __name__ == "__main__":
    main()
```

## File 2: requirements.txt
```
# Tidak ada dependency khusus karena menggunakan modul bawaan Python
```

## File 3: README.md
```markdown
# WiFi Password Viewer

Proyek sederhana untuk melihat password WiFi yang terhubung dan yang pernah terhubung ke perangkat Anda.

## Cara Menggunakan

1. Pastikan Anda menggunakan Windows
2. Jalankan script dengan Python 3:
   ```
   python main.py
   ```
3. Hasil akan ditampilkan di console dan disimpan dalam file teks

## Catatan

- Anda perlu menjalankan program ini sebagai Administrator untuk bisa melihat password WiFi
- Program ini hanya bekerja di Windows
- Hasil akan disimpan dalam file teks dengan timestamp di nama filenya
```

## Cara Menggunakan

1. Buat folder baru di VS Code
2. Buat ketiga file di atas
3. Buka terminal di VS Code dan jalankan:
   ```
   python main.py
   ```

## Catatan Penting

1. Anda harus menjalankan program ini sebagai Administrator untuk bisa mengakses password WiFi.
2. Program ini hanya bekerja di Windows karena menggunakan perintah `netsh` yang spesifik Windows.
3. Hasil akan otomatis disimpan dalam file teks dan dibuka setelah proses selesai.

Jika Anda ingin versi yang lebih aman atau untuk sistem operasi lain, perlu penyesuaian lebih lanjut.
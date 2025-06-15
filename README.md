# WiFi Password Recovery Tool - README

## 📝 Deskripsi
Tool ini memungkinkan Anda untuk melihat password WiFi yang tersimpan di komputer Windows dengan metode ekspor profil WiFi ke format XML dan membaca informasi sensitif yang tersimpan.

## 🛠 Fitur Utama
- Mengekstrak semua profil WiFi yang tersimpan
- Menampilkan detail autentikasi dan enkripsi
- Menampilkan password WiFi dalam format clear text (untuk jaringan personal)
- Bekerja bahkan ketika metode tradisional gagal

## ⚙️ Persyaratan Sistem
- Windows 10/11
- Python 3.x
- Hak akses Administrator

## 🚀 Cara Menggunakan

### Instalasi
1. Pastikan Python sudah terinstall:
   ```powershell
   python --version
   ```
2. Clone/salin file script ke komputer Anda

### Eksekusi Program
1. Buka Command Prompt/PowerShell sebagai Administrator
2. Navigasi ke folder script:
   ```powershell
   cd path\ke\folder\script
   ```
3. Jalankan program:
   ```powershell
   python wifi_password_recovery.py
   ```

### Output yang Dihasilkan
Program akan:
1. Membuat folder `wifi_exports` berisi file XML profil WiFi
2. Menampilkan daftar WiFi di console
3. Menyimpan hasil ekstraksi password dalam format teks

## 📂 Struktur File
```
project-folder/
├── wifi_password_recovery.py  # File script utama
├── wifi_exports/              # Folder hasil ekspor (terbentuk otomatis)
│   ├── Wi-Fi-Profil1.xml      # File XML profil WiFi
│   └── Wi-Fi-Profil2.xml
└── README.md                  # File ini
```

## ⚠️ Catatan Penting
1. Program HARUS dijalankan sebagai Administrator
2. Hanya bekerja untuk WiFi personal (WPA/WPA2-PSK)
3. Tidak bisa mengekstrak password WiFi enterprise (WPA-Enterprise)
4. Hasil mungkin "Tidak tersedia" untuk:
   - WiFi open network (tanpa password)
   - WiFi yang disetel tidak menyimpan password
   - WiFi enterprise

## 🔒 Keamanan
- Program hanya membaca data yang sudah tersimpan di sistem Anda
- Tidak mengirim data ke mana pun (berjalan lokal saja)
- File XML hasil ekspor mengandung informasi sensitif

## ❓ Troubleshooting
Jika program tidak bekerja:
1. Verifikasi running sebagai admin:
   ```powershell
   whoami /priv
   ```
2. Coba ekspor manual:
   ```powershell
   netsh wlan export profile name="NamaWiFi" folder="%USERPROFILE%\Desktop" key=clear
   ```
3. Pastikan adapter WiFi aktif

## 📜 Lisensi
Proyek ini open-source dan bebas digunakan untuk keperluan pribadi.

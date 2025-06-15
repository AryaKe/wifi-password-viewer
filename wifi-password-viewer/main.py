import os
import sys
import ctypes
import subprocess
import xml.etree.ElementTree as ET
from pathlib import Path

def run_as_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def get_wifi_profiles_alternative():
    """Metode alternatif untuk mendapatkan profil WiFi"""
    try:
        # Cek lokasi penyimpanan profil sistem
        wlan_profiles_dir = Path(os.environ['ProgramData']) / 'Microsoft' / 'Wlansvc' / 'Profiles' / 'Interfaces'
        
        if not wlan_profiles_dir.exists():
            print("Folder profil WiFi tidak ditemukan di lokasi standar")
            return None
            
        # Ekspor profil ke XML
        export_dir = Path.cwd() / "wifi_exports"
        export_dir.mkdir(exist_ok=True)
        
        cmd = f'netsh wlan export profile folder="{export_dir}" key=clear'
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        
        if result.returncode != 0:
            print("Gagal mengekspor profil WiFi:")
            print(result.stderr)
            return None
            
        return export_dir
        
    except Exception as e:
        print(f"Error dalam metode alternatif: {str(e)}")
        return None

def parse_xml_profiles(export_dir):
    """Parse file XML hasil ekspor"""
    profiles = []
    for xml_file in export_dir.glob("*.xml"):
        try:
            tree = ET.parse(xml_file)
            root = tree.getroot()
            
            ns = {'ns': 'http://www.microsoft.com/networking/WLAN/profile/v1'}
            
            profile = {
                'name': root.find('.//ns:name', ns).text,
                'auth': root.find('.//ns:authentication', ns).text,
                'encryption': root.find('.//ns:encryption', ns).text,
                'password': (root.find('.//ns:keyMaterial', ns).text 
                           if root.find('.//ns:keyMaterial', ns) is not None 
                           else "Tidak tersedia")
            }
            profiles.append(profile)
            
        except Exception as e:
            print(f"Gagal parsing {xml_file.name}: {str(e)}")
    
    return profiles

def main():
    if not run_as_admin():
        print("Program memerlukan hak administrator")
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
        sys.exit()
    
    print("=== WiFi Password Recovery Tool ===")
    print("Menggunakan metode alternatif...")
    
    export_dir = get_wifi_profiles_alternative()
    if not export_dir:
        print("Tidak dapat mengambil profil WiFi")
        input("Tekan Enter untuk keluar...")
        return
    
    profiles = parse_xml_profiles(export_dir)
    
    if not profiles:
        print("Tidak ada profil WiFi yang dapat dibaca")
    else:
        print("\nDaftar WiFi yang ditemukan:")
        for i, profile in enumerate(profiles, 1):
            print(f"\n{i}. {profile['name']}")
            print(f"   Authentication: {profile['auth']}")
            print(f"   Encryption: {profile['encryption']}")
            print(f"   Password: {profile['password']}")
    
    input("\nTekan Enter untuk keluar...")

if __name__ == "__main__":
    main()
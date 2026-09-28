import numpy as np
import requests

# 1) CSV dosyasını NumPy ile oku
#NumPy kullanarak CSV dosyasını oku. İlk satır başlık, diğer satırlar veri.
#Input: "data/characters.csv"
#Output: np.ndarray
def read_character_data(file_path: str):
    return np.genfromtxt(file_path, delimiter=',', dtype=str, skip_header=1)
    pass


# 2) Veri kümesinden eksik değerleri temizle
#None, boş string ("") veya "NaN" gibi eksik veri olan satırları çıkar.
# Input:
# [
#     ['Johnny', 'Rocker'],
#     ['V', None],
#     ['T-Bug', '']
# ]
# Output:
# [
#     ['Johnny', 'Rocker']
# ] 
def clean_missing_data(data: np.ndarray):
    temiz = []
    for satir in data:
        eksik = False
        for hucre in satir:
            if hucre is None or hucre == "" or hucre == "NaN":
                eksik = True
                break
        if not eksik:
            temiz.append(satir)
    return np.array(temiz)


# 3) Sadece belirli bir karakter sınıfına (örneğin "Netrunner") ait kayıtları döndür
#Belirtilen sınıfa sahip karakterleri getir.
#Input: 
# [
#     ['Johnny', 'Rocker'],
#     ['V', 'Solo'],
#     ['T-Bug', 'Netrunner']
# ], 'Netrunner'
#Output: [['T-Bug', 'Netrunner']]
def filter_by_class(data: np.ndarray, class_name: str):
    filtered_data = []
    for row in data:
        if row[1] == class_name:
            filtered_data.append(row)
    return np.array(filtered_data)
    pass


# 4) Karakter isimlerinden uzun olanları bul (örneğin 10 harften uzun)
# İsmi 10 harften uzun karakterleri bul.
# Input: 
# [
#     ['JohnnySilverhand', 'Rocker'],
#     ['V', 'Solo']
# ]
# Output: 
# ['JohnnySilverhand']
def get_long_names(data: np.ndarray):
    long_names = []
    for row in data:
        if len(row[0]) > 10:
            long_names.append(row[0])
    return long_names
    pass


# 5) İsimleri büyük harfe çevir ve yeniden döndür
# Tüm karakter isimlerini büyük harfe çevir (in-place ya da yeni dizi).
# Input: 
# [
#     ['v', 'Solo'],
#     ['t-bug', 'Netrunner']
# ]
# Output:
# [
#     ['V', 'Solo'],
#     ['T-BUG', 'Netrunner']
# ]
def uppercase_names(data: np.ndarray):
    uppercased_data = []
    for row in data:
        uppercased_row = [row[0].upper(), row[1]]
        uppercased_data.append(uppercased_row)
    return np.array(uppercased_data)
    pass

# 6) Sahte bir API'den karakter bilgilerini al
#Verilen URL'e GET isteği at ve response döndür.
#Kullanabileceğin örnel urller:
# https://dummyjson.com/users
# https://jsonplaceholder.typicode.com/users
# https://rickandmortyapi.com/api/character
# Output: requests.Response objesi (status_code + JSON data içeren)
def fetch_character_api_data(api_url: str):
    response = requests.get(api_url)
    return response
    pass


# 7) API yanıtının geçerli olup olmadığını kontrol et (status code 200 mü?)
# API yanıtı başarılı mı? (status code 200 mü?)
# Input: requests.Response
# Output: True ya da False
def validate_api_response(response: requests.Response):
    if response.status_code == 200:
        return True
    else:
        return False
    pass

# 8) API’den gelen JSON verisinden "name" alanlarını çek
# Amaç: JSON'dan name alanlarını bir listeye çıkar.
# Input:
# {
#   "users": [
#     {"id": 1, "name": "V"},
#     {"id": 2, "name": "Johnny"}
#   ]
# }
# Output: ['V', 'Johnny']
def extract_names_from_api(json_data: dict):
    isimler = []
    for kullanici in json_data["users"]:
        isimler.append(kullanici["name"])
    return isimler
    pass

# 9) Bir string içindeki özel karakterleri temizle (örneğin: %, $, ! vs.)
# String içindeki özel karakterleri temizle (sadece harf ve rakamlar kalsın)
# Input: "Hello@Cyber#punk!"
# Output: "HelloCyberpunk"
def clean_special_characters(s: str):
    return s.replace('@', '').replace('#', '').replace('!', '')
    pass

# 10) Dosyadan gelen verileri ve API'den gelenleri birleştir
# Amaç: Dosyadan gelen veriler ile API'den gelen name verilerini birleştirip liste olarak döndür.
# Input: 
# local_data = np.array([
#     ['Johnny', 'Rocker']
# ])
# api_names = ['V', 'T-Bug']
# Output: 
# [
#     ['Johnny', 'Rocker'],
#     ['V', 'API'],
#     ['T-Bug', 'API']
# ]
def merge_local_and_api_data(local_data: np.ndarray, api_names: list):
    merged_data = []
    for row in local_data:
        merged_data.append(row)
    for name in api_names:
        merged_data.append([name, 'API'])
    return np.array(merged_data)
    pass
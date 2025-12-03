# 🎵 Spotify İstatistik Arayüzü  

Spotify kullanım verilerini analiz edip **en çok dinlenen şarkıları ve sanatçıları görsel bir arayüzde** gösteren bir Python uygulamasıdır. Belirli tarihler arasında filtreleme yapabilir ve toplam dinleme sürelerini kolayca görebilirsiniz.  

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)

---

## 🚀 1️⃣ Sadece `.exe` Dosyasını Kullanmak İsteyenler İçin  

- Python kurulumu **gerekmez**.  
- Tek yapmanız gereken: `.exe` dosyasını bilgisayarınıza indirmek ve çalıştırmak.  

### 🎧 Spotify Veri Dosyasını Alma

1. Spotify hesabınıza gidin ve [Spotify Account → Privacy Settings](https://www.spotify.com/account/privacy/) kısmından **“Download your data / Download your Spotify history”** bölümünü bulun.  
2. İlgili yıllara ait **Streaming History JSON dosyalarını** indirin (ör. `StreamingHistory0.json`, `StreamingHistory1.json`, vb.).  
3. Tüm JSON dosyalarını **tek bir dosyada birleştirin** ve adını **`ozet.json`** olarak değiştirin.  
4. `ozet.json` dosyasını, `.exe` dosyasının bulunduğu **aynı klasöre** koyun.  

### 🖱 Kullanım

1. Başlangıç ve bitiş tarihlerini seçin  
2. “İstatistikleri Göster” butonuna tıklayın  
3. Çıktılar ekranda listelenecektir  

💡 Not: `.exe` dosyasını ilk açışta Windows güvenlik uyarısı gösterebilir, onay verdikten sonra çalışır.  

---

## 🛠 2️⃣ Açık Kaynak Python Kodunu İncelemek veya Geliştirmek İsteyenler İçin  

- Projenin Python kodları tamamen **açık kaynak** olarak paylaşılmıştır.  

### ⚙️ Gereksinimler

- Python 3.10+ veya 3.13  
- Gerekli paketler:  

```bash
pip install tkcalendar
python "Spotify özet.py"

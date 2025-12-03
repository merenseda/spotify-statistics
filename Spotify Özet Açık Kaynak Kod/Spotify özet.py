# -*- coding: utf-8 -*-
"""
Spotify İstatistik Arayüzü
@author: meren
"""

import json
from collections import defaultdict
from operator import itemgetter
import tkinter as tk
from tkinter import scrolledtext
from tkcalendar import DateEntry
from datetime import datetime

# JSON dosyasını oku
with open('ozet.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

def filter_data_by_date(start_date, end_date):
    """Verileri belirli tarihler arasında filtrele."""
    filtered = []
    for entry in data:
        played_at = entry.get('ts') or entry.get('played_at')
        if played_at:
            # datetime.date tipine çevirildi
            played_date = datetime.strptime(played_at[:10], "%Y-%m-%d").date()
            if start_date <= played_date <= end_date:
                filtered.append(entry)
    return filtered

def display_statistics():
    """İstatistikleri hesapla ve arayüzde göster."""
    start_date = start_date_picker.get_date()
    end_date = end_date_picker.get_date()
    filtered_data = filter_data_by_date(start_date, end_date)

    track_play_count = defaultdict(int)
    track_play_time = defaultdict(int)
    artist_play_count = defaultdict(int)
    artist_play_time = defaultdict(int)

    for entry in filtered_data:
        track = entry.get("master_metadata_track_name")
        artist = entry.get("master_metadata_album_artist_name")
        ms = entry.get("ms_played", 0)

        if track and artist:
            track_play_count[track] += 1
            track_play_time[track] += ms
            artist_play_count[artist] += 1
            artist_play_time[artist] += ms

    # Milisaniyeyi dakikaya çevir
    track_play_time = {k: v / 60000 for k, v in track_play_time.items()}
    artist_play_time = {k: v / 60000 for k, v in artist_play_time.items()}
    total_minutes = sum(track_play_time.values())

    # Arayüz çıktısını temizle
    output_text.delete("1.0", tk.END)

    # Sonuçları yaz
    output_text.insert(tk.END, "🔹 En Çok Dinlenen Şarkılar (oynatma sayısı):\n")
    for track, count in sorted(track_play_count.items(), key=itemgetter(1), reverse=True)[:10]:
        output_text.insert(tk.END, f"{track}: {count} kez\n")

    output_text.insert(tk.END, "\n🔹 En Çok Dinlenen Şarkılar (dakika):\n")
    for track, mins in sorted(track_play_time.items(), key=itemgetter(1), reverse=True)[:10]:
        output_text.insert(tk.END, f"{track}: {mins:.2f} dakika\n")

    output_text.insert(tk.END, "\n🔹 En Çok Dinlenen Sanatçılar (oynatma sayısı):\n")
    for artist, count in sorted(artist_play_count.items(), key=itemgetter(1), reverse=True)[:10]:
        output_text.insert(tk.END, f"{artist}: {count} kez\n")

    output_text.insert(tk.END, "\n🔹 En Çok Dinlenen Sanatçılar (dakika):\n")
    for artist, mins in sorted(artist_play_time.items(), key=itemgetter(1), reverse=True)[:10]:
        output_text.insert(tk.END, f"{artist}: {mins:.2f} dakika\n")

    output_text.insert(tk.END, f"\n⏱ Toplam Dinleme Süresi: {total_minutes:.2f} dakika\n")

# ------------------------------- #
#      TKINTER ARAYÜZÜ
# ------------------------------- #
window = tk.Tk()
window.title("Spotify İstatistikleri")
window.geometry("650x650")
window.config(bg="#f4f4f4")

# Tarih Etiketleri
tk.Label(window, text="Başlangıç Tarihi:", bg="#f4f4f4").grid(row=0, column=0, padx=5, pady=5)
start_date_picker = DateEntry(window, width=14, background='black', foreground='white', date_pattern='yyyy-mm-dd')
start_date_picker.grid(row=0, column=1, padx=5, pady=5)

tk.Label(window, text="Bitiş Tarihi:", bg="#f4f4f4").grid(row=1, column=0, padx=5, pady=5)
end_date_picker = DateEntry(window, width=14, background='black', foreground='white', date_pattern='yyyy-mm-dd')
end_date_picker.grid(row=1, column=1, padx=5, pady=5)

# Göster Butonu
tk.Button(window, text="İstatistikleri Göster", command=display_statistics).grid(row=2, column=0, columnspan=2, pady=10)

# Çıktı Alanı
output_text = scrolledtext.ScrolledText(window, width=80, height=25)
output_text.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

window.mainloop()

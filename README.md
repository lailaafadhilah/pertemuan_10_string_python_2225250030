# Pertemuan 10 - String dan Pengolahan Teks

Nama: Laila Fadhilah  
NIM: 2225250030  
Kelas: 3A

## Tujuan

Mengolah dan menormalisasi data teks dengan string Python, termasuk membersihkan spasi, mengubah kapitalisasi, menormalkan kode kelas, menghitung jumlah kata, dan membuat inisial nama.

## Cara Menjalankan

Jalankan latihan dengan perintah Python dari terminal VS Code. Contoh:

```bash
python latihan/01_dasar_string.py
python latihan/02_indeks_slicing.py
python latihan/03_method_string.py
python latihan/04_bersihkan_teks.py
python latihan/05_split_join.py
python latihan/06_pencarian_kata.py
python tugas/normalisasi_data_mahasiswa.py
```

Jika komputer menggunakan perintah `python3`, ganti `python` menjadi `python3`.

## Algoritma

1. Membaca nama lengkap dan kode kelas dari input.
2. Menghapus spasi berlebih pada awal dan akhir nama.
3. Memisahkan nama menjadi kata-kata untuk menghapus spasi berlebih di antara kata.
4. Mengubah nama ke format title case.
5. Mengubah kode kelas menjadi huruf besar dan menggabungkan setiap bagian dengan tanda hubung.
6. Menghitung jumlah kata pada nama yang telah dibersihkan.
7. Membuat inisial dari huruf pertama setiap kata nama.
8. Menampilkan nama bersih, kode kelas, jumlah kata, dan inisial.

Program menggunakan tiga fungsi agar setiap proses memiliki tugas yang jelas dan dapat digunakan kembali.

## Test Case

| No. | Input nama | Input kode kelas | Hasil yang diharapkan |
|---|---|---|---|
| 1 | aan hendrayana | pmat a 2026 | Aan Hendrayana; PMAT-A-2026; 2 kata; AH |
| 2 | fATHIYYAH mUTHMAINNAH | kelas b | Fathiyyah Muthmainnah; KELAS-B; 2 kata; FM |
| 3 | BUDI | pmtk 01 | Budi; PMTK-01; 1 kata; B |
| 4 | siti nur aisyah | kelas c | Siti Nur Aisyah; KELAS-C; 3 kata; SNA |


## Refleksi

Masalah yang ditemukan adalah data nama dan kode kelas memiliki spasi berlebih serta penggunaan huruf besar dan kecil yang tidak konsisten. Masalah ini diperbaiki dengan `strip()`, `split()`, `join()`, `title()`, dan `upper()`. Pengujian dilakukan menggunakan empat test case wajib untuk memastikan nama, kode kelas, jumlah kata, dan inisial sesuai.

## Sumber dan Bantuan

Bahan ajar Algoritma dan Pemrograman Pertemuan 10: String dan Pengolahan Teks dalam Python. Bantuan AI digunakan untuk membantu memahami materi, menyusun kode awal, dan menyiapkan test case. Kode diuji kembali dan hasil aktual diperiksa secara mandiri.
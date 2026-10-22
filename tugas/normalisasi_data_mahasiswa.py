def normalisasi_nama(nama):
    """Membersihkan spasi dan menyeragamkan format nama."""
    return " ".join(nama.strip().split()).title()


def buat_inisial(nama):
    """Membuat inisial dari setiap kata pada nama."""
    kata = normalisasi_nama(nama).split()
    return "".join(k[0] for k in kata)


def normalisasi_kode(kode):
    """Mengubah kode kelas menjadi huruf besar dan pemisah tanda hubung."""
    kata = kode.strip().upper().split()
    return "-".join(kata)


nama = input("Nama: ")
kode = input("Kode kelas: ")

nama_bersih = normalisasi_nama(nama)
kode_bersih = normalisasi_kode(kode)
jumlah_kata = len(nama_bersih.split())
inisial = buat_inisial(nama)

print("Nama bersih :", nama_bersih)
print("Kode kelas  :", kode_bersih)
print("Jumlah kata :", jumlah_kata)
print("Inisial     :", inisial)

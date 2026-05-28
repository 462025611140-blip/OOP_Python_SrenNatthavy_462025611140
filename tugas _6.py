

# 1. Base Class / Parent Teratas (A)
class Karyawan:
    def __init__(self, nama):
        self.nama = nama
        print(f"[Karyawan] Inisialisasi objek untuk {self.nama}")

    def bekerja(self):
        print(f"{self.nama} sedang melakukan pekerjaan umum perusahaan.")

# 2. Subclass Pertama / Turunan Kiri (B)
class Manajer(Karyawan):
    def __init__(self, nama, departemen):
        # super() akan meneruskan panggilan berdasarkan urutan MRO
        super().__init__(nama)
        self.departemen = departemen
        print(f"[Manajer] Inisialisasi bagian departemen: {self.departemen}")

    def bekerja(self):
        super().bekerja()  # Memanggil method milik Karyawan
        print(f"{self.nama} juga sedang mengelola tim di departemen {self.departemen}.")

# 3. Subclass Kedua / Turunan Kanan (C)
class Developer(Karyawan):
    def __init__(self, nama, bahasa_pemrograman):
        super().__init__(nama)
        self.bahasa_pemrograman = bahasa_pemrograman
        print(f"[Developer] Inisialisasi keahlian bahasa: {self.bahasa_pemrograman}")

    def bekerja(self):
        super().bekerja()  # Memanggil method milik Karyawan
        print(f"{self.nama} juga sedang menulis kode program menggunakan {self.bahasa_pemrograman}.")

# 4. Leaf Class / Turunan Paling Bawah (D) - Diamond Problem Terjadi di Sini
class TeamLead(Manajer, Developer):
    def __init__(self, nama, departemen, bahasa_pemrograman, jumlah_proyek):
        # super() di sini otomatis memanggil __init__ Manajer dan Developer secara teratur berkat MRO Python
        super().__init__(nama, departemen=departemen, bahasa_pemrograman=bahasa_pemrograman)
        self.jumlah_proyek = jumlah_proyek
        print(f"[TeamLead] Inisialisasi memimpin {self.jumlah_proyek} proyek sekaligus.")

    def bekerja(self):
        print(f"\n--- Alur Kerja {self.nama} (Sebagai Team Lead) dimulai ---")
        super().bekerja()  # Memanggil bekerja() milik Manajer dan Developer secara berurutan


# === SCRIPT UNTUK PENGUJIAN PROGRAM ===
if __name__ == "__main__":
    # Membuat objek dari kelas TeamLead yang mewarisi sifat Manajer dan Developer
    print("--- Proses Instansiasi Objek (Diamond Problem) ---")
    budi = TeamLead(nama="Budi", departemen="IT Dev", bahasa_pemrograman="Python", jumlah_proyek=3)
    
    # Menjalankan fungsi bekerja() untuk melihat efek penggunaan super()
    budi.bekerja()
    
    # Menampilkan urutan MRO (Method Resolution Order) untuk pembuktian teknis
    print("\n--- Urutan MRO Kelas TeamLead (Solusi Diamond Problem) ---")
    for urutan in TeamLead.__mro__:
        print(urutan)
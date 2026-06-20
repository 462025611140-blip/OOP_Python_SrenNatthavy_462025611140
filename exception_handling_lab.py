# =================================================================
# 2. Pembuatan Program (Custom Exception)
# =================================================================

# Membuat Custom Exception Class yang mewarisi dari kelas Exception bawaan Python
class SaldoMinimalError(Exception):
    """Exception yang dipicu jika penarikan melebihi batas saldo minimal."""
    def __init__(self, pesan="Penarikan gagal! Saldo Anda tidak mencukupi untuk mempertahankan batas minimal Rp50.000."):
        self.pesan = pesan
        super().__init__(self.pesan)


# Membuat Class Utama dengan logika validasi transaksi bank
class RekeningBank:
    def __init__(self, pemilik, saldo_awal):
        self.pemilik = pemilik
        self.saldo = saldo_awal
        self.BATAS_MINIMAL = 50000  # Aturan bisnis: Saldo mengendap minimal Rp50.000

    def tarik_tunai(self, jumlah):
        print(f"\n--- Memproses penarikan Rp{jumlah:,} untuk {self.pemilik} ---")
        
        # Menggunakan kata kunci 'raise' jika kondisi tidak memenuhi syarat
        if self.saldo - jumlah < self.BATAS_MINIMAL:
            raise SaldoMinimalError()
        
        # Jika lolos validasi, saldo berkurang
        self.saldo -= jumlah
        print(f"Penarikan Berhasil! Saldo saat ini: Rp{self.saldo:,}")


# =================================================================
# 3. Implementasi Try-Except-Finally
# =================================================================

if __name__ == "__main__":
    # Inisialisasi objek bank dengan saldo awal Rp150.000
    akun_budi = RekeningBank("Budi Santoso", 150000)

    # Membungkus pemanggilan metode di dalam blok try-except
    try:
        # Percobaan 1: Penarikan yang aman (Sisa saldo Rp70.000, di atas batas minimal)
        akun_budi.tarik_tunai(80000)
        
        # Percobaan 2: Penarikan yang memicu error (Sisa saldo akan menjadi Rp30.000, di bawah batas)
        akun_budi.tarik_tunai(40000)

    except SaldoMinimalError as error:
        # Menangani custom exception yang terjadi
        print(f"[ERROR TERDETEKSI] {error}")
    
    except Exception as general_error:
        # Mengantisipasi error tidak terduga lainnya
        print(f"[ERROR SYSTEM] Terjadi kesalahan: {general_error}")
        
    finally:
        # Blok yang akan selalu dijalankan
        print("Pesan: Proses pemeriksaan transaksi telah selesai dilakukan.")
        print(f"Informasi Terakhir - Saldo Akhir {akun_budi.pemilik}: Rp{akun_budi.saldo:,}\n")

# =======================================================
# Nama : Sren Natthavy
# Matkul: Pemrograman Berbasis Objek - Pertemuan 7
# =======================================================

# 1. PARENT CLASS
class Notifikasi:
    def __init__(self, penerima):
        self.penerima = penerima

    def kirim_pesan(self, isi_pesan):
        # Metode ini akan di-override oleh class anak
        pass

# 2. CHILD CLASS (Implementasi Method Overriding)
class EmailNotifikasi(Notifikasi):
    def kirim_pesan(self, isi_pesan):
        # Overriding metode kirim_pesan dengan logika spesifik Email
        print(f"[Email] Mengirim email ke {self.penerima}...")
        print(f"Isi: {isi_pesan}\n")

class SMSNotifikasi(Notifikasi):
    def kirim_pesan(self, isi_pesan):
        # Overriding metode kirim_pesan dengan logika spesifik SMS
        print(f"[SMS] Mengirim SMS ke nomor {self.penerima}...")
        print(f"Isi: {isi_pesan}\n")

# 3. INDEPENDENT CLASS (Untuk Demonstrasi Duck Typing)
class WhatsAppNotifikasi:
    def __init__(self, nomor_wa):
        self.nomor_wa = nomor_wa

    # Tidak mewarisi dari 'Notifikasi', tetapi memiliki nama metode yang sama
    def kirim_pesan(self, isi_pesan):
        print(f"[WhatsApp] Mengirim pesan WA ke {self.nomor_wa}...")
        print(f"Isi: {isi_pesan}\n")

# 4. FUNGSI MANDIRI (Menerapkan Prinsip Duck Typing)
def jalankan_pengiriman(objek_notifikasi, pesan):
    """
    Fungsi ini menerima objek apa saja, tanpa memedulikan tipe kelasnya.
    Selama objek tersebut memiliki metode 'kirim_pesan()', fungsi akan bekerja.
    """
    objek_notifikasi.kirim_pesan(pesan)

# 5. PENGUJIAN PROGRAM
if __name__ == "__main__":
    # Instansiasi objek dari kelas yang berbeda-beda
    notif_email = EmailNotifikasi("Natthavy@unida.com")
    notif_sms = SMSNotifikasi("081217522643")
    notif_wa = WhatsAppNotifikasi("0975295060") # Objek Duck Typing

    teks_pesan = "Halo! Ini adalah uji coba Polymorphism dan Duck Typing."

    print("--- OUTPUT TUGAS PERTEMUAN 7 ---\n")
    
    # Memanggil fungsi yang sama untuk objek yang berbeda-beda
    jalankan_pengiriman(notif_email, teks_pesan)
    jalankan_pengiriman(notif_sms, teks_pesan)
    jalankan_pengiriman(notif_wa, teks_pesan)

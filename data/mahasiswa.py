class Mahasiswa:
    def __init__(self, nim, nama, jurusan):
        self.nim = nim
        self.nama = nama
        self.jurusan = jurusan

    def __str__(self):
        return f"NIM: {self.nim}, Nama: {self.nama}, Jurusan: {self.jurusan}"


class DataMahasiswa:
    def __init__(self):
        self.data = []

    def tambah_mahasiswa(self, mahasiswa):
        self.data.append(mahasiswa)

    def hapus_mahasiswa(self, nim):
        self.data = [m for m in self.data if m.nim != nim]

    def ubah_mahasiswa(self, nim, nama_baru=None, jurusan_baru=None):
        for m in self.data:
            if m.nim == nim:
                if nama_baru:
                    m.nama = nama_baru
                if jurusan_baru:
                    m.jurusan = jurusan_baru

    def cari_mahasiswa(self, nim):
        for m in self.data:
            if m.nim == nim:
                return m
        return None

    def tampilkan_semua(self):
        return self.data
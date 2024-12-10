class ViewMahasiswa:
    @staticmethod
    def tampilkan_list(data_mahasiswa):
        if not data_mahasiswa:
            print("Data mahasiswa kosong.")
        else:
            for m in data_mahasiswa:
                print(m)

    @staticmethod
    def tampilkan_detail(mahasiswa):
        if mahasiswa:
            print(mahasiswa)
        else:
            print("Mahasiswa tidak ditemukan.")

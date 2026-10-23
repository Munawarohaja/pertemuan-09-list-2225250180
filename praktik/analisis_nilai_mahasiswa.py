def hitung_rata_rata(data):
    """Fungsi menghitung rata-rata nilai, aman untuk list kosong."""
    if len(data) == 0:
        return 0.0
    return sum(data) / len(data)

def saring_nilai_lulus(data, batas=60):
    """Fungsi menyaring dan mengembalikan list berisi nilai yang lulus."""
    hasil_lulus = []
    for nilai in data:
        if nilai >= batas:
            hasil_lulus.append(nilai)
    return hasil_lulus

def utama():
    # 1. Simpan minimal 10 nilai dalam sebuah list
    data_nilai = [78, 55, 90, 67, 60, 82, 45, 71, 88, 59]
    
    # 2. Pemrosesan Data
    total_mhs = len(data_nilai)
    total_nilai = sum(data_nilai)
    rata = hitung_rata_rata(data_nilai)
    nilai_min = min(data_nilai) if data_nilai else 0
    nilai_max = max(data_nilai) if data_nilai else 0
    
    list_lulus = saring_nilai_lulus(data_nilai, batas=60)
    jumlah_lulus = len(list_lulus)
    jumlah_belum_lulus = total_mhs - jumlah_lulus
    
    # 3. Tampilkan Hasil dengan Format Rapi
    print("==========================================")
    print("      RINGKASAN ANALISIS NILAI MAHASISWA   ")
    print("==========================================")
    print(f"Data Nilai Seluruhnya : {data_nilai}")
    print(f"Banyak Data           : {total_mhs}")
    print(f"Total Nilai           : {total_nilai}")
    print(f"Rata-rata Nilai       : {rata:.2f}")
    print(f"Nilai Minimum         : {nilai_min}")
    print(f"Nilai Maksimum        : {nilai_max}")
    print("------------------------------------------")
    print(f"Batas Kelulusan       : 60")
    print(f"Daftar Nilai Lulus    : {list_lulus}")
    print(f"Jumlah Mahasiswa Lulus: {jumlah_lulus}")
    print(f"Jumlah Belum Lulus    : {jumlah_belum_lulus}")
    print("==========================================")

if __name__ == "__main__":
    utama()
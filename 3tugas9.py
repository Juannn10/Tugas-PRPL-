# Nama = Juan Rezel Oktara Ramadhan
# Kelas = 1A
# NIM = 2403469

jam_mulai = int(input("Input mulai jam: "))
menit_mulai = int(input("Input mulai menit: "))
detik_mulai = int(input("Input mulai detik: "))

jam_selesai = int(input("Input selesai jam: "))
menit_selesai = int(input("Input selesai menit: "))
detik_selesai = int(input("Input selesai detik: "))

total_detik_mulai = (jam_mulai * 3600) + (menit_mulai * 60) + detik_mulai

total_detik_selesai = (jam_selesai * 3600) + (menit_selesai * 60) + detik_selesai

selisih_detik = total_detik_selesai - total_detik_mulai

jam = selisih_detik // 3600
sisa_detik = selisih_detik % 3600
menit = sisa_detik // 60
detik = sisa_detik % 60

print(f"Output: {jam} jam - {menit} menit - {detik} detik")
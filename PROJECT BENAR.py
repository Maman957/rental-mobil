no_plat = []
merk = []
tipe = []
subtotal = []
total = 0
kode_a = []
nama = []
no = []
jenis_kelamin = []
no_hp = []
alamat = []
tanggal = []
i = 0
daftar_mobil = (f"""
+--------------------------[RENTAL MOBIL AYEM TENTREM]------------------------------+
Daftar Mobil Tersedia	:
 +-----+------+------+------+------+------+------+------+------+------+------+------+
 | Kode Mobil |  Plat Nomor |  Merk Mobil |  Tipe Mobil | Per 24 Jam  | Per 12 Jam  |
 +-----+------+------+------+------+------+------+------+------+------+------+------+
 |   M-001    |   AB0101CE  |   Toyota    |  Yaris G-CV |   250000    |   150000    |
 |   M-002    |   AA1424DW  |   Toyota    | Hilux D Cap |   430000    |   230000    |
 |   M-003    |   AB4590QE  |   Suzuki    |   Karimun   |   220000    |   120000    |
 |   M-004    |   AD9057AC  |   Daihatsu  |   Terios    |   300000    |   170000    |
 +-----+------+------+------+------+------+------+------+------+------+------+------+
    """)
tambah = True
while (tambah == True):
	print("="*50)
	print(" SELAMAT DATANG DI RENTAL MOBIL AYEM TENTREM ")
	print("="*50)
	print("  1. Lihat Daftar Mobil")
	print("  2. Memasukkan Data Penyewa")
	print("  3. Memasukkan Data Penyewaan")
	print("  4. Melihat Nota Penyewaan")
	print("-"*50)
	
	kode = int(input("Masukkan kode yang ingin di akses : "))
	if (kode == 1):
		print(daftar_mobil)
	elif (kode == 2):
		print("Silahkan isi data penyewa	: ")
		kode_1 = input(" Kode Penyewa		: ")
		nama_1 = input(" Nama Penyewa		: ")
		no_1 = input(" Nomor Identitas	: ")
		jenis_kelamin_1 = input(" Jenis Kelamin		: ")
		no_hp_1 = input (" No Hp			: ")
		alamat_1 = input (" Alamat			: ")
		tanggal_1 =input (" Tanggal Sewa		: ")
		
		kode_a.append(kode_1)
		nama.append(nama_1)
		no.append(no_1)
		jenis_kelamin.append(jenis_kelamin_1)
		no_hp.append(no_hp_1)
		alamat.append(alamat_1)
		tanggal.append(tanggal_1)
		
		print("="*82)
		print(" Kode\t Nama Penyewa\t No Identitas\t Jenis Kelamin\t Nomor Hp\t Alamat\t")
		print("="*82)
		s = 0
		for kode_1 in kode_a:
			print(kode_a[s],"\t",nama[s],"\t",no[s],"\t",jenis_kelamin[s],"\t",no_hp[s],"\t",alamat[s],"\t")
			s += 1
		print("-"*82)
		
	elif(kode == 3):
		print(daftar_mobil)
		print("Silahkan isi data penyewaan	:")
		kode_2 = input(" Masukkan kode mobil	: ")
		sewa_2 = int(input(" Lama Sewa (12/24)	: "))

		if kode_2 == "M-001" :
			no_plat.append("AB0101CE")
			merk.append("Toyota")
			tipe.append("Yaris G-CV")
			if (sewa_2 == 12):
				subtotal.append(150000)
				total += (150000)
			else:
				subtotal.append(250000)
				total += (250000)
		elif kode_2 == "M-002" :
			no_plat.append("AA1424DW")
			merk.append("Toyota")
			tipe.append("Hilux D Cap ")
			if (sewa_2 == 12):
				subtotal.append(230000)
				total += (230000)
			else:
				subtotal.append(430000)
				total += (430000)
		elif kode_2 == "M-003" :
			no_plat.append("AB4590QE")
			merk.append("Suzuki")
			tipe.append("Karimun")
			if (sewa_2 == 12):
				subtotal.append(120000)
				total += (120000)
			else:
				subtotal.append(220000)
				total += (220000)
		elif kode_2 == "M-004" :
			no_plat.append("AD90057AC")
			merk.append("Daihatsu")
			tipe.append("Terios")
			if (sewa_2 == 12):
				subtotal.append(170000)
				total += (170000)
			else:
				subtotal.append(300000)
				total += (300000)
		else :
			print("  Kode mobil tidak ditemukan,masukkan dengan benar!\n")

	else: tambah = False
print("")
print("")
print("+-----------------[RENTAL MOBIL AYEM TENTREM]-------------------+")
print("")
print("Data Penyewa :")
print("="*65)
print("Kode \t Nama Penyewa\t No Identitas \t Tanggal Sewa")
print("="*65)
a = 0
for kode_1 in kode_a:
	print(kode_a[a],"\t",nama[a],"\t",no[a],"\t",tanggal[a])
	a += 1
print("-"*65)
print("")
print("Data Penyewaa Mobil : ")
print("+-------+-------+-------+-------+-------+-------+-------+-------+")
print("| Plat Nomor\t| Merk Mobil\t| Tipe Mobil\t| Subharga\t|")
print("+-------+-------+-------+-------+-------+-------+-------+-------+")
for plat in no_plat:
	print("|",no_plat[i],"\t|",merk[i],"\t|",tipe[i],"\t|",subtotal[i],"\t|")
	i += 1
print("+-------+-------+-------+-------+-------+-------+-------+-------+")
print("Jadi total biaya sewanya adalah		    : Rp.",total)
	



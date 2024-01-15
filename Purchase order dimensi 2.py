rincian_pembelian={
    '1':{"Nama_Material":"Kain katun", "Unit":"Roll", "Qty":300 , "Harga_Satuan":2100000},"\t"
    '2':{"Nama_Material":"Resleting ", "Unit":"Pcs ", "Qty":1100 , "Harga_Satuan":2000   },"\t"
    '3':{"Nama_Material":"Tali      ", "Unit":"M   ","Qty":3000, "Harga_Satuan":3000   },
    '4':{"Nama _Material":"Busa angin", "Unit":"M   ", "Qty":250 , "Harga_Satuan":10000  },
    '5':{"Nama_Material":"Benang    ", "Unit":"Roll", "Qty":10  , "Harga_Satuan":6000   },
    '6':{"Nama_Material":"Pita      ", "Unit":"Pcs ", "Qty":2000, "Harga_Satuan":2500   },
}

subtotal_harga1=rincian_pembelian['1']["Qty"]*rincian_pembelian['1']["Harga_Satuan"]
rincian_pembelian['1'].update({"Subtotal_Harga":subtotal_harga1})


subtotal_harga2=rincian_pembelian['2']["Qty"]*rincian_pembelian['2']["Harga_Satuan"]
rincian_pembelian['2'].update({"Subtotal_Harga":subtotal_harga2})


subtotal_harga3=rincian_pembelian['3']["Qty"]*rincian_pembelian['3']["Harga_Satuan"]
rincian_pembelian['3'].update({"Subtotal_Harga":subtotal_harga3})


subtotal_harga4=rincian_pembelian['4']["Qty"]*rincian_pembelian['4']["Harga_Satuan"]
rincian_pembelian['4'].update({"Subtotal_Harga":subtotal_harga4})


subtotal_harga5=rincian_pembelian['5']["Qty"]*rincian_pembelian['5']["Harga_Satuan"]
rincian_pembelian['5'].update({"Subtotal_Harga":subtotal_harga5})


subtotal_harga6=rincian_pembelian['6']["Qty"]*rincian_pembelian['6']["Harga_Satuan"]
rincian_pembelian['6'].update({"Subtotal_Harga":subtotal_harga6})

nama_vendor=input("Nama Order   : ")
alamat=input("Alamat       : ")
nomor_telepon=input("Nomor Telepon: ")
email=input("Email        : ")
kontak_person=input("Kontak Person: ")
no_order=input("No Order     : ")
tanggal_order=input("Tanggal Order: ")

print("==========================================================================================================================================")
print("Nama Order   : "+nama_vendor)
print("Alamat       : "+alamat)
print("Nomor Telepon: "+nomor_telepon)
print("Email        : "+email)
print("Kontak Person: "+kontak_person)
print("No Order     : "+no_order)
print("Tanggal Order: "+tanggal_order)
print("==========================================================================================================================================")

print(rincian_pembelian)

print("==========================================================================================================================================")
total_harga=(rincian_pembelian['1']['Subtotal_Harga']+rincian_pembelian['2']['Subtotal_Harga']+rincian_pembelian['3']['Subtotal_Harga']+rincian_pembelian['4']['Subtotal_Harga']+rincian_pembelian['5']['Subtotal_Harga']+rincian_pembelian['6']['Subtotal_Harga'])
print("Total Harga: ",total_harga)
ppn=(11/100*total_harga)
print("PPN        : ",ppn)
grand_total=(total_harga+ppn)
print("Grand Total: ",grand_total)
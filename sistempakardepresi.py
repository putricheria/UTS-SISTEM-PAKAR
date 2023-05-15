import numpy as np 
import pandas as pd 
from tabulate import tabulate

print('+---------------------------------------+')
print('|\tSelamat datang di sistem pakar\t|')
print('|\tTingkat Depresi pada remaja\t|')

diseases = [['C1','Gangguan mood'],
['C2','Depresi ringan'],
['C3','Depresi sedang'],
['C4','Depresi berat']
]

symptons=[
['A1',	'Sedih'],
['A2',	'Kelelahan melakukan aktivitas'],
['A3', 'kurang berkonsentrasi'],
['A4',	'Bosan atau jenuh'],
['A5',	'Sering melamun'],
['A6',	'Tidak bersemangat'],
['A7',	'Sering galau'],
['A8',	'Pesimis mengenai masa depan'],
['A9',	'Sering menangis dengan alasan yang tidak jelas'],
['A10',	'Mempunyai gangguan tidur atau insomnia'],
['A11',	'Sering cemas'],
['A12',	'Kecewa dengan diri sendiri'],
['A13',	'Terganggu dengan segala hal'],
['A14',	'Lebih sering terlihat murung'],
['A15',	'kehilangan minat dalam kegiatan atau hobi yang dulu disenangi'],
['A16',	'Kesepian'],
['A17',	'mempunyai perasaan bersalah'],
['A18',	'mempunyai perasaan dihukum'],
['A19',	'Mempunyai perasaan benci terhadap diri sendiri'],
['A20',	'Mudah tersinggung'],
['A21',	'Kehilangan selera makan'],
['A22',	'Khawatir tentang penampilan'],
['A23',	'sangat sensitive atau mudah marah terhadap orang disekitar'],
['A24',	'lebih suka menyendiri'],
['A25',	'mempunyai pikiran untuk bunuh diri'],
['A26',	'sulit mengambil keputusan'],
['A27',	'sulit melakukan kegiatan dengan baik'],
['A28',	'ada perubahan penambahan atau penurunan berat badan'],
['A29',	'Kurang percaya diri']

]

patient_symp = []

#menu 1
def show_symptoms():
    dataframes =  pd.DataFrame(symptons)
    diseases_table = tabulate(dataframes, headers=['Kode Gejala','Nama gejala'],
                    tablefmt = 'fancy_grid', numalign='left')

    print(diseases_table)
    main()
#menu 2
def add_symptoms():
    for i in range(len(symptons)):
        symptomp = input ('Masukkan kode gejala yang anda alami :')
        patient_symp.append (symptomp)
        choice = input('Apakah ada gejala lain? Y/N ')
        if choice =='N'or choice == 'n':
            break
    main()
#menu 3
def show_pt_symptoms():
    if not patient_symp:
        print('Silahkan masukkan gejala terlebih dahulu')
        main()
    else: 
        patient_symp.sort()
        dataframes = pd.DataFrame(patient_symp)
        diseases_table = tabulate(dataframes, headers=['Kode gejala'], 
                                  tablefmt = 'fancy_grid', numalign='left')

        print(diseases_table)
        choice = input('Adakah gejala lain yang belum anda sebutkan? Y/N ')
        if choice == 'Y' or choice == 'y':
            add_symptoms()
        else:
            main()
#menu 4
def diagnose(sy):
    if not sy:
        print('Silahkan masukkan gejala terlebih dahulu!')
        main()
    else:
        sy.sort()
        if sy[0] == 'G1' and sy[1] == 'G2' and sy[2] == 'G3' and sy[3] == 'G4' and sy[4] == 'G5' and sy[5] == 'G7':
            return diseases[0]
        elif sy[0] == 'G1' and sy[1] == 'G2' and sy[2] == 'G6' and sy[3] == 'G8' and sy[4] == 'G10' and sy[5] == 'G11' and sy[6] == 'G14' and sy[7] == 'G15' and sy[8] == 'G16' and sy[9] == 'G22':
            return diseases[1]
        elif sy[0] == 'G1' and sy[1] == 'G9' and sy[2] == 'G10' and sy[3] == 'G11' and sy[4] == 'G12' and sy[5] == 'G13' and sy[6] == 'G16' and sy[7] == 'G17' and sy[8] == 'G20' and sy[9] == 'G22' and sy[10] == 'G23' and sy[11] == 'G27':
            return diseases[2]
        elif sy[0] == 'G1' and sy[1] == 'G9' and sy[2] == 'G10' and sy[3] == 'G12' and sy[4] == 'G13' and sy[5] == 'G16' and sy[6] == 'G18' and sy[7] == 'G19' and sy[8] == 'G20' and sy[9] == 'G21' and sy[10] == 'G24' and sy[11] == 'G25' and sy[12] == 'G26' and sy[13] == 'G27' and sy[14] == 'G28' and sy[15] == 'G29':
            return diseases[3]
        

def main():
    print('+---------------------------------------+')
    print('silahkan pilih menu dibawah :')
    print('1. Tampilkan daftar gejala')
    print('2. Masukkan gejala yang dialami')
    print('3. Tampilkan kode gejala yang dialami')
    print('4. Tampilkan diagnosa')
    print('5. keluar')
    choice = int(input('Masukkan pilihan : '))
    print('------------------------------')
    if choice == 1:
        show_symptoms()
    elif choice == 2:
        add_symptoms()
    elif choice == 3:
        show_pt_symptoms()
    elif choice == 4:
        disease = diagnose(patient_symp)
        print('Anda mengalami : ',disease[1])
        patient_symp.clear()
        main() 
    elif choice == 5:
        exit()
        print('+---------------------------------------+')    

main()
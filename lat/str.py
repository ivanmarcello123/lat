 
text= "python"
a,b,c,d,e,f= text
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
buah = ['apel','mangga']
buah1,buah2=buah
print(buah1)
print(buah2)


huruf_pertama=text[0]
print(huruf_pertama)

# slicing string
print('slicing string:')
kalimat = 'belajar pemrograman python sangat menyenangkan'
x = kalimat[0:3]
print(x)
print(kalimat[0:3])
print(kalimat[3:7])
print(kalimat[-3]) 
print(kalimat[::2])


print('string concatention:')
x='UBM'
y=' is the best'
z= x+''+y+str(10000)
print(z)
print(x+''+y)

print('mengukur panjang string')


print("modifikasi string:")
teks2="belajar pemrograman python"
print(teks2.capitalize())
print(teks2.upper())
print(teks2.lower())



print("replace string:")
teks2='belajar,pemrograman,python'
print(teks2.replace('python','dasar'))

print("split string:")
print(teks2.split())


print("join string:")
buah = ["apel","mangga","melon","pepaya"]
hasil='|'.join(buah)
print(hasil)


print("find and count string:")
paragraf='''Korupsi merupakan salah satu masalah besar yang menghambat kemajuan sosial, ekonomi, dan politik di Indonesia.
 Tindak pidana korupsi mencakup berbagai bentuk penyalahgunaan kekuasaan dan sumber daya negara untuk kepentingan pribadi atau kelompok tertentu,
   seperti pemotongan anggaran negara, suap, penggelapan dana, hingga manipulasi kebijakan. 
   Meskipun Indonesia telah berkomitmen untuk memberantas korupsi melalui berbagai lembaga seperti Komisi Pemberantasan Korupsi (KPK), 
   masalah ini tetap menjadi tantangan besar.'''
hasil_cari=paragraf.find("Indonesia")
print(hasil_cari)
#memanggil file gempa dan import semua method/fungsi
from gempa import *

#mebuat objek gempa dg argumen
gempa1 = gempa("banten", 1.2)
gempa2 = gempa("palu", 6.1)
gempa3 = gempa("cianjur", 5.6)
gempa4 = gempa("jayapura", 3.3)
gempa5 = gempa("garut", 4.0)

#informasi gempa
print("## info gempa maseh ##")
print()
gempa1.dampak()

print()
print("## info gempa maseh ##")
print()
gempa2.dampak()

print()
print("## info gempa maseh ##")
print()
gempa3.dampak()

print()
print("## info gempa maseh ##")
print()
gempa4.dampak()

print()
print("## info gempa maseh ##")
print()
gempa5.dampak()

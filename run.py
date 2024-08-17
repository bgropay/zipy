# program untuk meng-crack kata sandi file zip
#
# perhatian
#
# program ini dibuat hanya untuk tujuan edukasi dan
# pembelajaran saja. jangan gunakan program ini untuk
# tujuan yang tidak sah (ilegal).
#
# - dibuat oleh @ropay menggunakan python 3
#

import os
import time
import pyzipper

print("""+-------------------------------------+
| Program : Crack kata sandi File ZIP |
| Pembuat : Ropay                     |
| Githib  : github.com/bgropay/zipy   |
+-------------------------------------+""")

while True:
        try:
                file_zip = input("[?] File ZIP: ")
                if not os.path.isfile(file_zip):
                        print(f"[-] File ZIP '{file_zip}' tidak ditemukan.")
                        continue
                else:
                        if not file_zip.endswith(".zip"):
                                print(f"[-] File '{file_zip}' bukan file ZIP.")
                                continue
                        else:
                                print(f"[+] File ZIP '{file_zip}' ditemukan.")
                                break
        except KeyboardInterrupt:
                print("[*] Keluar dari program...")
                time.sleep(3)
                exit()

while True:
        try:
                wordlist = input("[?] Wordlist: ")
                if not os.path.isfile(wordlist):
                        print(f"[-] Wordlist '{wordlisy}' tidak ditemukan.")
                        continue
                else:
                        print(f"[+] Wordlist '{wordlist}' ditemukan.")
                        with open(wordlist, encoding="latin-1", errors="ignore") as w:
                                daftar_kata_sandi = w.read().splitlines()
                        break
        except KeyboardInterrupt:
                print("[*] Keluar dari program...")
                time.sleep(3)
                exit()
print("-"*39)
try:
        for kata_sandi in daftar_kata_sandi:
                time.sleep(0.5)
                try:
                        print(f"[*] Mencoba kata sandi: {kata_sandi}")
                        with pyzipper.AESZipFile(file_zip) as fz:
                                fz.pwd = kata_sandi.encode("latin-1")
                                crack = fz.testzip()
                                if crack is None:
                                        print("-"*39)
                                        print(f"[+] Kata sandi ditemukan: {kata_sandi}")
                                        print("-"*39)
                                        exit()
                except Exception:
                        continue
        print("[-] Kata sandi tidak ditemukan.")
except KeyboardInterrupt:
        print("[*] Keluar dari program...")
        time.sleep(3)
        exit()

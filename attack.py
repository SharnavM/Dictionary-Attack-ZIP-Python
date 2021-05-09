from tqdm import tqdm
import pyzipper

isFound = False
file = "0.jpg"    #Replace this with a file name inside your zip

def printName(zipFile):
    with pyzipper.AESZipFile(zipFile) as f:
        for name in f.namelist():
            print(name)

def attack(zipFile, wordList):
    total = len(list(open(wordList, "rb")))
    print("Total passwords to test:- ", total)
    print("\n")
    with pyzipper.AESZipFile(zipFile) as f:
        with open(wordList, "rb") as wordList:
            for word in tqdm(wordList, total=total, unit="word"):
                password = word.decode().strip()
                try:
                    f.extract(file, pwd=password.encode('utf-8'))
                except:
                    continue
                else:
                    isFound = True
                    break
            if isFound:
                print("\n[*] Password Found:- ",word.decode().strip())
            else:
                print("\n[!] Password not Found")


attack("test.zip", "rockyou.txt")

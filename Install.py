import os

print("Установка библиотек")
os.system("pip3 install --upgrade pip")
bib = ["requests", "termcolor", "fake_useragent", "progress", "beautifulsoup4", "datetime"]
for i in range(len(bib)):
    print("Установка "+bib[i]+"...\033[0m")
    os.system("pip3 install "+bib[i])
os.system('cls' if os.name == 'nt' else 'clear')
print("Установка завершена!")
print("\nНажмите Enter чтобы закрыть")
input()
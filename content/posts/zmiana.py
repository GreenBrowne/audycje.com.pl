import os

# Ścieżka do katalogu z plikami md
directory = 'C:\\Users\\srcj\\Desktop\\audycje.com.pl\\content\\posts\\'

# Fragmenty do zamiany
old_fragment = 'https://audycje.com.pl/posts/wsparcieee/'
new_fragment = 'https://audycje.com.pl/posts/wsparcie/'

# Lista do przechowywania nazw zmienionych plików
changed_files = []

# Przejdź przez wszystkie pliki w katalogu
for filename in os.listdir(directory):
    if filename.endswith('.md'):
        file_path = os.path.join(directory, filename)
        
        # Otwórz plik i czytaj jego zawartość
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # Zamień stary fragment na nowy
        new_content = content.replace(old_fragment, new_fragment)
        
        # Zapisz plik z powrotem
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(new_content)

        # Dodaj nazwę pliku do listy zmienionych plików
        changed_files.append(filename)

# Wypisz listę zmienionych plików
if changed_files:
    print("Zmienione pliki:")
    for changed_file in changed_files:
        print(changed_file)
else:
    print("Żadne pliki nie zostały zmienione.")      

print("Zamiana zakończona!")
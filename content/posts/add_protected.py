import os

def add_protected_line():
    # Pobranie bieżącego katalogu roboczego
    directory = os.getcwd()
    
    # Iteracja przez pliki w katalogu
    for filename in os.listdir(directory):
        # Sprawdzenie, czy plik ma rozszerzenie .md
        if filename.endswith('.md'):
            file_path = os.path.join(directory, filename)
            
            # Odczyt zawartości pliku z kodowaniem UTF-8
            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    lines = file.readlines()
            except UnicodeDecodeError:
                print(f"Nie można odczytać pliku {file_path} z kodowaniem UTF-8.")
                continue

            # Sprawdzenie, czy pierwsza linia zaczyna się od ---
            if lines and lines[0].strip() == '---':
                # Dodanie linii 'protected: true' po pierwszej linii
                new_lines = [lines[0]]  # Pierwsza linia (---)
                new_lines.append('protected: true\n')  # Dodanie 'protected: true'
                
                # Dodanie pozostałych linii
                new_lines.extend(lines[1:])
            else:
                # Jeśli nie ma `---` na początku, dodaj `protected: true` na początku
                new_lines = ['protected: true\n'] + lines

            # Zapisanie zmienionej zawartości do pliku
            try:
                with open(file_path, 'w', encoding='utf-8') as file:
                    file.writelines(new_lines)
            except UnicodeEncodeError:
                print(f"Nie można zapisać pliku {file_path} z kodowaniem UTF-8.")

# Uruchomienie funkcji
add_protected_line()

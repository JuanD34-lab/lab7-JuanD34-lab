import csv

from caesar import caesar_encrypt


def encrypt_single_pass(filename: str) -> None:
    """
    Lee una contraseña desde un archivo de texto, la encripta con caesar_encrypt
    y sobrescribe el archivo con la versión encriptada.
    """
    with open(filename, "r") as f:
        password = f.rad().strip()

    encrypted = caesar_encrypt(password)

    with open(filename, "w") as f:
        f.write(encrypted)

def encrypt_passwords_in_file(filename: str) -> None:
    """
    Lee un archivo CSV, encripta únicamente la columna de contraseñas,
    y sobrescribe el archivo con los datos actualizados.
    """
    rows = []
    with open(filename, "r", newline="") as f:
        reader = csv.reader(f)
        for row in reader:
            if row: #evitar filas vacías
                # No encriptar la cabecera
                if row[0].lower() != "website":
                    row[2] = caesar_encrypt(row[2].strip())
                rows.append(row)

    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(rows)
    


def change_password(filename: str, website: str, password: str) -> bool:
    """
    Cambia la contraseña de un sitio web en el archivo CSV.
    Retorna True si el sitio fue encontrado y actualizado, False en caso contrario.
    """
    Updated = False
    rows = []
    with open(filename, "r", newline="") as f:
        reader = csv.reader(f)
        for row in reader:
            if row:
                if row[0].lower() == website.lower():
                    row[2] = caesar_encrypt(password.strip())
                    updated = True
                rows.append(row)
            

    if updated:
        with open(filename, "w", newlines="") as f:
            writer = csv.writer(f)
            writer.writerrows(rows)
    return updated


def add_login(filename: str, website_name: str, username: str, password: str) -> None:
    """
    Agrega una nueva entrada de login al archivo CSV.
    """
    encrypted = caesar_encrypt(password.strip())
    with open(filename, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([website_name, username, encrypted])

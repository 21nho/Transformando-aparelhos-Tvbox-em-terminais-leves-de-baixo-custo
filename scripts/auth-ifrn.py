#!/usr/bin/python3

import ssl
import urllib.parse
import urllib.request
from getpass import getpass

def getint(message: str) -> int:
    while True:
        try:
            matricula = int(input(message))
            break
        except ValueError:
            print("A matrícula deve ter apenas dígitos!")
    return matricula

def main() -> None:
    matricula = getint("Digite sua matrícula: ")
    senha = getpass("Digite sua senha: ")

    body_data = urllib.parse.urlencode(
        {"escapeUser": matricula, "user": matricula, "passwd": senha, "ok": "Login"}
    ).encode("ascii")

    ssl_config = ssl.create_default_context()
    ssl_config.check_hostname = False
    ssl_config.verify_mode = ssl.CERT_NONE

    with urllib.request.urlopen(
        "https://autenticacao-cnat.ifrn.local:6082/php/uid.php?vsys=1&rule=0",
        data=body_data,
        context=ssl_config,
    ) as response:
        if "User Authenticated" in response.read().decode("utf-8"):
            print("Usuário autenticado com sucesso!")
        else:
            print("A autenticação falhou!")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nFinalizado pelo usuário!")

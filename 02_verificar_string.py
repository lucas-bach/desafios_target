import re

def contar_letra_a(texto: str) -> int:
    return len(re.findall(r"a", texto, re.IGNORECASE))

def obter_entrada_usuario(mensagem: str, default: str) -> str:
    entrada = input(mensagem).strip()
    return entrada if entrada else default

def main():
    string_predefinida = "a"
    texto = obter_entrada_usuario("Por favor, digite um texto:(ou pressione enter para usar o texto predefinido) ", string_predefinida)

    
    try:
        total_a = contar_letra_a(texto)

        if total_a > 0:
            print(f"O texto {texto} tem {total_a} 'a'.")
        else:
            print(f"O texto {texto} não tem 'a'.")

    except ValueError:
        print(f"O texto {texto} tem {total_a} 'a'.")

if __name__ == "__main__":
    main()
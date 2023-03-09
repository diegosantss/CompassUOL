import hashlib 

while True:
    string = input("Digite uma string gerar seu hash ou digite 'exit' para sair:\n")
    if string == 'exit':
        break
    #transforma a string para o encode 'uft-8'
    string_encode = hashlib.sha1(string.encode('utf-8'))
    #exibe o hash da string  com a função hexdigest
    string_hash = string_encode.hexdigest()
    print(f'O hash da string {string} é: {string_hash}')
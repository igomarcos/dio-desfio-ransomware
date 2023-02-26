import os
import pyaes

## abrindo o arquivo criptografado

file_name = 'alvo.txt.malvadao'
file = open(file_name, 'rb')
file_data = file.read()
file.close()

## chave para descriptografar

key = b"testeransomwares"
aes = pyaes.AESModeOfOperationCTR(key)
decrypt_data = aes.decrypt(file_data)

## remove o arquivo criptografado

os.remove(file_name)

## criando um novoa rquivo descriptografado

new_file = 'alvo.txt'
new_file = open(f'{new_file}', "wb")
new_file.write(decrypt_data)
new_file.close()


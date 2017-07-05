# retorna True se s contém somente letras
s = 'Hello'
print(s, s.isalpha())
s = 'Hello!'
print(s, s.isalpha())
#retorna True se s contém somente dígitos.

s = '1234'
print(s, s.isdigit())
s = 'G1234!'
print(s, s.isdigit())

#lower retorna a versão de s com todas as letras minúsculas.
upper retorna a versão de s com todas as letras maiúsculas.
: s = 'Olimpíadas'
minusculas = s.lower()
maiusculas = s.upper()
print(minusculas)
print(maiusculas)
print(s)


s = 'Olimpíadas'
print(s.find('a'))
print(s.find('X'))


letra = input('Entre uma letra: ')
if letra.lower() in ('a', 'e', 'i', 'o', 'u'):
print(letra, 'é uma vogal')
else:
print(letra, 'não é uma vogal')


email = input('Forneça um endereço de email: ')
indice = email.find('@')
username = email[0:indice]
dominio = email[indice+1:len(email)]
print('Username:', username)
print('Domínio:', dominio)

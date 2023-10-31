nome=input('Digite seu nome:')
cpf=int(input('Digite seu CPF:'))
data=int(input('Data de nascimento:'))
genero=input('Gênero:')
nacionalidade=input('Nacionalidade:')
n1=int(input('CEP:'))
n2=input('Escolaridade:')
n3=input('Nome do responsàvel:')
n4=int(input('Número de telefone:'))
n5=int(input('Número do responsàvel:'))
print(f""" 
\033[1;35:43mCadastro para o curso: 
\033[0;31m Nome: {nome}  
\033[0;32m CPF:{cpf}   
\033[0;36m Data d'nasc:{data}
\033[0;37m Gênero: {genero}
\033[0;33m Nacionalidade: {nacionalidade}
\033[0;34m CEP: {n1} 
\033[0;36m Escolaridade:{n2}
\033[0;33m Responsàvel:{n3}
\033[0;30m Número de telefone:{n4}
\033[0;35m Número do responsàvel:{n5}
      """)

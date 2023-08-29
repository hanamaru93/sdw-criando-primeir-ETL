import pandas as pd
import json
import random
import secrets as sc

#Esse ETL captura os dados do csv que contem os jogadores da NBA e organiza com nome, 
#sobrenome e data de nascimento gerando um arquivo .txt de saída

print("Esse ETL captura os dados do csv que contem os jogadores da NBA e organiza com nome, sobrenome e data de nascimento gerando um arquivo .txt de saída")
input('Tecle Enter para continuar...')

df = pd.read_csv('players.csv');
jogadores_nba = df
numero_de_serie = sc.token_hex(random.randint(10, 10))

def registros_gerais():
    _lista_jogadores = "\nNome: "+df['fname']+" "+df['lname'] +"\nData de Nascimento: " +df['birthday'] + "\n"
    arquivo = open(f'jogadores-{numero_de_serie}.txt', 'x')
    for jogador in  _lista_jogadores:

        arquivo.write(f'{jogador}')
        print(jogador)
    return 'OK'

     

registros_gerais()

print(f'nome do arquivo: jogadores-{numero_de_serie}.txt')

#arquivo_de_saida = open()


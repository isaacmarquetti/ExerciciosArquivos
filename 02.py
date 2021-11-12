"""
A ACME Inc., uma empresa de 500 funcionários, está tendo problemas
de espaço em disco no seu servidor de arquivos.
Para tentar resolver este problema, o Administrador de Rede precisa
saber qual o espaço ocupado pelos usuários, e identificar os
usuários com maior espaço ocupado. Através de um programa, baixado
da Internet, ele conseguiu gerar o seguinte arquivo, chamado
"usuarios.txt":

alexandre       456123789
anderson        1245698456
antonio         123456456
carlos          91257581
cesar           987458
rosemary        789456125

Neste arquivo, o nome do usuário possui 15 caracteres. A partir
deste arquivo, você deve criar um programa que gere um relatório,
chamado "relatório.txt", no seguinte formato:

ACME Inc.               Uso do espaço em disco pelos usuários
------------------------------------------------------------------------
Nr.  Usuário        Espaço utilizado     % do uso

1    alexandre       434,99 MB             16,85%
2    anderson       1187,99 MB             46,02%
3    antonio         117,73 MB              4,56%
4    carlos           87,03 MB              3,37%
5    cesar             0,94 MB              0,04%
6    rosemary        752,88 MB             29,16%

Espaço total ocupado: 2581,57 MB
Espaço médio ocupado: 430,26 MB

O arquivo de entrada deve ser lido uma única vez, e os dados
armazenados em memória, caso sejam necessários, de forma a
agilizar a execução do programa. A conversão da espaço ocupado
em disco, de bytes para megabytes deverá ser feita através de
uma função separada, que será chamada pelo programa principal.
O cálculo do percentual de uso também deverá ser feito através
de uma função, que será chamada pelo programa principal.
"""


def conversor_mb(n):
    return n * 0.00000095367432


def porcentagem_mb(n, total):
    return (n / total) * 100


relatorio = {}
dados = []
somar_dados = 0
media_dados = 0
qtde = 0

with open('c:/temp/usuarios.txt', 'r') as arquivo:
    for linha in arquivo:
        cadastro = linha.strip()
        relatorio['nome'] = linha[:15].strip()
        relatorio['tamanho'] = conversor_mb(int(linha[16:].strip()))
        dados.append(relatorio.copy())

    for dado in dados:
        qtde += 1
        somar_dados += dado['tamanho']

    media_dados = somar_dados / qtde

    for dado in dados:
        dado['porcentagem'] = porcentagem_mb(dado['tamanho'], somar_dados)

with open('c:/temp/relatorio.txt', 'w') as arquivo:

    arquivo.writelines(f"ACME Inc.               Uso do espaço em disco pelos usuários\n")
    arquivo.writelines(f"------------------------------------------------------------------------\n")
    arquivo.writelines(f"Nr.   Usuário        Espaço utilizado     % do uso\n")
    arquivo.writelines('\n')

    for v, dado in enumerate(dados):
        arquivo.writelines(f"{v+1:<5} {dado['nome']:<12}{dado['tamanho']:>10.2f} MB{dado['porcentagem']:>18.2f}%\n")

    arquivo.writelines('\n')
    arquivo.writelines(f'Espaço total ocupado: {somar_dados:.2f} MB\n')
    arquivo.writelines(f'Espaço médio ocupado: {media_dados:.2f} MB\n')
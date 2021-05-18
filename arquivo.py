import csv, os

def abre_log(file='access.log'):
    for linha in open(file):
        yield linha, linha.upper()


def abre_csv(file='caso_full.csv'):
    for linha in open(file):
        yield linha


def busca_leme(file='caso_full.csv'):
    for linha in open(file):
        if 'Leme' in linha:
            yield linha


def separa_candidaturas(file):
    read = abre_csv(file)
    while True:
        try:
            linha = next(read).replace('\n', '').split(',')
            ano = linha[0]
            if ano == 'ano_eleicao':
                header = linha
            else:
                filename = f'Arquivos/eleicoes_{ano}.csv'

                # Create file with header
                if not os.path.exists(filename):
                    print('New File ', ano)
                    with open(filename, 'w', newline='') as csv_w:
                        csv_writer = csv.writer(csv_w, delimiter=';')
                        csv_writer.writerow(header)

                # Append lines in file
                with open(filename, 'a', newline='') as csv_a:
                    csv_writer = csv.writer(csv_a, delimiter=';')
                    csv_writer.writerow(linha)

        except StopIteration:
            del read
            break

# candidaturas = open(, encoding='utf8')
separa_candidaturas('candidatura.csv')
arquivo_carregado_em_memoria = open('caso_full.csv').read()
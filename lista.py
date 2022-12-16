# alunos: Ana Denicoli e Julio Cesar
#função: programa que utiliza vetores e exibe quantos caracteres possui o nome digitado pelo usuário

lista = []

for x in range (0,5):
    a = str(input('Digite um nome: '))
    lista.append(a)
    print(f'tem :', len(a))
def escolhaop():
    print("**************************************")
    print("* 1 --> preço do produto pós imposto *")
    print("* 2 -->  horário em formato PM/AM    *")
    print("* 3 -->  sair do programa            *")
    print("**************************************")
    op = int(input("Digite opcao deseja: "))
    if op ==1:
        somaImposto()
    elif op ==2:
        saida()
    elif op ==3:
        sair()
    elif op != 1 or 2 or 3:
        escolhaop()

def somaImposto():
    custo=float(input("\nInforme o custo do produto: "))
    taxaImposto= float(input("Informe a taxa de imposto sobe o produto: "))
    custo_imposto=(taxaImposto/100)*custo
    valor_final=custo_imposto + custo
    print(str(valor_final))
    return escolhaop()
def convercao():
    horas=int(input("Informe as horas: "))
    minutos=int(input("Informe os minutos: "))
    if horas>12: 
        novo_horario=horas-12
        print("{}".format(novo_horario), ":",minutos, "PM")
    else:
        print("{}".format(horas), ":",minutos, "AM")
    return escolhaop()
def saida():
    print(convercao())
def sair():
    print("* Fim do programa. Até mais! *")

escolhaop()

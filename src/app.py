import sys

gastos = []

def adicionar(valor, descricao):
    if valor < 0:
        raise ValueError("Valor não pode ser negativo")
    gastos.append({"valor": valor, "descricao": descricao})

def listar():
    return gastos

def total():
    return sum(g["valor"] for g in gastos)

def main():
    if len(sys.argv) < 2:
        print("Uso: add/list/total")
        return

    comando = sys.argv[1]

    if comando == "add":
        valor = float(sys.argv[2])
        descricao = sys.argv[3]
        adicionar(valor, descricao)
        print("Gasto adicionado")

    elif comando == "list":
        for g in listar():
            print(g)

    elif comando == "total":
        print(total())

if __name__ == "__main__":
    main()
import os

class Produto:
    def __init__(self, id, nome, unidade, quantidade, descricao):
        self.id = id
        self.nome = nome
        self.unidade = unidade
        self.quantidade = quantidade
        self.descricao = descricao

    def __str__(self):
        return f"ID: {self.id}, Nome: {self.nome}, Unidade: {self.unidade}, Quantidade: {self.quantidade}, Descrição: {self.descricao}"

class ListaDeCompras:
    def __init__(self):
        self.produtos = []
        self.proximo_id = 1

    def adicionar_produto(self, nome, unidade, quantidade, descricao):
        produto = Produto(self.proximo_id, nome, unidade, quantidade, descricao)
        self.produtos.append(produto)
        self.proximo_id += 1
        return produto

    def remover_produto(self, id):
        for produto in self.produtos:
            if produto.id == id:
                self.produtos.remove(produto)
                return produto
        return None

    def pesquisar_produtos(self, nome):
        resultados = [produto for produto in self.produtos if nome.lower() in produto.nome.lower()]
        return resultados

    def listar_produtos(self):
        return self.produtos

def mostrar_menu():
    print("\n1. Adicionar produto")
    print("2. Remover produto")
    print("3. Pesquisar produtos")
    print("4. Sair do programa")
    print()

def obter_unidade():
    unidades = ["Quilograma", "Grama", "Litro", "Mililitro", "Unidade", "Metro", "Centímetro"]
    print("Escolha a unidade de medida:")
    for i, unidade in enumerate(unidades, start=1):
        print(f"{i}. {unidade}")
    escolha = int(input("Digite o número correspondente à unidade de medida: "))
    if 1 <= escolha <= len(unidades):
        return unidades[escolha - 1]
    else:
        print("Escolha inválida.")
        return obter_unidade()

def cabecalho():
    print("=" * 50)
    print("Bem-vindo à Lista de Compras Simples!")
    print("=" * 50)

def main():
    lista = ListaDeCompras()
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        cabecalho()
        produtos = lista.listar_produtos()
        if produtos:
            print("Produtos na lista:")
            for produto in produtos:
                print(produto)
        else:
            print("Nenhum produto na lista.")
        mostrar_menu()
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            nome = input("Nome do produto: ")
            unidade = obter_unidade()
            quantidade = input("Quantidade: ")
            descricao = input("Descrição: ")
            produto = lista.adicionar_produto(nome, unidade, quantidade, descricao)
            print(f"Produto adicionado: {produto}")
        elif escolha == '2':
            id = int(input("ID do produto a ser removido: "))
            produto = lista.remover_produto(id)
            if produto:
                print(f"Produto removido: {produto}")
            else:
                print("Produto não encontrado.")
        elif escolha == '3':
            nome = input("Digite o nome do produto para pesquisa: ")
            resultados = lista.pesquisar_produtos(nome)
            if resultados:
                print(f"{len(resultados)} produto(s) encontrado(s):")
                for produto in resultados:
                    print(produto)
            else:
                print("Nenhum produto encontrado.")
        elif escolha == '4':
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida.")

        input("Pressione Enter para continuar...")

if __name__ == "__main__":
    main()
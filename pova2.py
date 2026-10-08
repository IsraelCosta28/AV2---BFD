class Documento:
    def __init__(self, titulo, conteudo, tipo):
        
        self.__titulo = titulo
        self.__conteudo = conteudo
        self.__tipo = tipo

    
    def get_titulo(self):
        return self.__titulo

    def get_conteudo(self):
        return self.__conteudo

    def get_tipo(self):
        return self.__tipo


class Impressora:
  
    def imprimir(self, documento: Documento):
        print("\n" + "="*40)
        print("          IMPRESSÃO INICIADA")
        print("="*40)
        print(f"Tipo: {documento.get_tipo().upper()}")
        print(f"Título: {documento.get_titulo()}")
        print("-" * 40)
        print(documento.get_conteudo())
        print("="*40)
        print("          IMPRESSÃO CONCLUÍDA")
        print("="*40 + "\n")


def menu():
    
    minha_impressora = Impressora()
    
    
    documentos = []

    while True:
        print("--- MENU DA IMPRESSORA ---")
        print("1 - Criar novo documento")
        print("2 - Imprimir um documento")
        print("3 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            print("\n-- Novo Documento --")
            titulo = input("Digite o título: ")
            tipo = input("Digite o tipo (ex: relatório, carta, artigo): ")
            conteudo = input("Digite o conteúdo do documento:\n")
            
            
            novo_doc = Documento(titulo, conteudo, tipo)
            documentos.append(novo_doc)
            print("Documento criado com sucesso!\n")

        elif opcao == '2':
            if len(documentos) == 0:
                print("\nNenhum documento na fila para imprimir. Crie um primeiro!\n")
            else:
                print("\n-- Documentos Disponíveis --")
                for i, doc in enumerate(documentos):
                    
                    print(f"[{i}] {doc.get_titulo()} ({doc.get_tipo()})")
                
                escolha = input("Digite o número do documento que deseja imprimir: ")
                
                
                if escolha.isdigit() and 0 <= int(escolha) < len(documentos):
                    doc_selecionado = documentos[int(escolha)]
                    minha_impressora.imprimir(doc_selecionado)
                else:
                    print("Opção inválida!\n")

        elif opcao == '3':
            print("Desligando impressora...")
            break
        
        else:
            print("Opção inválida, tente novamente.\n")


if __name__ == "__main__":
    menu()

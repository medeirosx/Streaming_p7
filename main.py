class StreamingSystem:
    def __init__(self):
        self.catalog = {
            'Filmes': ['Os Três Patetas', 'Vingadores', '007', 'Avatar' , 'De Volta para o Futuro' ],
            'Séries': ['Mr Robot', 'Lost', 'Prison Break', 'Stranger Things', 'Game of Thrones']
        }

    def show_catalog(self):
        print("Catálogo de Streaming:")
        for category, titles in self.catalog.items():
            print(f"\n{category}:")
            for title in titles:
                print(title)

    def play_video(self, video):
        print(f"Reproduzindo: {video}")


def main():
    system = StreamingSystem()
    while True:
        print("\nBem-vindo ao Sistema de Streaming!")
        print("Escolha uma opção:")
        print("1. Visualizar Catálogo")
        print("2. Sair")
        option = input("Opção: ")

        if option == '1':
            system.show_catalog()
            category = input("\nEscolha uma categoria (Filmes/Séries): ")
            if category in system.catalog.keys():
                title = input("Escolha um título: ")
                if title in system.catalog[category]:
                    print("\nIniciando reprodução...")
                    system.play_video(title)
                else:
                    print("Título não encontrado.")
            else:
                print("Categoria não encontrada.")
        elif option == '2':
            print("Saindo do Sistema de Streaming...")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
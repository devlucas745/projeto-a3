# Sistema simples de biblioteca

class Livro:
    def __init__(self, titulo, autor, data_publicacao):
        self.titulo = titulo
        self.autor = autor
        self.data_publicacao = data_publicacao

    def __str__(self):
        return f"📘 '{self.titulo}' — {self.autor} ({self.data_publicacao})"


class Biblioteca:
    def __init__(self):
        self.livros = []

    def adicionar_livro(self, livro):
        self.livros.append(livro)
        print(f"✅ Livro '{livro.titulo}' adicionado com sucesso!")

    def listar_livros(self):
        if not self.livros:
            print("📚 Nenhum livro na biblioteca ainda.")
        else:
            print("\nLista de livros na biblioteca:")
            for livro in self.livros:
                print(livro)


# Exemplo de uso
if __name__ == "__main__":
    biblioteca = Biblioteca()

    # Adicionando livros
    livro1 = Livro("Dom Casmurro", "Machado de Assis", 1899)
    livro2 = Livro("1984", "George Orwell", 1949)
    livro3 = Livro("O Pequeno Príncipe", "Antoine de Saint-Exupéry", 1943)

    biblioteca.adicionar_livro(livro1)
    biblioteca.adicionar_livro(livro2)
    biblioteca.adicionar_livro(livro3)

    # Listando livros
    biblioteca.listar_livros()

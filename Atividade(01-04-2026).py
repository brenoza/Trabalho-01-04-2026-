catalogo = {}
emprestimosativos = {}
historico = []


def adicionarLivro(codigo, titulo, autor, quantidade):
    if codigo in catalogo:
        print(f"Erro: Livro com código {codigo} já existe")
        return False

    catalogo[codigo] = {
        "titulo": titulo,
        "autor": autor,
        "quantidade": quantidade
    }

    print(f"Livro '{titulo}' adicionado com sucesso")
    return True



def emprestarLivro(codigo, nome_usuario):
    if codigo not in catalogo:
        print("Livro não encontrado")
        return False

    if catalogo[codigo]["quantidade"] <= 0:
        print("Livro indisponível")
        return False

    catalogo[codigo]["quantidade"] -= 1
    emprestimosativos[codigo] = nome_usuario

    print(f"Livro emprestado para {nome_usuario}")
    return True



def devolverLivro(codigo):
    if codigo in emprestimosativos:
        usuario = emprestimosativos[codigo]

        catalogo[codigo]["quantidade"] += 1
        historico.append((codigo, usuario, "devolvido"))

        del emprestimosativos[codigo]

        print(f"Livro devolvido com sucesso por {usuario} ✅")
        return True
    else:
        print("Esse livro não está emprestado ❌")
        return False



adicionarLivro("L001", "Codigo Limpo", "Robert Martin", 2)
emprestarLivro("L001", "João")
devolverLivro("L001")
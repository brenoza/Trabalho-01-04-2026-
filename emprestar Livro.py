def emprestar_livro(codigo, nome_aluno):

    if codigo not in catalogo:
        print(f"Erro: Livro com codigo {codigo} não encontrado!")
        return False

    if catalogo[codigo]["quantidade"] <= 0:
        print(f"Erro: '{catalogo[codigo]['titulo']}' não está disponivel!")
        return False

    livros_do_aluno = conta_livros_aluno(nome_aluno)
    if livros_do_aluno >= 2:
        print(f"Erro: {nome_aluno} já pegou 2 livros (limite máximo)!")
        return False
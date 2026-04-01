def devolve_livro(codigo, nome_aluno):

    if codigo not in emprestimoAtivo or nome_aluno not in emprestimoAtivo[codigo]:
        print(f"Erro: {nome_aluno} não pegou este livro")
        return False

emprestimoAtivo[codigo].remove(nome_aluno)

catalogo[codigo]["quantidade"] += 1

historico.append({
"tipo": "devolução",
"codigo": codigo,
"titulo": catalogo[codigo]["titulo"],
"aluno": nome_aluno
})

print(f"{nome_aluno} devolveu '{catalogo['titulo']}' com sucesso!")
return True

def conta_livros_aluno(nome_aluno):

def conta_livros_aluno(nome_aluno):

    contador = 0

for codigo, alunos in emprestimoAtivo.item():

    if nome_aluno in alunos:
        contador += 1

return contador

dfe lista_emprestimos():

print("\n" + "="*60)
print("LIVROS EMPRESTADOS NO MOMENTO")
print("="*60)

if not emprestimoAtivo:
    print("Nenhum livro emprestado.")
    return

for codigo, alunos in emprestimoAtivo.items ():
    titulo = catalogo[codigo]["titulo"]
    print(f"\n {titulo}({codigo})")

    for aluno in alunos:
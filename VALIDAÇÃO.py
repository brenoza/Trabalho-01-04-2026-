if codigo in emprestimoAtivo and nome_aluno in emprestimoAtivo[codigo]:
    print(f"Erro: {nome_aluno} já pegou este lívro!")
    return False

if codigo not in emprestimoAtivo:
    emprestimoAtivo[codigog] = []

emprestimoAtivo[codigo].append(nome_aluno)

catalogo[codigo]["quantidade"] -= 1

historico.append({
"tipo": "emprestimo",
"codigo": codigo,
"titulo": catalogo[codigo]["titulo"],
"aluno": nome_aluno
})

print(f"{nome_aluno} pegou '{catalogo[codigo]['titulo']}' com sucesso!")
return True 
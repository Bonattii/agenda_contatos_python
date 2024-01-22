def adicionar_contato(contatos, nome_novo_contato, telefone_novo_contato, email_novo_contato):
  contato = {
    "nome": nome_novo_contato,
    "telefone": telefone_novo_contato,
    "email": email_novo_contato,
    "favorito": False
  }
  contatos.append(contato)
  print(f"Contato {nome_novo_contato} adicionado com sucesso!")
  return

def ver_contatos(contatos):
  print("\nLista de contatos:")
  for indice, contato in enumerate(contatos, start=1):
    nome_contato = contato["nome"]
    telefone_contato = contato["telefone"]
    email_contato = contato["email"]
    print(f"{indice}. {nome_contato} - {telefone_contato} - {email_contato}")
  return

contatos = []

while True:
  print("\nAgenda de contatos:")
  print("1. Salvar um novo contato")
  print("2. Visualizar lista de contatos")
  print("3. Editar um contato")
  print("4. Marcar/desmarcar um contato como favorito")
  print("5. Visualizar lista de contatos favoritos")
  print("6. Deletar um contato")
  print("7. Sair")

  escolha = input("Digite sua escolha: ")

  if escolha == "1":
    nome_novo_contato = input("Digite o nome do contato: ")
    telefone_novo_contato = input("Digite o telefone do contato: ")
    email_novo_contato = input("Digite o email do contato: ")
    adicionar_contato(contatos, nome_novo_contato, telefone_novo_contato, email_novo_contato)
  elif escolha == "2":
    ver_contatos(contatos)
  elif escolha == "7":
    break

  print("Programa finalizado.")

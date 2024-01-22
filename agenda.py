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
    status = "✓" if contato["favorito"] else " "
    nome_contato = contato["nome"]
    telefone_contato = contato["telefone"]
    email_contato = contato["email"]
    print(f"{indice}. {nome_contato} - {telefone_contato} - {email_contato} - favorito[{status}]")
  return

def atualizar_contato(contatos, indice_contato, novo_nome_contato, novo_telefone_contato, novo_email_contato):
  indice_contato_ajustado = int(indice_contato) - 1
  if indice_contato_ajustado >= 0 and indice_contato_ajustado < len(contatos):
    contato = contatos[indice_contato_ajustado]
    contato["nome"] = novo_nome_contato
    contato["telefone"] = novo_telefone_contato
    contato["email"] = novo_email_contato
    print("Contato atualizado com sucesso!")
  else:
    print("Contato não encontrado.")
  return

def toggle_favorite(contatos, indice_contato):
  indice_contato_ajustado = int(indice_contato) - 1
  if indice_contato_ajustado >= 0 and indice_contato_ajustado < len(contatos):
    contato = contatos[indice_contato_ajustado]
    contato["favorito"] = not contato["favorito"]
    print("Contato atualizado com sucesso!")
  else:
    print("Contato não encontrado.")
  return

def ver_contatos_favoritos(contatos):
  print("\nLista de contatos favoritos:")
  for indice, contato in enumerate(contatos, start=1):
    if contato["favorito"]:
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
  elif escolha == "3":
    ver_contatos(contatos)
    indice_contato = input("Digite o numero do contato que deseja editar: ")
    novo_nome_contato = input("Digite o novo nome do contato: ")
    novo_telefone_contato = input("Digite o novo telefone do contato: ")
    novo_email_contato = input("Digite o novo email do contato: ")
    atualizar_contato(contatos, indice_contato, novo_nome_contato, novo_telefone_contato, novo_email_contato)
  elif escolha == "4":
    ver_contatos(contatos)
    indice_contato = input("Digite o numero do contato que deseja marcar/desmarcar como favorito: ")
    toggle_favorite(contatos, indice_contato)
  elif escolha == "5":
    ver_contatos_favoritos(contatos)
  elif escolha == "7":
    print("Programa finalizado.")
    break

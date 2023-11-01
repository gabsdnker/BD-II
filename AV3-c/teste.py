import mysql.connector

conecta = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="gabi"
)

opcao = ""

while opcao != 0:
    print("Opções:")
    print("0- Sair")
    print("1- Inserir")
    print("2- Modificar")
    print("3- Remover")
    print()

    opcao = int(input("Escolha a opção: "))

    if opcao == 1:
        cursor = conecta.cursor()

        nome = input("Informe o nome: ")
        idade = input("Informe a idade: ")

        sql = "INSERT INTO faculdade (nome, idade) VALUES (%s, %s)"
        val = (nome, idade)
        cursor.execute(sql,val)

        print("Dados inseridos com sucesso!")
        print()

        conecta.commit()
        conecta.close()

    elif opcao == 2:
        cursor = conecta.cursor()
        nome = input("Informe o nome do usuário a ser atualizado: ")

        novo_nome = input("Informe o novo nome: ")
        nova_idade = input("Informe a nova idade: ")

        sql = ("UPDATE faculdade SET nome = %s, idade = %s WHERE nome = %s")
        val = (novo_nome, nova_idade, nome)
        cursor.execute(sql, val)

        if cursor.rowcount > 0:
            print("Os dados foram atualizados com sucesso!")
            print()
        else:
            print("Nenhum registro encontrado para atualizar.")
            print()

        conecta.commit()
        conecta.close()

    elif opcao == 3:
        cursor = conecta.cursor()

        nome = input("Informe o nome do usuário a ser removido: ")

        sql = "DELETE FROM faculdade WHERE nome = %s"
        val = (nome,)
        cursor.execute(sql, val)

        conecta.commit()

        if cursor.rowcount > 0:
            print(f"Registros de {nome} removidos")
            print()
        else:
            print(f"Nenhum registro encontrado com o nome {nome}")
            print()

        conecta.close()

    else:
        if opcao == 0:
            print("Saindo...")
        else:
            print("ERRO! Selecione uma opção válida.")
            print()

    
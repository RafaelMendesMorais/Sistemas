import json
import os

ARQUIVO_JSON = "chamados.json"


def carregar_chamados():
    if os.path.exists(ARQUIVO_JSON):  # ve se o caminho (path) exist
        with open(ARQUIVO_JSON, "r") as file: # vai ler o arquivo, ou seja abre em modo de leitura o arquivo
            return json.load(file) # le oar arquivo e transforma em um objeto de pythom
    return []

def salvar_chamados(chamados):
    with open(ARQUIVO_JSON, "w") as file:
        json.dump(chamados, file, indent=4)

def cadastrar_chamado():
    chamados = carregar_chamados()
    id_chamado = len(chamados) + 1
    descricao = input("Digite a descrição do seu problema: ")
    prioridade = int(input("Digite a prioridade (1-5): "))
    chamado = {"id": id_chamado, "descrição": descricao, "prioridade": prioridade}
    chamados.append(chamado) 
    salvar_chamados(chamados)
    print("Chamado cadastrado com sucesso!")

def buscar_chamado():
    chamados = carregar_chamados()
    termo = input("Digite o ID ou termo da descrição: ")
    for chamado in chamados:
        if str(chamado["id"]) == termo or termo.lower() in chamado["descrição"].lower(): #verifica se o ID do chamado é igual ao termo ou se o termo, o o lower coloca  todas como minusculas
            print(chamado)

def remover_chamado(): 
    chamados = carregar_chamados()
    id_remover = int(input("Digite o ID do chamado a remover: "))
    chamados = [c for c in chamados if c["id"] != id_remover] # vai excluir o chamado com o id escolhido, e vai criar uma nova(ja sem o excluido)
    salvar_chamados(chamados)
    print("chamado salvo com sucesso")

def listar_chamados():
    chamados = carregar_chamados()
    chamados.sort(key=lambda x: x["prioridade"], reverse=True) #ordena a lista chamados em ordem decrescente ligada com a chave ali(prioriade)
    for chamado in chamados:
        print(chamado)

def estatisticas():
    chamados = carregar_chamados()
    print(f"Total de chamados: {len(chamados)}")
    if chamados:
        media_prioridade = sum(c["prioridade"] for c in chamados) / len(chamados) # vai calcular a média das prioridades
        print(f"Prioridade média: {media_prioridade:.2f}")

def limpar_lista():
    chamados = carregar_chamados()
    opcao = input("Confirme com c para limpar a lista: ").upper() # método UPPER ele deixa as letras maiusculas
    if opcao == "C":
        salvar_chamados([])
        print("Lista de chamados apagada.")

def menu():  #menu princincipal onde cada uma delas executa uma função referente a opção...
    while True:
        print("\n[1] Cadastrar chamado")
        print("[2] buscar chamado")
        print("[3] remover chamado")
        print("[4] listar chamados")
        print("[5] estatísticas")
        print("[6] limpar a lista toda")
        print("[0] sair")
        opcao = input("Eescolha uma opção: ")
        if opcao == "1":
            cadastrar_chamado()
        elif opcao == "2":
            buscar_chamado()
        elif opcao == "3":
            remover_chamado()
        elif opcao == "4":
            listar_chamados()
        elif opcao == "5":
            estatisticas()
        elif opcao == "6":
            limpar_lista()
        elif opcao == "0":
            break
        else:
            print("opção inválida.")

menu()


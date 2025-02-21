import json
import os

ARQUIVO_JSON = "chamados.json"


def carregar_chamados():
    if os.path.exists(ARQUIVO_JSON):  
        with open(ARQUIVO_JSON, "r") as file:
            return json.load(file)
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
        if str(chamado["id"]) == termo or termo.lower() in chamado["descrição"].lower():
            print(chamado)

def remover_chamado(): 
    chamados = carregar_chamados()
    id_remover = int(input("Digite o ID do chamado a remover: "))
    chamados = [c for c in chamados if c["id"] != id_remover]
    salvar_chamados(chamados)
    print("chamado salvo com sucesso")

def listar_chamados():
    chamados = carregar_chamados()
    chamados.sort(key=lambda x: x["prioridade"], reverse=True)
    for chamado in chamados:
        print(chamado)

def estatisticas():
    chamados = carregar_chamados()
    print(f"Total de chamados: {len(chamados)}")
    if chamados:
        media_prioridade = sum(c["prioridade"] for c in chamados) / len(chamados)
        print(f"Prioridade média: {media_prioridade:.2f}")

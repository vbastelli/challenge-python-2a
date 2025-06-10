# Dados de estoque fornecidos
end_sp = {
    "endereco": {
        "cep": "03685-020",
        "logradouro": "Rua Morro da Santa",
        "bairro": "Jardim São Nicolau",
        "localidade": "São Paulo",
        "estado": "São Paulo",
        "regiao": "Sudeste"
    }
}
end_rj = {
    "endereco": {
        "cep": "20020-080",
        "logradouro": "Av. Presidente Vargas",
        "bairro": "Centro",
        "localidade": "Rio de Janeiro",
        "estado": "Rio de Janeiro",
        "regiao": "Sudeste"
    }
}
end_campinas = {
    "endereco": {
        "cep": "13025-240",
        "logradouro": "Rua José Paulino",
        "bairro": "Centro",
        "localidade": "Campinas",
        "estado": "São Paulo",
        "regiao": "Sudeste"
    }
}

estoque_dasa = {
    "tubo_coleta_sangue": {
        "id": "001",
        "locais": {
            "Laboratório SP": {
                "Quantidade": 120,
                "endereco": end_sp["endereco"]
            },
            "Hospital RJ": {
                "Quantidade": 80,
                "endereco": end_rj["endereco"]
            },
            "Unidade Campinas": {
                "Quantidade": 45,
                "endereco": end_campinas["endereco"]
            }
        },
        "ideal": 100
    },
    "luvas_descartaveis": {
        "id": "002",
        "locais": {
            "Laboratório SP": {
                "Quantidade": 300,
                "endereco": end_sp["endereco"]
            },
            "Hospital RJ": {
                "Quantidade": 450,
                "endereco": end_rj["endereco"]
            },
            "Unidade Campinas": {
                "Quantidade": 280,
                "endereco": end_campinas["endereco"]
            }
        },
        "ideal": 400
    },
    "reagente_bioquimico": {
        "id": "003",
        "locais": {
            "Laboratório SP": {
                "Quantidade": 30,
                "endereco": end_sp["endereco"]
            },
            "Hospital RJ": {
                "Quantidade": 12,
                "endereco": end_rj["endereco"]
            },
            "Unidade Campinas": {
                "Quantidade": 18,
                "endereco": end_campinas["endereco"]
            }
        },
        "ideal": 25
    },
    "kit_teste_covid": {
        "id": "004",
        "locais": {
            "Laboratório SP": {
                "Quantidade": 50,
                "endereco": end_sp["endereco"]
            },
            "Hospital RJ": {
                "Quantidade": 20,
                "endereco": end_rj["endereco"]
            },
            "Unidade Campinas": {
                "Quantidade": 10,
                "endereco": end_campinas["endereco"]
            }
        },
        "ideal": 40
    },
    "mascara_n95": {
        "id": "005",
        "locais": {
            "Laboratório SP": {
                "Quantidade": 80,
                "endereco": end_sp["endereco"]
            },
            "Hospital RJ": {
                "Quantidade": 160,
                "endereco": end_rj["endereco"]
            },
            "Unidade Campinas": {
                "Quantidade": 95,
                "endereco": end_campinas["endereco"]
            }
        },
        "ideal": 150
    },
    "alcool_70": {
        "id": "006",
        "locais": {
            "Laboratório SP": {
                "Quantidade": 40,
                "endereco": end_sp["endereco"]
            },
            "Hospital RJ": {
                "Quantidade": 70,
                "endereco": end_rj["endereco"]
            },
            "Unidade Campinas": {
                "Quantidade": 35,
                "endereco": end_campinas["endereco"]
            }
        },
        "ideal": 60
    },
    "contrastem_radiologico": {
        "id": "007",
        "locais": {
            "Hospital RJ": {
                "Quantidade": 22,
                "endereco": end_rj["endereco"]
            },
            "Unidade Campinas": {
                "Quantidade": 5,
                "endereco": end_campinas["endereco"]
            }
        },
        "ideal": 15
    },
    "seringa_5ml": {
        "id": "008",
        "locais": {
            "Laboratório SP": {
                "Quantidade": 200,
                "endereco": end_sp["endereco"]
            },
            "Hospital RJ": {
                "Quantidade": 350,
                "endereco": end_rj["endereco"]
            },
            "Unidade Campinas": {
                "Quantidade": 180,
                "endereco": end_campinas["endereco"]
            }
        },
        "ideal": 250
    },
    "agulha_25g": {
        "id": "009",
        "locais": {
            "Laboratório SP": {
                "Quantidade": 400,
                "endereco": end_sp["endereco"]
            },
            "Hospital RJ": {
                "Quantidade": 500,
                "endereco": end_rj["endereco"]
            },
            "Unidade Campinas": {
                "Quantidade": 300,
                "endereco": end_campinas["endereco"]
            }
        },
        "ideal": 450
    },
    "frasco_urina": {
        "id": "010",
        "locais": {
            "Laboratório SP": {
                "Quantidade": 100,
                "endereco": end_sp["endereco"]
            },
            "Hospital RJ": {
                "Quantidade": 60,
                "endereco": end_rj["endereco"]
            },
            "Unidade Campinas": {
                "Quantidade": 70,
                "endereco": end_campinas["endereco"]
            }
        },
        "ideal": 90
    },
    "swab_estéril": {
        "id": "011",
        "locais": {
            "Laboratório SP": {
                "Quantidade": 150,
                "endereco": end_sp["endereco"]
            },
            "Hospital RJ": {
                "Quantidade": 100,
                "endereco": end_rj["endereco"]
            },
            "Unidade Campinas": {
                "Quantidade": 95,
                "endereco": end_campinas["endereco"]
            }
        },
        "ideal": 120
    },
    "gaze_estéril": {
        "id": "012",
        "locais": {
            "Laboratório SP": {
                "Quantidade": 500,
                "endereco": end_sp["endereco"]
            },
            "Hospital RJ": {
                "Quantidade": 800,
                "endereco": end_rj["endereco"]
            },
            "Unidade Campinas": {
                "Quantidade": 400,
                "endereco": end_campinas["endereco"]
            }
        },
        "ideal": 600
    },
    "avental_descartavel": {
        "id": "013",
        "locais": {
            "Laboratório SP": {
                "Quantidade": 90,
                "endereco": end_sp["endereco"]
            },
            "Hospital RJ": {
                "Quantidade": 200,
                "endereco": end_rj["endereco"]
            },
            "Unidade Campinas": {
                "Quantidade": 100,
                "endereco": end_campinas["endereco"]
            }
        },
        "ideal": 150
    },
    "cateter_venoso": {
        "id": "014",
        "locais": {
            "Hospital RJ": {
                "Quantidade": 35,
                "endereco": end_rj["endereco"]
            },
            "Unidade Campinas": {
                "Quantidade": 20,
                "endereco": end_campinas["endereco"]
            }
        },
        "ideal": 40
    },
    "pipeta_automatica": {
        "id": "015",
        "locais": {
            "Laboratório SP": {
                "Quantidade": 15,
                "endereco": end_sp["endereco"]
            },
            "Unidade Campinas": {
                "Quantidade": 10,
                "endereco": end_campinas["endereco"]
            }
        },
        "ideal": 20
    },
    "sabonete_antisseptico": {
        "id": "016",
        "locais": {
            "Laboratório SP": {
                "Quantidade": 60,
                "endereco": end_sp["endereco"]
            },
            "Hospital RJ": {
                "Quantidade": 85,
                "endereco": end_rj["endereco"]
            },
            "Unidade Campinas": {
                "Quantidade": 45,
                "endereco": end_campinas["endereco"]
            }
        },
        "ideal": 70
    },
    "etiquetas_laboratorio": {
        "id": "017",
        "locais": {
            "Laboratório SP": {
                "Quantidade": 500,
                "endereco": end_sp["endereco"]
            },
            "Hospital RJ": {
                "Quantidade": 300,
                "endereco": end_rj["endereco"]
            },
            "Unidade Campinas": {
                "Quantidade": 250,
                "endereco": end_campinas["endereco"]
            }
        },
        "ideal": 400
    }
}

# Funções de gerenciamento de estoque
def obter_endereco_completo(endereco):
    """Retorna o endereço formatado como string."""
    return f"{endereco['logradouro']}, {endereco['bairro']}, {endereco['localidade']} - {endereco['estado']} (CEP: {endereco['cep']})"

def verificar_estoque_baixo(estoque):
    """Verifica produtos com estoque abaixo do ideal."""
    print("\n📉 Produtos abaixo do ideal:")
    encontrou = False
    for produto, dados in estoque.items():
        ideal = dados["ideal"]
        for unidade, detalhes in dados["locais"].items():
            quantidade = detalhes["Quantidade"]
            if quantidade < ideal:
                encontrou = True
                print(f"- {produto} está com {quantidade} em {unidade} (ideal: {ideal})")
    if not encontrou:
        print("Nenhum produto abaixo do ideal.")

def verificar_estoque_sobrando(estoque):
    """Verifica produtos com estoque acima do ideal."""
    print("\n📈 Produtos acima do ideal:")
    encontrou = False
    for produto, dados in estoque.items():
        ideal = dados["ideal"]
        for unidade, detalhes in dados["locais"].items():
            quantidade = detalhes["Quantidade"]
            if quantidade > ideal:
                encontrou = True
                print(f"- {produto} está com {quantidade} em {unidade} (ideal: {ideal})")
    if not encontrou:
        print("Nenhum produto acima do ideal.")

def relatorio_estoque_por_local(estoque):
    """Gera um relatório consolidado do estoque por local."""
    relatorio = {}
    for produto, dados in estoque.items():
        for unidade, detalhes in dados["locais"].items():
            if unidade not in relatorio:
                relatorio[unidade] = {
                    "endereco": obter_endereco_completo(detalhes["endereco"]),
                    "itens": []
                }
            relatorio[unidade]["itens"].append({
                "produto": produto,
                "quantidade": detalhes["Quantidade"],
                "ideal": dados["ideal"],
                "status": "Baixo" if detalhes["Quantidade"] < dados["ideal"] else "Acima" if detalhes["Quantidade"] > dados["ideal"] else "Ideal"
            })
    
    print("\n📋 Relatório de Estoque por Local:")
    for unidade, info in relatorio.items():
        print(f"\nLocal: {unidade}")
        print(f"Endereço: {info['endereco']}")
        print("Itens:")
        for item in info["itens"]:
            print(f"- {item['produto']}: {item['quantidade']} (Ideal: {item['ideal']}, Status: {item['status']})")

def priorizar_reposicao(estoque):
    """Identifica produtos com maior déficit em relação ao ideal e sugere reposição."""
    prioridades = []
    for produto, dados in estoque.items():
        ideal = dados["ideal"]
        for unidade, detalhes in dados["locais"].items():
            quantidade = detalhes["Quantidade"]
            if quantidade < ideal:
                deficit = ideal - quantidade
                prioridades.append({
                    "deficit": deficit,
                    "produto": produto,
                    "unidade": unidade,
                    "quantidade": quantidade,
                    "ideal": ideal,
                    "endereco": obter_endereco_completo(detalhes["endereco"])
                })
    
    prioridades.sort(key=lambda x: x["deficit"], reverse=True)
    
    print("\n🚨 Prioridades de Reposição:")
    if prioridades:
        for item in prioridades[:5]:
            print(f"- {item['produto']} em {item['unidade']}: Déficit de {item['deficit']} (Atual: {item['quantidade']}, Ideal: {item['ideal']}) - {item['endereco']}")
    else:
        print("Nenhum produto precisa de reposição.")

def verificar_disponibilidade_regional(estoque, regiao):
    """Verifica produtos disponíveis em estoque em uma região específica."""
    print(f"\n🌍 Produtos Disponíveis na Região {regiao}:")
    encontrou = False
    for produto, dados in estoque.items():
        for unidade, detalhes in dados["locais"].items():
            if detalhes["endereco"]["regiao"].lower() == regiao.lower():
                encontrou = True
                print(f"- {produto} em {unidade}: {detalhes['Quantidade']} (Ideal: {dados['ideal']}) - {obter_endereco_completo(detalhes['endereco'])}")
    
    if not encontrou:
        print(f"Nenhum produto encontrado na região {regiao}")

def calcular_media_estoque_produto(estoque, produto_id):
    """Calcula a média do estoque de um produto específico em todos os locais."""
    if produto_id not in estoque:
        return None
    
    quantidades = [detalhes["Quantidade"] for detalhes in estoque[produto_id]["locais"].values()]
    media = sum(quantidades) / len(quantidades) if quantidades else 0
    return media

def comparar_estoque_locais(estoque, produto_id):
    """Compara o estoque de um produto entre diferentes locais."""
    if produto_id not in estoque:
        print(f"\nProduto {produto_id} não encontrado.")
        return
    
    print(f"\n📊 Comparação de Estoque para {produto_id}:")
    for unidade, detalhes in estoque[produto_id]["locais"].items():
        print(f"- {unidade}: {detalhes['Quantidade']} (Ideal: {estoque[produto_id]['ideal']}) - {obter_endereco_completo(detalhes['endereco'])}")
    
    media = calcular_media_estoque_produto(estoque, produto_id)
    if media is not None:
        print(f"Média do estoque nos locais: {media:.1f}")

def sugerir_transferencias_estoque(estoque):
    """Sugere transferências de produtos entre locais com excesso para locais com falta."""
    transferencias = []
    for produto, dados in estoque.items():
        ideal = dados["ideal"]
        locais_excesso = {}
        locais_falta = {}
        
        for unidade, detalhes in dados["locais"].items():
            quantidade = detalhes["Quantidade"]
            if quantidade > ideal:
                locais_excesso[unidade] = quantidade - ideal
            elif quantidade < ideal:
                locais_falta[unidade] = ideal - quantidade
        
        for unidade_falta, deficit in locais_falta.items():
            for unidade_excesso, excesso in locais_excesso.items():
                if excesso > 0 and deficit > 0:
                    quant_transferir = min(excesso, deficit)
                    transferencias.append({
                        "produto": produto,
                        "de": unidade_excesso,
                        "para": unidade_falta,
                        "quantidade": quant_transferir,
                        "endereco_de": obter_endereco_completo(dados["locais"][unidade_excesso]["endereco"]),
                        "endereco_para": obter_endereco_completo(dados["locais"][unidade_falta]["endereco"])
                    })
    
    print("\n🔄 Sugestões de Transferências de Estoque:")
    if transferencias:
        for t in transferencias:
            print(f"- Transferir {t['quantidade']} de {t['produto']} de {t['de']} ({t['endereco_de']}) para {t['para']} ({t['endereco_para']})")
    else:
        print("Nenhuma transferência sugerida.")

# Função para limpar o terminal (funciona em Windows e Unix-like)
import os
def limpar_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

# Função do menu interativo
def menu_interativo():
    while True:
        limpar_terminal()
        print("=== Sistema de Gerenciamento de Estoque ===")
        print("1. Verificar estoque baixo")
        print("2. Verificar estoque sobrando")
        print("3. Relatório de estoque por local")
        print("4. Priorizar reposição")
        print("5. Verificar disponibilidade regional")
        print("6. Comparar estoque de um produto entre locais")
        print("7. Sugerir transferências de estoque")
        print("8. Sair")
        
        try:
            opcao = input("\nEscolha uma opção (1-8): ")
            
            if opcao == "1":
                limpar_terminal()
                verificar_estoque_baixo(estoque_dasa)
            elif opcao == "2":
                limpar_terminal()
                verificar_estoque_sobrando(estoque_dasa)
            elif opcao == "3":
                limpar_terminal()
                relatorio_estoque_por_local(estoque_dasa)
            elif opcao == "4":
                limpar_terminal()
                priorizar_reposicao(estoque_dasa)
            elif opcao == "5":
                limpar_terminal()
                regiao = input("Digite a região (ex: Sudeste): ")
                verificar_disponibilidade_regional(estoque_dasa, regiao)
            elif opcao == "6":
                limpar_terminal()
                produto = input("Digite o nome do produto (ex: tubo_coleta_sangue): ")
                comparar_estoque_locais(estoque_dasa, produto)
            elif opcao == "7":
                limpar_terminal()
                sugerir_transferencias_estoque(estoque_dasa)
            elif opcao == "8":
                limpar_terminal()
                print("Saindo do sistema. Até logo!")
                break
            else:
                print("\nOpção inválida! Por favor, escolha um número entre 1 e 8.")
            
            if opcao != "8":
                input("\nPressione Enter para voltar ao menu...")
        
        except KeyboardInterrupt:
            limpar_terminal()
            print("Operação interrompida. Saindo do sistema.")
            break
        except Exception as e:
            print(f"\nOcorreu um erro: {e}")
            input("\nPressione Enter para voltar ao menu...")

# Executa o menu
if __name__ == "__main__":
    menu_interativo()
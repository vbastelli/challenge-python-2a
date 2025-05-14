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

def verificar_estoque_baixo(estoque):
    print("📉 Produtos abaixo do ideal:")
    for produto, dados in estoque.items():
        ideal = dados["ideal"]
        for unidade, detalhes in dados["locais"].items():
            quantidade = detalhes["Quantidade"]
            if quantidade < ideal:
                print(f"- {produto} está com {quantidade} em {unidade} (ideal: {ideal})")

def verificar_estoque_sobrando(estoque):
    print("📈 Produtos acima do ideal:")
    for produto, dados in estoque.items():
        ideal = dados["ideal"]
        for unidade, detalhes in dados["locais"].items():
            quantidade = detalhes["Quantidade"]
            if quantidade > ideal:
                print(f"- {produto} está com {quantidade} em {unidade} (ideal: {ideal})")

def obter_enderecos_por_id(estoque, item_id):
    for nome_produto, dados in estoque.items():
        if dados.get("id") == item_id:
            locais = dados.get("locais", {})
            resultado = {}
            for nome_local, info in locais.items():
                endereco = info.get("endereco")
                if endereco:
                    resultado[nome_local] = endereco
            return resultado
    return f"Item com ID '{item_id}' não encontrado."




verificar_estoque_baixo(estoque_dasa)
verificar_estoque_sobrando(estoque_dasa)

print(obter_enderecos_por_id(estoque_dasa, "010"))
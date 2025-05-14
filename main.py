estoque_dasa = {
    "tubo_coleta_sangue": {
        "id": "001",
        "locais": {
            "Laboratório SP": 120,
            "Hospital RJ": 80,
            "Unidade Campinas": 45
        },
        "ideal": 100
    },
    "luvas_descartaveis": {
        "id": "002",
        "locais": {
            "Laboratório SP": 300,
            "Hospital RJ": 450,
            "Unidade Campinas": 280
        },
        "ideal": 400
    },
    "reagente_bioquimico": {
        "id": "003",
        "locais": {
            "Laboratório SP": 30,
            "Hospital RJ": 12,
            "Unidade Campinas": 18
        },
        "ideal": 25
    },
    "kit_teste_covid": {
        "id": "004",
        "locais": {
            "Laboratório SP": 50,
            "Hospital RJ": 20,
            "Unidade Campinas": 10
        },
        "ideal": 40
    },
    "mascara_n95": {
        "id": "005",
        "locais": {
            "Laboratório SP": 80,
            "Hospital RJ": 160,
            "Unidade Campinas": 95
        },
        "ideal": 150
    },
    "alcool_70": {
        "id": "006",
        "locais": {
            "Laboratório SP": 40,
            "Hospital RJ": 70,
            "Unidade Campinas": 35
        },
        "ideal": 60
    },
    "contrastem_radiologico": {
        "id": "007",
        "locais": {
            "Hospital RJ": 22,
            "Unidade Campinas": 5
        },
        "ideal": 15
    },
    "seringa_5ml": {
        "id": "008",
        "locais": {
            "Laboratório SP": 200,
            "Hospital RJ": 350,
            "Unidade Campinas": 180
        },
        "ideal": 250
    },
    "agulha_25g": {
        "id": "009",
        "locais": {
            "Laboratório SP": 400,
            "Hospital RJ": 500,
            "Unidade Campinas": 300
        },
        "ideal": 450
    },
    "frasco_urina": {
        "id": "010",
        "locais": {
            "Laboratório SP": 100,
            "Hospital RJ": 60,
            "Unidade Campinas": 70
        },
        "ideal": 90
    },
    "swab_estéril": {
        "id": "011",
        "locais": {
            "Laboratório SP": 150,
            "Hospital RJ": 100,
            "Unidade Campinas": 95
        },
        "ideal": 120
    },
    "gaze_estéril": {
        "id": "012",
        "locais": {
            "Laboratório SP": 500,
            "Hospital RJ": 800,
            "Unidade Campinas": 400
        },
        "ideal": 600
    },
    "avental_descartavel": {
        "id": "013",
        "locais": {
            "Laboratório SP": 90,
            "Hospital RJ": 200,
            "Unidade Campinas": 100
        },
        "ideal": 150
    },
    "cateter_venoso": {
        "id": "014",
        "locais": {
            "Hospital RJ": 35,
            "Unidade Campinas": 20
        },
        "ideal": 40
    },
    "pipeta_automatica": {
        "id": "015",
        "locais": {
            "Laboratório SP": 15,
            "Unidade Campinas": 10
        },
        "ideal": 20
    },
    "sabonete_antisseptico": {
        "id": "016",
        "locais": {
            "Laboratório SP": 60,
            "Hospital RJ": 85,
            "Unidade Campinas": 45
        },
        "ideal": 70
    },
    "etiquetas_laboratorio": {
        "id": "017",
        "locais": {
            "Laboratório SP": 500,
            "Hospital RJ": 300,
            "Unidade Campinas": 250
        },
        "ideal": 400
    }
}



def verificar_estoque_baixo(estoque):
    print("📉 Produtos abaixo do ideal:")
    for produto, dados in estoque.items():
        ideal = dados["ideal"]
        for unidade, quantidade in dados["locais"].items():
            if quantidade < ideal:
                print(f"- {produto} está com {quantidade} em {unidade} (ideal: {ideal})")


def verificar_estoque_sobrando(estoque):
    print("📈 Produtos acima do ideal:")
    for produto, dados in estoque.items():
        ideal = dados["ideal"]
        for unidade, quantidade in dados["locais"].items():
            if quantidade > ideal:
                print(f"- {produto} está com {quantidade} em {unidade} (ideal: {ideal})")

verificar_estoque_baixo(estoque_dasa)

verificar_estoque_sobrando(estoque_dasa)
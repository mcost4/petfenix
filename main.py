from fastapi import FastAPI, Query
from typing import Literal

app = FastAPI()

# Tabela de preços baseada na planilha fornecida
tabela_precos = {
    "2025": {
        "Coletiva": {"Até 1kg": 260, "1 a 15kg": 400, "16 a 30kg": 520, "Acima de 30kg": 750},
        "Individual": {"Até 1kg": 420, "1 a 15kg": 690, "16 a 30kg": 900, "Acima de 30kg": 1200},
        "Imediata": {"Até 1kg": 950, "1 a 15kg": 1380, "16 a 30kg": 1380, "Acima de 30kg": 1500},
    },
    "2026-Cartao": {
        "Coletiva": {"Até 1kg": 285, "1 a 15kg": 440, "16 a 30kg": 570, "Acima de 30kg": 825},
        "Individual": {"Até 1kg": 460, "1 a 15kg": 760, "16 a 30kg": 880, "Acima de 30kg": 1320},
        "Imediata": {"Até 1kg": 1045, "1 a 15kg": 1520, "16 a 30kg": 1520, "Acima de 30kg": 1700},
    },
    "2026-Pix": {
        "Coletiva": {"Até 1kg": 270.75, "1 a 15kg": 418, "16 a 30kg": 541.5, "Acima de 30kg": 783.75},
        "Individual": {"Até 1kg": 437, "1 a 15kg": 722, "16 a 30kg": 836, "Acima de 30kg": 1254},
        "Imediata": {"Até 1kg": 992.75, "1 a 15kg": 1444, "16 a 30kg": 1444, "Acima de 30kg": 1567.5},
    },
}

TAXA_URGENCIA = 90.0

@app.get("/preco")
def consultar_preco(
    ano: Literal["2025", "2026-Cartao", "2026-Pix"] = Query(..., description="Ano e forma de pagamento"),
    servico: Literal["Coletiva", "Individual", "Imediata"] = Query(...),
    peso: Literal["Até 1kg", "1 a 15kg", "16 a 30kg", "Acima de 30kg"] = Query(...),
    urgencia: bool = Query(False, description="Se é urgente, adiciona taxa de urgência")
):
    preco = tabela_precos[ano][servico][peso]
    if urgencia:
        preco += TAXA_URGENCIA
    return {"preco": preco}

@app.get("/")
def root():
    return {"mensagem": "API de consulta de preços PetFênix"}

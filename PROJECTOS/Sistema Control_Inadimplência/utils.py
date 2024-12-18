# =========================
# utils.py (Funções Auxiliares)
# =========================

import pandas as pd

def validate_and_format_data(data):
    """
    Valida e formata os dados do arquivo Excel.
    :param data: DataFrame contendo os dados do arquivo Excel.
    :return: DataFrame validado e formatado.
    """
    required_columns = ["name", "ldday", "lamount", "balprinc", "arrears", "days", "lastrepdate"]

    # Verificar colunas obrigatórias
    for column in required_columns:
        if column not in data.columns:
            raise ValueError(f"Coluna obrigatória ausente: {column}")

    # Formatar valores monetários
    data["lamount"] = data["lamount"].apply(lambda x: f"{x:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))
    data["balprinc"] = data["balprinc"].apply(
        lambda x: f"{x:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))
    data["arrears"] = data["arrears"].apply(lambda x: f"{x:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))

    return data

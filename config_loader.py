import json
import os
from logger_config import logger

def load_config(file_path="config/empresas.json"):
    if not os.path.exists(file_path):
        logger.error(f"Arquivo de configuração não encontrado: {file_path}")
        return []

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            empresas = json.load(f)
            logger.info(f"Configuração carregada com sucesso. {len(empresas)} empresas encontradas.")
            return empresas
    except json.JSONDecodeError as e:
        logger.error(f"Erro ao decodificar JSON do arquivo de configuração: {e}")
        return []
    except Exception as e:
        logger.error(f"Erro inesperado ao carregar arquivo de configuração: {e}")
        return []

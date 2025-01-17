import os
import sys

import pandas as pd
import structlog
from utils.utils import load_config_file

sys.path.append(os.path.join(os.path.dirname(__file__), "../src"))
logger = structlog.getLogger()


class DataLoad:
    """
    Classe para carregar dados de um arquivo CSV.

    Methods:
        load_data: Carrega os dados do arquivo CSV especificado.
    """

    def __init__(self) -> None:
        pass

    def load_data(self, dataset_name: str) -> pd.DataFrame:
        """Carrega os dados a partir do nome do dataser fornecido

        Args:
            dataset_name (str): O nome do arquivo CSV a ser carregado.

        Returns:
            dataframe: Um DataFrame contendo os dados carregados do arquivo CSV.
        """
        logger.info(f"Começando a carga dos dados com o nome {dataset_name}")
        try:
            dataset = load_config_file().get(dataset_name)
            if dataset is None:
                raise ValueError(
                    f"Erro: O nome do dataset fornecido é incorreto: {dataset}"
                )
            path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
            dataset_path = os.path.join(path, "data", "raw", dataset)

            loaded_data = pd.read_csv(dataset_path)
            return loaded_data[load_config_file().get("columns_to_use")]
        except ValueError as ve:
            logger.error(str(ve))
        except Exception as e:
            logger.error(f"Erro inesperado: {str(e)}")

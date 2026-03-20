import argparse
from config_loader import load_config
from robot_runner import RobotRunner
from logger_config import logger

def main():
    parser = argparse.ArgumentParser(description="Processo RPA de Coleta de Faturas")
    parser.add_argument("--headless", action="store_true", help="Executar navegador em modo Headless (oculto)", default=False)
    args = parser.parse_args()

    empresas_config = load_config()
    
    if not empresas_config:
        logger.error("Nenhuma configuração de empresa carregada. O robô será encerrado.")
        return

    runner = RobotRunner(empresas_config, headless=args.headless)
    runner.run()

if __name__ == "__main__":
    main()

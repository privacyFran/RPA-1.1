import traceback
from logger_config import logger
from browser_manager import get_browser
from site_automation import CPFLAutomation

class RobotRunner:
    def __init__(self, empresas_config, headless=False):
        self.empresas = empresas_config
        self.headless = headless

    def run(self):
        logger.info("=== Iniciando execução do Robô Coletor de Faturas ===")
        
        for config in self.empresas:
            empresa_name = config.get('empresa', 'desconhecido').lower()
            logger.info(f"Iniciando coleta {empresa_name.upper()}")
            
            driver = None
            try:
                driver, download_dir = get_browser(empresa_name, headless=self.headless)
                
                if not driver:
                    logger.error(f"[{empresa_name.upper()}] Pulando processamento devido a erro no navegador.")
                    continue
                
                if empresa_name == 'cpfl':
                    automation = CPFLAutomation(driver, config, download_dir)
                else:
                    logger.warning(f"[{empresa_name.upper()}] Automação não implementada para esta empresa.")
                    continue
                
                sucesso = automation.executar()
                
                if sucesso:
                    logger.info(f"[{empresa_name.upper()}] Coleta finalizada com sucesso.")
                else:
                    logger.warning(f"[{empresa_name.upper()}] Coleta finalizada com erros ou incompleta.")

            except Exception as e:
                logger.error(f"[{empresa_name.upper()}] Erro inesperado durante execução: {str(e)}")
                # logger.debug(traceback.format_exc())
            
            finally:
                if driver:
                    logger.info(f"[{empresa_name.upper()}] Fechando navegador.")
                    try:
                        driver.quit()
                    except Exception as e:
                        logger.error(f"[{empresa_name.upper()}] Erro ao fechar navegador: {e}")
                        
        logger.info("=== Execução do Robô finalizada ===")

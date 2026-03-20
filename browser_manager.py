import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from logger_config import logger

def get_browser(empresa_name, headless=False):
    """
    Configura e retorna uma instância do Chrome WebDriver.
    """
    options = Options()
    
    if headless:
        options.add_argument('--headless=new')
        options.add_argument('--disable-gpu')
        options.add_argument('--window-size=1920,1080')
        logger.info(f"[{empresa_name}] Configurando navegador em modo HEADLESS")
    else:
        options.add_argument('--start-maximized')
        logger.info(f"[{empresa_name}] Configurando navegador em modo NORMAL")

    # Anti-bot detection mitigation
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)

    # Set up download directory dynamically
    base_dir = os.path.dirname(os.path.abspath(__file__))
    download_dir = os.path.join(base_dir, "downloads", empresa_name)
    
    if not os.path.exists(download_dir):
        os.makedirs(download_dir)
        
    logger.info(f"[{empresa_name}] Diretório de download: {download_dir}")

    # Configs to auto download PDFs instead of trying to open them
    prefs = {
        "download.default_directory": download_dir,
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "plugins.always_open_pdf_externally": True, 
        "safebrowsing.enabled": True
    }
    options.add_experimental_option("prefs", prefs)

    try:
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=options)
        # Apply stealth settings
        driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
        return driver, download_dir
    except Exception as e:
        logger.error(f"[{empresa_name}] Falha ao iniciar o navegador: {e}")
        return None, None

import time
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def remove_non_bmp(text):
    return ''.join(c for c in text if ord(c) <= 0xFFFF)

def send_whatsapp_message(message, contact_name="ChorumeNews"):
    print("🟡 Inicializando navegador...")

    options = uc.ChromeOptions()
    options.add_argument("--user-data-dir=C:/whatsapp_bot_profile")
    options.add_argument("--headless=new")  # Ative após testes
    options.add_argument("--log-level=3")

    driver = uc.Chrome(options=options)
    driver.get("https://web.whatsapp.com")

    print("🟡 Aguardando carregamento do WhatsApp Web...")
    time.sleep(15)

    print("🟢 WhatsApp carregado. Procurando contato...")

    search_box = driver.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="3"]')
    search_box.clear()
    search_box.send_keys(contact_name)
    time.sleep(2)

    chat = driver.find_element(By.XPATH, f'//span[@title="{contact_name}"]')
    chat.click()
    print(f"🟢 Chat com '{contact_name}' aberto.")

    msg_box = driver.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="10"]')

    print("🟡 Enviando mensagem...")
    msg_box.send_keys(remove_non_bmp(message))
    msg_box.send_keys("\n")
    print("✅ Mensagem enviada com sucesso.")

    time.sleep(3)
    driver.quit()
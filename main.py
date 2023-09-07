from logic import check_contacts_on_whatsapp
from utils import setup_browser

def main():
    browser, wait = setup_browser(40)

    contacts_to_check = ['+923227942883', '+923227942881', '+923227942885']
    results = check_contacts_on_whatsapp(wait, contacts_to_check)
    print(results)

    browser.quit()

if __name__ == "__main__":
    main()

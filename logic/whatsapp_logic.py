from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from .custom_conditions import element_to_be_present_either_of_two_conditions
from selenium.webdriver.support import expected_conditions as EC

def check_contacts_on_whatsapp(wait, phone_numbers):
    result = {}

    # Click the new chat button
    new_chat_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'span[data-icon="chat"]')))
    new_chat_button.click()

    for phone_number in phone_numbers:
        # Enter the phone number
        contact_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div[role="textbox"]')))
        contact_input.send_keys(phone_number)

        condition = element_to_be_present_either_of_two_conditions(
            (By.XPATH, f"//span[translate(@title, ' ', '')='{phone_number}']"),
            (By.XPATH, "//span[@class='_11JPr' and contains(text(), 'No results found for')]"))
        
        found_condition, _ = wait.until(condition)
        if found_condition == 'first':  # found the contact
            result[phone_number] = True
        elif found_condition == 'second':  # did not find the contact
            result[phone_number] = False

        # Clear the contact input
        for _ in range(len(phone_number) + 1):
            contact_input.send_keys(Keys.BACKSPACE)
    return result

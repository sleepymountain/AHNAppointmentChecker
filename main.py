import os

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import logging
from selenium.webdriver.remote.remote_connection import LOGGER
from win10toast import ToastNotifier
import sched, time
from datetime import datetime
from colorama import Fore

toaster = ToastNotifier()
s = sched.scheduler(time.time, time.sleep)

url = "https://www.ahn.org/coronavirus/vaccine/schedule/eligible.html"
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])


def start():

    print('AHN Appointment Checker v1.6b | by caverin/sleepymountain')
    print('https://github.com/sleepymountain/AHNAppointmentChecker')
    print(f'')
    print('[i] Running appointment checker..')
    print(f'')
    LOGGER.setLevel(logging.WARNING)


if __name__ == '__main__':
    start()
    if not os.path.exists('log'):
        os.makedirs('log')
    logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M %p', filename='log/log.txt', level=logging.INFO)



def no_appt_xpath():
    with webdriver.Chrome(options=chrome_options) as driver:
        wait = WebDriverWait(driver, 10)
        driver.get("https://www.ahn.org/coronavirus/vaccine/schedule.html")
        try:
            driver.find_element_by_xpath("/html/body/main/div[2]/div/section/div/div/div/div[1]/div/h1")
        except NoSuchElementException:
            no_appt_xpath.no_appointments = 0
            return False
        else:
            no_appt_xpath.no_appointments = 1
            return True


def load_page():
        now = datetime.now()
        dt_string = now.strftime("%m/%d/%Y %I:%M %p")
        print('[i] Checking for new appointments..')
        no_appt_xpath()
        if no_appt_xpath.no_appointments == 1:
            print(dt_string, " | There are no appointments available")
            logging.info(' | There are no appointments available')
            print(f'')
        elif no_appt_xpath.no_appointments == 0:
            print("[!]", dt_string, " | There might be appointments available!")
            print("[i] If the page loads and shows that there are no appointments, open in a private window.")
            logging.info(' | There might be appointments available!')
            print(f'')
            toaster.show_toast("AHN Appointment Checker", "There are appointments available!")
            os.startfile(url)
        else:
            print(dt_string, " | There are no appointments available")
            logging.info(' | There are no appointments available')
            print(f'')
        print('[i] Waiting 5 minutes.')
        time.sleep(300)



while True:
    load_page()



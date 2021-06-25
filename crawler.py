import random

from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium_stealth import stealth

SEARCH_STRINGS = [
    "arraylist java",
    "java mutex",
    "mutex lock",
    "python list comprehension",
    "list comprehension",
    "c++ move semantics"
]


def get_random_search_term():
  return random.choice(SEARCH_STRINGS)


def set_old_user_agent(driver):
  stealth(driver,
          user_agent='DN',
          languages=["en-US", "en"],
          vendor="Google Inc.",
          platform="Win32",
          webgl_vendor="Intel Inc.",
          renderer="Intel Iris OpenGL Engine",
          fix_hairline=True,
          )


def set_new_user_agent(driver):
  stealth(driver,
          user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36',
          languages=["en-US", "en"],
          vendor="Google Inc.",
          platform="Win32",
          webgl_vendor="Intel Inc.",
          renderer="Intel Iris OpenGL Engine",
          fix_hairline=True,
          )


if __name__ == "__main__":
  options = Options()
  options.add_argument('--allow-running-insecure-content')
  options.add_argument("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36")
  options.add_experimental_option("excludeSwitches", ['enable-logging', 'enable-automation'])
  options.add_experimental_option('useAutomationExtension', False)
  options.add_argument('--disable-blink-features=AutomationControlled')

  search_key_history = []

  driver = webdriver.Chrome(options=options, executable_path='./chromedriver')

  # this switch of user agents was based from here: https://www.reddit.com/r/Python/comments/mtvbz1/selenium_google_login_blocked_in_automation/
  set_old_user_agent(driver)
  sleep(1)
  driver.get("http://google.com/ncr")
  sleep(1)
  # new tab opening inspired from here: https://python-forum.io/thread-7530.html
  driver.execute_script("window.open('');")
  sleep(3)
  driver.switch_to.window(driver.window_handles[1])
  sleep(1)
  driver.get("http://google.com/ncr")
  sleep(1)

  print("Type anything and ENTER to start the search")
  wait_input = input()

  while True:
    q_input = driver.find_element_by_name("q")
    q_input.clear()
    search_key = get_random_search_term()
    search_key_history.append(search_key)
    q_input.send_keys(search_key, Keys.ENTER)

    sleep(5)

    try:
      element = driver.find_element_by_partial_link_text('I want to play')
      print('Found link. Login in the first tab and after that press anything here and ENTER')
      print(search_key_history)
      a = input()
      break
    except:
      pass

      sleep(5)

  driver.quit()

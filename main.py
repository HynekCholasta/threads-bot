from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
#chatgpt 
from openai import OpenAI
import selenium

from dotenv import load_dotenv, dotenv_values

load_dotenv()


env_values = dotenv_values('.env')
# Initialize OpenAI client
openai_api_key = env_values['OPENAI_API_KEY']
# Initialize the OpenAI client with the API key from the environment variable
client = OpenAI(api_key=openai_api_key)

# Make a request to the OpenAI API using the updated interface
chat_completion = client.chat.completions.create(
    model='gpt-3.5-turbo',
    messages=[
        {'role': 'user', 'content': 'give me a wise stoic quote, put the quote in quotation marks and also separate the quote from the the part who said it by one line'},
    ]
)

# Print the entire response object for debugging
print(chat_completion)

# Extract the content of the response
output = chat_completion.choices[0].message.content
print(output)


#ACCESSNG THREADS

time.sleep(3)

# Set up the webdriver using webdriver-manager
service = Service(EdgeChromiumDriverManager().install())
driver = webdriver.Edge(service=service)

# Open a webpage
url = 'https://www.threads.net/login'  # Replace with the URL of the page you want to interact with
driver.get(url)

# Allow some time for the page to load
time.sleep(3)

# Find the specific div (example by id, you can use other selectors like class name, xpath, etc.)
try:
    wait = WebDriverWait(driver, 2)  # 10 seconds timeout
    div = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.x1i10hfl.xjbqb8w.x1ypdohk.x2lah0s.xe8uvvx.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.x2lwn1j.xexx8yu.x18d9i69.x1n2onr6.x16tdsg8.x1hl2dhg.xggy1nq.x1ja2u2z.x1t137rt.x1q0g3np.x1lku1pv.x1a2a7pz.x6s0dn4.x1a2cdl4.xnhgr82.x1qt0ttw.xgk8upj.x9f619.x3nfvp2.x1s688f.x90ne7k.xl56j7k.x193iq5w.x1swvt13.x1pi30zi.x12w9bfk.x1g2r6go.x11xpdln.xz4gly6.x87ps6o.xuxw1ft.x19kf12q.x6bh95i.x1re03b8.x1hvtcl2.x3ug3ww.x13fuv20.xu3j5b3.x1q0q8m5.x26u7qi.x178xt8z.xm81vs4.xso031l.xy80clv.xp07o12.x11r8ahe.x1iyjqo2.x15x72sd')))
    div.click()
except Exception as e:
    print(f"Error finding element by CLASS_NAME: {e}")

time.sleep(2)




# Combine all class names into a CSS selector for the <a> tag
class_selector = (
    '.x1i10hfl.x1qjc9v5.xjqpnuy.xa49m3k.xqeqjp1.x2hbi6w.x13fuv20.xu3j5b3'
    '.x1q0q8m5.x26u7qi.x972fbf.xcfux6l.x1qhh985.xm0m39n.x9f619.x1ypdohk'
    '.xdl72j9.x2lah0s.xe8uvvx.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.x2lwn1j'
    '.xeuugli.x1n2onr6.x16tdsg8.x1hl2dhg.xggy1nq.x1ja2u2z.x1t137rt.x87ps6o'
    '.x1lku1pv.xzii09s.x1tlxs6b.x1g8br2z.x1gn5b1j.x230xth.x78zum5.xdt5ytf'
    '.x1b3rpy.x1cnzs8.xxbr6pl.xwxc41k.xbbxn1n.x12w9bfk.x1g2r6go.x11xpdln.xk4oym4'
)

# Wait for the <a> element to be present and clickable
try:
    wait = WebDriverWait(driver, 10)  # 10 seconds timeout
    link_element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, f'a{class_selector}')))
    link_element.click()
except Exception as e:
    print(f"Error finding or clicking the element by CSS_SELECTOR: {e}")

time.sleep(3)

env_values = dotenv_values('.env')
username = env_values['USERNAME']
password = env_values['PASSWORD']

# Create an instance of ActionChains
actions = ActionChains(driver)
# Simulate pressing keys (for example, typing "Hello World" followed by pressing ENTER)
actions.send_keys(username).send_keys(Keys.TAB).perform()
time.sleep(3)
actions.send_keys(password).send_keys(Keys.ENTER).perform()

# Allow some time to observe the result
time.sleep(5)


class_selector2 = (
    '.x1i10hfl.xjbqb8w.x1ejq31n.xd10rxx.x1sy0etr.x17r0tee.x972fbf.xcfux6l'
    '.x1qhh985.xm0m39n.x9f619.xe8uvvx.xdj266r.xat24cr.xexx8yu.x4uap5.x18d9i69'
    '.x16tdsg8.x1hl2dhg.xggy1nq.x1a2a7pz.x6s0dn4.x1a2cdl4.xnhgr82.x1qt0ttw'
    '.xgk8upj.x1ed109x.x78zum5.x1iyjqo2.x1i64zmx.x1emribx.x1e558r4.x87ps6o'
)

# Wait for the <div> element to be present and clickable
try:
    wait = WebDriverWait(driver, 3)  # 10 seconds timeout
    div_element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, f'div{class_selector2}')))
    div_element.click()
except Exception as e:
    print(f"Error finding or clicking the element by CSS_SELECTOR2: {e}")
time.sleep(10)
actions.send_keys(f"{output}")
time.sleep(5)
actions.key_down(Keys.CONTROL).send_keys(Keys.RETURN).key_up(Keys.CONTROL).perform()


time.sleep(10)


# Close the browser
driver.quit()

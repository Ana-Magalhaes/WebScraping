import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from bs4 import BeautifulSoup
from time import sleep

# Links for WebScraping
link_apple = 'https://www.apple.com/br/iphone-15-pro/'
link_samsung = 'https://www.samsung.com/br/smartphones/galaxy-s24-ultra/'

# Open the page to analyze and go for specifications 
options = webdriver.EdgeOptions()
driver = webdriver.Edge(options=options)
driver.get(link_apple)
sleep(3)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
sleep(5)
specifications = driver.find_element(By.XPATH, '/html/body/nav/div/div[2]/div[2]/div[1]/ul/li[3]/a').click()

# Parameter
html = driver.page_source

# Iniciation of WebScraping, catch all website
soup = BeautifulSoup(html, 'html.parser')

# Shortcuts
blocks = soup.find_all('div', class_='techspecs-column')
column1 = blocks[6]
column2 = blocks[8]
column3 = blocks[12]
column4 = blocks[13]
column5 = blocks[33]
column6 = blocks[19]
column7 = blocks[29]
column8 = blocks[30]
column9 = blocks[31]
column10 = blocks[23]
column11 = blocks[24]

# Puzzle (Parts of)
screen1 = column1.find('ul', class_='techspecs-list').getText().strip()
screen2 = column2.find('ul', class_='techspecs-list').getText().strip()
cam1 = column3.find('ul', class_='techspecs-list').getText().strip()
cam2 = column4.find('ul', class_='techspecs-list').getText().strip()
sys = soup.find('div', class_='techspecs-section section-os')
net = column6.find('ul', class_='techspecs-list').getText().strip()
work = soup.find('div', class_='row model-group')
work2 = work.find('ul', class_='techspecs-list').getText().strip()
one = column7.getText().strip()
two = column8.getText().strip()
three = column9.find('ul', class_='techspecs-list').getText().strip()
aud = column10.getText().strip()
io = column11.getText().strip()

# Specifications for Pandas (Option 1)
colors_Apple = soup.find('div', class_='techspecs-column iphone-pro-max small-spans-2-columns').getText().strip()
capacity_Apple = soup.find('ul', class_='techspecs-list').getText().strip()
dimensions_Apple = soup.find('div', class_='techspecs-column small-spans-2-columns').getText().strip()
screen_Apple = (screen1) + '\n' + (screen2)
processor_Apple = soup.find('div', class_='column copy large-10 medium-9 small-12 small-push-0').getText().strip()
camera_Apple = cam1 + '\n' + cam2
sensors_Apple = column5.find('ul', class_='techspecs-list').getText().strip()
system_Apple = sys.find('ul', class_='techspecs-list').getText().strip()
network_Apple = net + '\n' + work2
battery_Apple = one + '\n' + two + '\n' + three
audio_Apple = aud + '\n' + io

# Exit Website
driver.quit()

# Open the page to analyze  
options = webdriver.EdgeOptions()
driver = webdriver.Edge(options=options)
driver.get(link_samsung)
sleep(3)

# Try to accept cookies 
try:
    cookie = driver.find_element(By.XPATH,'/html/body/div[4]/div/div/div[2]/button[2]').click()
except:
    sleep(3)

# Go for specifications
specifications_ = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/div/div/div/div/div[1]/section/div/div/div[2]/div/ul/li[4]/a').click()
sleep(10)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
sleep(5)

# Parameter
html_ = driver.page_source

# Create an BeautifulSoup object to analyze the HTML 
soup_ = BeautifulSoup(html_, 'html.parser')

# Shortcuts
bloco = soup_.find_all('ul', class_='specification__spec-list')
coluna = bloco[4]
coluna2 = bloco[10]
coluna3 = bloco[1]
coluna4 = bloco[0]
coluna5 = bloco[3]
coluna6 = bloco[9]
coluna7 = bloco[7]
coluna8 = bloco[5]
coluna9 = bloco[11]
coluna10 = bloco[12]

# Puzzle (Parts of)
color = soup_.find('div', class_='specification__color-list').getText().strip()
colors = color.split('\n')
cor = '\n'.join(cores for cores in colors if cores.strip()) #Remove only paragraph empty

# Specifications for Pandas (Option 2)
colors_Samsung = '\n'.join(cores for cores in colors if cores.strip()) #Remove only paragraph empty
capacity_Samsung = coluna.getText().strip()
dimensions_Samsung = coluna2.getText().strip()
screen_Samsung = coluna3.getText().strip()
processor_Samsung = coluna4.getText().strip()
camera_Samsung = coluna5.getText().strip()
sensors_Samsung = coluna6.getText().strip()
system_Samsung = coluna7.getText().strip()
network_Samsung = coluna8.getText().strip()
battery_Samsung = coluna9.getText().strip()
audio_Samsung = coluna10.getText().strip()

# Exit Website
driver.quit()

# Data List
data = [
    ('Apple', 'Colors', colors_Apple),
    ('Apple', 'Capacity', capacity_Apple),
    ('Apple', 'Dimensions', dimensions_Apple),
    ('Apple', 'Screen', screen_Apple),
    ('Apple', 'Processor', processor_Apple),
    ('Apple', 'Camera', camera_Apple),
    ('Apple', 'Sensors', sensors_Apple),
    ('Apple', 'System', system_Apple),
    ('Apple', 'Network', network_Apple),
    ('Apple', 'Battery', battery_Apple),
    ('Apple', 'Audio', audio_Apple),
    ('Samsung', 'Colors', colors_Samsung),
    ('Samsung', 'Capacity', capacity_Samsung),
    ('Samsung', 'Dimensions', dimensions_Samsung),
    ('Samsung', 'Screen', screen_Samsung),
    ('Samsung', 'Processor', processor_Samsung),
    ('Samsung', 'Camera', camera_Samsung),
    ('Samsung', 'Sensors', sensors_Samsung),
    ('Samsung', 'System', system_Samsung),
    ('Samsung', 'Network', network_Samsung),
    ('Samsung', 'Battery', battery_Samsung),
    ('Samsung', 'Audio', audio_Samsung)
]

# Create DataFrame
df = pd.DataFrame(data, columns=['Brand', 'Type', 'Value'])

# Save to an Excel File
df.to_excel('data.xlsx', index=False)

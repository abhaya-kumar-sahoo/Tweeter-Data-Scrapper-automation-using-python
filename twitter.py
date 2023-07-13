import json
import os
import shutil
import zipfile

import pymongo as pymongo
import react as react
from pyasn1.compat.octets import null
from pymongo import MongoClient
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import pyautogui
import webbrowser

from selenium.webdriver.common.keys import Keys

chrome_options = Options()

# Specify the path to the browser profile
chrome_options.add_argument("--user-data-dir=/Users/abhaya/Library/Application Support/Google/Chrome/Default/")
chrome_options.add_argument('--auto-open-devtools-for-tabs')

# Create a new instance of the Chrome driver
driver = webdriver.Chrome(options=chrome_options)

driver.maximize_window()



# Open a URL in the Chrome browser
url = 'https://www.twitter.com/login'
driver.get(url)
time.sleep(4)

isFirstLoop= True;

def callPasswordfun() :
    password_field1 = driver.find_elements(By.NAME, "password")
    password_field1[0].send_keys('YOUR-Password-XXXXXXXXX')
    time.sleep(4)
    login_button1 = driver.find_elements(By.CSS_SELECTOR,".css-1dbjc4n.r-sdzlij.r-1phboty.r-rs99b7.r-19yznuf.r-64el8z")
    time.sleep(2)
    login_button1[0].click()
def usenameFunction():
    password_field = driver.find_elements(By.TAG_NAME, "input")
    password_field[0].send_keys('YOUR-Username-XXXXXXXXXX')
    time.sleep(4)
    login_button = driver.find_elements(By.CSS_SELECTOR,".css-1dbjc4n.r-sdzlij.r-1phboty.r-rs99b7.r-19yznuf.r-64el8z")
    time.sleep(2)
    login_button[0].click()

def emailLogin():
    input_element = driver.find_element(By.TAG_NAME, "input")
    input_element.send_keys('YOUR-email-XXXXXXXXXXXX')
    time.sleep(2)
    input_button = driver.find_element(By.CSS_SELECTOR, ".css-18t94o4.css-1dbjc4n.r-sdzlij.r-1phboty.r-rs99b7.r-ywje51.r-usiww2.r-2yi16.r-1qi8awa.r-1ny4l3l.r-ymttw5.r-o7ynqc.r-6416eg.r-lrvibr.r-13qz1uu")
    input_button.click()
    check = null
    try:
        check = driver.find_elements(By.CSS_SELECTOR,
                                     ".r-30o5oe.r-1niwhzg.r-17gur6a.r-1yadl64.r-deolkf.r-homxoj.r-poiln3.r-7cikom.r-1ny4l3l.r-t60dpp.r-1dz5y72.r-fdjqy7.r-13qz1uu")
    except:
        check = []
    if (len(check) > 0):
        callPasswordfun()
        print("check", check)

    else:
        print("check-888", check)
        time.sleep(2)
        usenameFunction()
        time.sleep(3)
        callPasswordfun()



def PointerClick():
    screen_width, screen_height = pyautogui.size()

    if isFirstLoop:
        relative_x = int(screen_width * 0.58)  # 50% of the screen width
        relative_y = int(screen_height * 0.4)  # 50% of the screen height
        time.sleep(2)
        # select resources tab
        pyautogui.click(x=relative_x, y=relative_y)
        pyautogui.click(x=relative_x, y=relative_y)
        pyautogui.click(x=relative_x, y=relative_y)
        time.sleep(2)
        ########################################################################
        # box selection
        relative_x = int(screen_width * 0.03)  # 50% of the screen width
        relative_y = int(screen_height * 0.54)  # 50% of the screen height
        pyautogui.click(x=relative_x, y=relative_y)
        time.sleep(1)

        relative_x = int(screen_width * 0.03)  # 50% of the screen width
        relative_y = int(screen_height * 0.64)  # 50% of the screen height
        pyautogui.click(x=relative_x, y=relative_y)
        time.sleep(1)

        relative_x = int(screen_width * 0.03)  # 50% of the screen width
        relative_y = int(screen_height * 0.67)  # 50% of the screen height
        pyautogui.click(x=relative_x, y=relative_y)
        time.sleep(1)

        relative_x = int(screen_width * 0.03)  # 50% of the screen width
        relative_y = int(screen_height * 0.71)  # 50% of the screen height
        pyautogui.click(x=relative_x, y=relative_y)
    ############################################################################
    else:
        relative_x = int(screen_width * 0.7)  # 50% of the screen width
        relative_y = int(screen_height * 0.8)  # 50% of the screen height
        pyautogui.click(x=relative_x, y=relative_y)

    time.sleep(15)
    path = os.path.join(os.path.expanduser("~"), "Downloads", "twitter.com.zip")
    path1 = os.path.join(os.path.expanduser("~"), "Downloads", "twitter.com")
    if os.path.exists(path):
        os.remove(path)

    if os.path.exists(path1):
        # os.chmod(path1, 0o777)
        shutil.rmtree(path1)

        # os.remove(path1)

    # save file
    relative_x = int(screen_width * 0.9)  # 50% of the screen width
    relative_y = int(screen_height * 0.48)  # 50% of the screen height
    pyautogui.click(x=relative_x, y=relative_y)
    time.sleep(10)

    # extract file
    # relative_x = int(screen_width * 0.1)  # 50% of the screen width
    # relative_y = int(screen_height * 0.88)  # 50% of the screen height
    # pyautogui.click(x=relative_x, y=relative_y)

    zip_file_path = os.path.join(os.path.expanduser("~"), "Downloads", "twitter.com.zip")
    extract_destination = '/Users/abhaya/Downloads'

    # Open the zip file
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        # Extract all files and directories to the specified destination
        zip_ref.extractall(extract_destination)

def UploadToMongodb():
    # Establish a connection to the MongoDB server
    client = MongoClient('YOUR-MONGODB-DATABASE-URL-XXXXXXXXXXXXXX')

    # Select the database and collection
    db = client['tweeterdata']
    collection = db['tweeterdata']
    # file_name = os.path.join(os.path.expanduser("~"), "Downloads/twitter.com/i/api/graphql/Uv42IObcWFhsgKHYEh5Brw",
    #                          "HomeTimeline.json")

    graph_folder = "/Users/abhaya/Downloads/twitter.com/i/api/graphql"

    max_size = 0
    max_size_file = ""

        # Iterate over each folder within the graph folder
    for folder_name in os.listdir(graph_folder):
            folder_path = os.path.join(graph_folder, folder_name)

            # Check if the current item is a folder
            if os.path.isdir(folder_path):
                # Iterate over the files within the folder
                for file_name in os.listdir(folder_path):
                    file_path = os.path.join(folder_path, file_name)

                    # Check if the current item is a JSON file
                    if file_name.endswith(".json") and os.path.isfile(file_path):
                        # Get the size of the file
                        file_size = os.path.getsize(file_path)

                        # Update the maximum size and file path if necessary
                        if file_size > max_size:
                            max_size = file_size
                            max_size_file = file_path

    print("File with the largest size:", max_size_file)
    print("Size:", max_size, "bytes")




    # Open the JSON file and load its contents
    with open(max_size_file) as file:
        json_data = json.load(file)

        # Insert the JSON data into the collection
    collection.insert_one(json_data)
    print('JSON data uploaded successfully.')

        # Close the connection
    client.close()

def StartAutomation():
    profile_element = null
    try:
        profile_element = driver.find_element(By.CSS_SELECTOR, ".css-1dbjc4n.r-172uzmj.r-1pi2tsx.r-1ny4l3l.r-13qz1uu")
    except:
        profile_element = null
    if (profile_element):
        print("ABHAYA", profile_element)
        PointerClick()
    else:
        print("Not found")
        emailLogin()


def ExecuutionSteps():
    time.sleep(2)
    StartAutomation()
    print("Uploading......")
    time.sleep(3)
    UploadToMongodb()

while True:
    ExecuutionSteps()
    print("Looping......")

    time.sleep(30)
    driver.refresh()
    isFirstLoop = False
    print("Looping...ending...")


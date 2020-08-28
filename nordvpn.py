import sys
import traceback
import urllib

# import aggregate as aggregate
from base64 import b64encode
from builtins import set
from multiprocessing.dummy import Process

# import PROXY as PROXY
# import UserAgent as UserAgent
import self as self
import urllib3
import re
import os
# from ml.models import *
from bs4     import BeautifulSoup as bs, BeautifulSoup
import requests
import time
import datetime
import multiprocessing

# from fake_useragent import UserAgent
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities, Proxy, ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.proxy import ProxyType
import geckodriver_autoinstaller

# from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC, expected_conditions

from fake_useragent import UserAgent
def my_proxy(port, user_name, password, ip_add):
    # print(user_name)
    # geckodriver_autoinstaller.install()
    headers = {'User-Agent': UserAgent().random}
    fp = webdriver.FirefoxProfile()

    # fp.add_argument("--headless")

    fp.set_preference("network.proxy.type", 1)
    fp.set_preference("network.proxy.http", str(ip_add))
    fp.set_preference("network.proxy.http_port", int(port))
    fp.set_preference("network.proxy.ssl", str(ip_add))
    # fp.
    # fp.set_preference("-headless")
    fp.set_preference("network.proxy.ssl_port", int(port))
    fp.set_preference("network.proxy.ftp", str(ip_add))
    fp.set_preference("network.proxy.ftp_port", int(port))
    fp.set_preference("network.proxy.socks", str(ip_add))
    fp.set_preference('network.proxy.noproxy','aSFasfa')
    fp.set_preference("network.proxy.socks_port", int(port))
    fp.set_preference("browser.cache.disk.enable", False)
    fp.set_preference("browser.cache.memory.enable", False)
    fp.set_preference("browser.cache.offline.enable", False)
    fp.set_preference("network.http.use-cache", False)
    fp.set_preference("network.proxy.Username",str(user_name))
    fp.set_preference("network.proxy.Password", str(password))
    # fp.set_preference("general.useragent.override",UserAgent().random)
    fp.update_preferences()

    try:
        # browser = webdriver.Firefox(firefox_profile=fp)
        browser = webdriver.Firefox(executable_path='driver/geckodriver', firefox_profile=fp)
        time.sleep(2)
        browser.get("https://ident.me/")
        time.sleep(5)
        # browser.find_element_by.send_keys("asdd")
        # browser.get("http://fbaileyiii@gmail.com:213500DN@ident.me/basic_auth")
        # browser.get("https://ident.me/")
        wait(browser, 5).until(EC.alert_is_present())
        # time.sleep(2)
        alert = browser.switch_to_alert()
        # print(alert.)
        # time.sleep(1)
        # alert.send_keys('xxxxx')
        # alert.send_keys(Keys.TAB)
        # alert.send_keys('yyyy')
        # browser.switch_to.alert.send_keys(user_name + Keys.TAB + password)
        # browser.switch_to.alert.accept()
        # alert=browser.switch_to().alert()
        # alert = browser.switch_to_alert()
        print("1234567")
        # alert.send_keys(user_name + Keys.TAB + password)
        time.sleep(2)
        print("fraz")
        alert.accept()
        time.sleep(20)

        # browser.get("https://ident.me/")
        # time.sleep(5)
        # if browser.title=='Problem loading page':
        #     print("Here")
        #     browser.quit()
        # else:pass
        browser.get("https://ident.me/")

    except Exception as e:
        print(e.__str__())
        traceback.print_exc()
        browser.quit()

    return browser
def login(browser):
    # browser=from_browser()
    browser.get("https://www.facebook.com/")
    username = browser.find_element_by_id("email")
    time.sleep(5)
    password = browser.find_element_by_id("pass")
    time.sleep(3)
    submit = browser.find_element_by_id("loginbutton")
    time.sleep(2)
    username.send_keys("gradyhenderson13@outlook.com")
    password.send_keys("grady13")
    # Step 4) Click Login
    submit.click()
    time.sleep(2)
    return browser


def main(ip_add,browser):#(s,n):
    browser=login(browser)
    time.sleep(5)
    print("login")
    # for data in csvreader(path)[s:n]:
    #     split=(str(data).split("category/")[1])[:-1]
    #     category=split.replace("-"," ")
    #     # print(category)
    category="ecommerce-website"
    page=1
    data="https://www.facebook.com/pages/category/ecommerce-website/"
    while True:
        try:
            if browser.title=="Page not found | Facebook":
                print("asd")
                break
            else:
                if str(ip_add)=='73.137.12.79':
                    print("Stoppppppppppppppppppppp")
                    break
                else:
                    browser.get(data+"?page="+str(page))
                    if browser.title=="Facebook":
                        break
                    else:
                        # browser.get(data+"?page="+str(page))
                        print(browser.title)
                        soup = BeautifulSoup(browser.page_source, 'html.parser')
                        for maindiv in soup.find_all('div', {'class': '_4-u2 _6x0a _4-u8'}):
                            # print(maindiv)
                            like_div=maindiv.find('div',{'class':'_6x0f rfloat _ohf'})
                            next_div=like_div.find_next('div')
                            # print(next_div.text)

                            try:
                                imgdiv=maindiv.find('div',{'class':'_4bl7 _6x0b'})
                                imglink=imgdiv.find('a')
                                link=imglink['href']
                                print("Page Link=>  "+str(link))
                            except:
                                link=" "
                            # try:
                            #     image=imgdiv.find('img')
                            #     imagelink=image['src']
                            #     # print("Image => "+str(imagelink))
                            # except:
                            #     imagelink=" "
                            # try:
                            #     nameanchor=maindiv.find('a',{'class':'_6x0d'})
                            #     name=nameanchor.text
                            #     # print("Title => "+str(name))
                            # except:
                            #     name=""
                            # try:
                            #     des=maindiv.find('div',{'class':'_ajw'})
                            #     desriction=des.text
                            #     # print("Description =>   "+str(desriction))
                            # except:
                            #     desriction=""
                            # try:
                            #     alldes=maindiv.find('div',{'class':'_4bl9'})
                            #     alldescription=alldes.text
                            #     # print("All Description =>   "+str(alldescription))
                            # except:
                            #     alldescription=""

                            # try:
                            #     query_obj = Category.objects.filter(category_name=category)
                            #     # print(query_obj.exists())
                            #     if query_obj.exists() == True:
                            #         query_obj = query_obj[0]
                            #         # print(query_obj)
                            #         print('category already exists')
                            #     else:
                            #         query_obj = Category(category_name=category)
                            #         # print(query_obj)
                            #         query_obj.save()
                            #         print('category save')
                            #     facebook_obj = Advertisers.objects.filter(fb_page_link=link).first()
                            #     if facebook_obj == None:
                            #         print("new object")
                            #         getid = query_obj.id
                            #         facebooksave = Advertisers(
                            #             category=Category(str(getid)),
                            #             page_name=str(name),
                            #             fb_page_link=str(link),
                            #
                            #         )
                            #         facebooksave.save()
                            #         print("save////////////////////////")
                            # except Exception as e:
                            #     print(e.__str__())
                            #     traceback.print_exc()

                            # print("//////////////////////////////////*****************************///////////////////////")
        except:
            pass
        page=page+1



my_proxy(80,'fbaileyiii@gmail.com','213500DN','us6233.nordvpn.com')
import json
req=requests.get("https://nordvpn.com/wp-admin/admin-ajax.php?action=servers_recommendations&filters={%22country_id%22:228}")
json_convert=json.loads(req.text)
# print(json_convert)
for data in json_convert:
    try:
        server_name=data['hostname']
        print(server_name)
        browser=my_proxy(80, 'fbaileyiii@gmail.com', '213500DN','us4667.nordvpn.com')
        soup=BeautifulSoup(browser.page_source,'lxml')
        ip_add=soup.text
        print(ip_add)
        main(ip_add,browser)
        browser.quit()
    except:
        pass
 # fp.add_argument("--headless")
    # fp.set_preference("network.proxy.type", 1)
    # fp.set_preference("network.proxy.https", str(ip_add))
    # fp.set_preference("network.proxy.https_port", int(port))
    # fp.set_preference("network.proxy.ssl", str(ip_add))
    # # fp.set_preference("-headless")
    # fp.set_preference("network.proxy.ssl_port", int(port))
    #
    # fp.set_preference("browser.cache.disk.enable", False)
    # fp.set_preference("browser.cache.memory.enable", False)
    # fp.set_preference("browser.cache.offline.enable", False)
    # fp.set_preference("network.http.use-cache", False)
    # fp.set_preference("general.useragent.override",UserAgent().random)
    # fp.update_preferences()

import re
import os
import time
from selenium.webdriver.support import expected_conditions as EC
import json
import requests
import django
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

os.environ['DJANGO_SETTINGS_MODULE'] = 'Active_Adds.settings'
django.setup()
from Advertisement.models import Category,Advertisers


def Get_PageID(link):
        result = requests.get(str(link))#, proxies=proxies, headers=headers)
        try:
            result = result.text
            profile_id = re.search(r"page_id=[0-9]+", result)
            profile_id = re.search(r"[0-9]+", profile_id.group()).group()
            # print(profile_id)
            if profile_id!="None":

                # FacebookDatapages.objects.filter(pk=getid).update(page_id=profile_id)
                print(profile_id)
                print("save")
                # return profile_id
                # break

                # pass
            else:
                pass

        except:
            pass

# for data in FacebookDatapages.objects.values('fb_page_link'):
#     link=data['fb_page_link']
#     print(Get_PageID(link))


def selenium_pageid(name,get_id):
    CHROMEDRIVER_PATH = "driver/chromedriver"

    from pyvirtualdisplay import Display
    display = Display(visible=0, size=(1024, 768))
    display.start()
    # # vdisplay = xvfbwrapper.Xvfb()
    # vdisplay.start()

    # launch stuff inside virtual display here

    # vdisplay.stop()
    chromeoptions = webdriver.ChromeOptions()
    chromeoptions.add_argument('--disable-notifications')
    chromeoptions.add_argument('--disable-dev-shm-usage')
    chromeoptions.add_argument('--shm-size=2g')
    chromeoptions.add_argument('--no-sandbox')
    chromeoptions.add_argument('--headless')
    chromeoptions.add_argument('--ignore-certificate-errors')
    browser = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH, chrome_options=chromeoptions)

    # browser=from_browser()
    while True:
        try:
            browser.get("https://lookup-id.com/#")
            browser.find_element_by_xpath("/html/body/div[4]/form/header/div/div[1]/div/input[1]").send_keys(str(name))
            browser.find_element_by_xpath("/html/body/div[4]/form/header/div/div[1]/div/input[2]").click()
            time.sleep(5)
            test=browser.find_element_by_xpath("/html/body/div[4]/form/header/div/div[3]/div/p[2]/span[1]").text
            # FacebookDatapages.objects.filter(pk=get_id).update(page_id=test)
            print("save")
            break
        except:
            pass
if __name__ == '__main__':
    def from_browser():
        # from pyvirtualdisplay import Display
        # display = Display(visible=0, size=(1024, 768))
        # display.start()
        # # vdisplay = xvfbwrapper.Xvfb()
        # vdisplay.start()

        browser = webdriver.Firefox(executable_path="driver/geckodriver1")
        return browser

    def test(s,n):
        from selenium.webdriver.common.keys import Keys
        browser=from_browser()
        browser.get("https://megritools.com/bulk-facebook-id-finder")

        for data in Advertisers.objects.values('fb_page_link').order_by("id")[s:n]:
            print(str(data['fb_page_link']))
        # browser.find_element_by_css_selector("#linksBox").send_keys(str(data['fb_page_link'])+Keys.ENTER)
        # browser.find_element_by_css_selector("#checkButton").click()
        # time.sleep(30)
        # soup=BeautifulSoup(browser.page_source, 'lxml')
        #
        # for table in soup.find_all('table',{'id':'resTable'}):
        #     num=0
        #     for tr in table.find_all('tr')[1:]:
        #         # td = tr.find_all('td')
        #         link=tr.find('td',{'id':'link-'+str(num)})
        #         print(link.text)
        #         page_number=tr.find('td',{'id':'status-'+str(num)}).text
        #         print(page_number)
        #         num=num+1


    # test(1,25)

    def get_link(s,n):
        browser = from_browser()

        print("HERE")
        browser.get("https://megritools.com/bulk-facebook-id-finder")
        for data in Advertisers.objects.values('id','fb_page_link').filter(fb_page_id__isnull=True).order_by("id")[s:n]:

            browser.get("https://megritools.com/bulk-facebook-id-finder")
            print(data['fb_page_link'])
            browser.find_element_by_css_selector("#linksBox").send_keys(str(data['fb_page_link']))
            browser.find_element_by_css_selector("#checkButton").click()
            try:
                element_present = EC.presence_of_element_located((By.XPATH, '//*[@id="status-0"]/b'))
                WebDriverWait(browser, 50).until(element_present)
                page_id=browser.find_element_by_xpath("//*[@id='status-0']").text
                print(page_id)
                # obj = Advertisers.objects.get(pk=data['id'])
                # obj.fb_page_id = str(page_id)
                # obj.save()

                # facebooksave = Advertisers.(
                #     fb_page_id=str(page_id)
                #
                # )
                # facebooksave.save()
                print("save////////////////////////")
            except TimeoutException:
                print(element_present)
                "Timed out waiting for page to load"

    def hots_name(country_id):
        host_name_list=[]
        req = requests.get("https://nordvpn.com/wp-admin/admin-ajax.php?action=servers_recommendations&filters={%22country_id%22:"+str(country_id)+"}")
        json_convert = json.loads(req.text)
        # print(json_convert)
        for data in json_convert:
            try:
                server_name = data['hostname']
                host_name_list.append(server_name)
                # print(server_name)
            except:
                pass
        return host_name_list


    # get_link(0,10)
    from multiprocessing import Process

    # starttime = time.time()
    # processes = []
    # start = 0
    # end = 600
    # for i in range(0, 10):
    #     p = Process(target=get_link, args=(start, end,))
    #     processes.append(p)
    #     start = end
    #     end = end + 600
    #     p.start()
    #     time.sleep(2)
    # for process in processes:
    #     process.join()
    #     time.sleep(2)
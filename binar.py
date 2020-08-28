import json
import time
import traceback
from datetime import time

import requests
import tabs as tabs
from numpy.testing._private.parameterized import param
from selenium.webdriver import Proxy
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.proxy import ProxyType
from selenium.webdriver.support.ui import WebDriverWait as wait
# from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support import expected_conditions as EC, expected_conditions
from selenium import webdriver
# def my_proxy(port, user_name, password, ip_add):
#     fp = webdriver.FirefoxProfile()
#
#     # fp.add_argument("--headless")
#
#     fp.set_preference("network.proxy.type", 1)
#     fp.set_preference("network.proxy.http", str(ip_add))
#     fp.set_preference("network.proxy.http_port", int(port))
#     fp.set_preference("network.proxy.ssl", str(ip_add))
#     # fp.
#     # fp.set_preference("-headless")
#     fp.set_preference("network.proxy.ssl_port", int(port))
#     fp.set_preference("network.proxy.ftp", str(ip_add))
#     fp.set_preference("network.proxy.ftp_port", int(port))
#     fp.set_preference("network.proxy.socks", str(ip_add))
#     fp.set_preference('network.proxy.noproxy','aSFasfa')
#     fp.set_preference("network.proxy.socks_port", int(port))
#     fp.set_preference("browser.cache.disk.enable", False)
#     fp.set_preference("browser.cache.memory.enable", False)
#     fp.set_preference("browser.cache.offline.enable", False)
#     fp.set_preference("network.http.use-cache", False)
#     fp.set_preference("network.proxy.socksUsername",str(user_name))
#     fp.set_preference("network.proxy.socksPassword", str(password))
#     # fp.set_preference("general.useragent.override",UserAgent().random)
#     fp.update_preferences()
#
#
#     # browser = webdriver.Firefox(firefox_profile=fp)
#     browser = webdriver.Firefox(executable_path='driver/geckodriver', firefox_profile=fp)
#     # time.sleep(2)
#     browser.get("https://ident.me/")
#     time.sleep(2)
#     # Alert(browser).send_keys("WillianShakesphere")
#     # Alert(browser).accept()
#     Alert(browser).send_keys(Keys.TAB)
#     time.sleep(123)
#
#
#     # alert = browser.switch_to_alert()
#     # alert.send_keys(user_name + Keys.TAB + password)
#     # time.sleep(2)
#     # print("fraz")
#     # alert.accept()
#     # time.sleep(20)



# my_proxy(80, 'fbaileyiii@gmail.com', '213500DN','us4667.nordvpn.com')

# PROXY = "us4667.nordvpn.com:80"
# webdriver.DesiredCapabilities.FIREFOX['proxy'] = {
#     "httpProxy": PROXY,
#     "ftpProxy": PROXY,
#     "sslProxy": PROXY,
#     # "noProxy": None,
#     "proxyType": "MANUAL",
# }
# driver = webdriver.Firefox(executable_path="driver/geckodriver")
# driver.get('http://www.whatsmyip.org/')

# from seleniumwire import webdriver
# # from selenium import webdriver
#
# proxy= "http://fbaileyiii@gmail.com:213500DN@us6233.nordvpn.com:80"
# options = {'proxy': {'http': proxy, 'https': proxy, 'no_proxy': 'localhost,127.0.0.1,dev_server:8080'}}
# # driver = webdriver.Firefox(executable_path="driver/geckodriver")
# try:
#     driver = webdriver.Firefox(seleniumwire_options=options, executable_path="driver/geckodriver")
#
#     driver.get('https://ident.me/')
#     time.sleep(2)
#     # driver.get('https://www.facebook.com/')
#     print(driver.get_cookies())
# except Exception as e:
#     print(e)
#


import requests

url = 'https://members.helium10.com/black-box/set-filters'


# payload={'page':2}

# headers={
# "x-csrf-token": "azjEP_k-xxDXen3MrujEch-1kJX8V-BMHM48VeSM2iECTbd6yWmvRoYZPqWaopE8V-qop6wyg3hNvX1m1MSAUw==",
# "cookie":"_gcl_au=1.1.531741439.1597102673; _ga=GA1.2.807547068.1597102673; _gid=GA1.2.531315018.1597102673; _vwo_uuid_v2=D2C38ED23BF0421E409772CF32A4CF208|59def9806c9b87e5e5b0eb8b684ee1ef; _fbp=fb.1.1597102674147.1891569070; _ga=GA1.3.807547068.1597102673; _gid=GA1.3.531315018.1597102673; ab.storage.userId.4d3ca359-c724-43de-9b97-cb9f1fee4769=%7B%22g%22%3A%221543602669%22%2C%22c%22%3A1597103330623%2C%22l%22%3A1597103330623%7D; ab.storage.deviceId.4d3ca359-c724-43de-9b97-cb9f1fee4769=%7B%22g%22%3A%2270317be7-7217-1bdd-b1aa-c767529ec122%22%2C%22c%22%3A1597103330629%2C%22l%22%3A1597103330629%7D; ajs_anonymous_id=%2288468397-99f5-4be0-80ce-8f34a5547a9e%22; ajs_user_id=%221543602669%22; current-marketplace=5a7deede86e62213f2adae2c21dde37c8919c5317898e27c859a9080214c380fa%3A2%3A%7Bi%3A0%3Bs%3A19%3A%22current-marketplace%22%3Bi%3A1%3Bs%3A13%3A%22ATVPDKIKX0DER%22%3B%7D; __stripe_mid=dba22044-06b7-464f-9b5a-03f5dc2bae017d06e5; _vis_opt_s=2%7C; _vis_opt_test_cookie=1; _identity=2ed3df042cd61bdd5d967a384b046097a3fe69b9f9d15ce1021004202410b825a%3A2%3A%7Bi%3A0%3Bs%3A9%3A%22_identity%22%3Bi%3A1%3Bs%3A81%3A%22%5B1543602669%2C%229iTOup4P6YThPl2lP4OPdwIs23dBThCH%22%2C2592000%2Cnull%2Cnull%2C%2239.42.162.197%22%5D%22%3B%7D; _csrf=4f171c0e6146399bf0aa824d12edbed1b6843169a6adc397385e433322eb4485a%3A2%3A%7Bi%3A0%3Bs%3A5%3A%22_csrf%22%3Bi%3A1%3Bs%3A32%3A%22iusE0WhVQcCi4JUNH_82Pec4QsA30HZr%22%3B%7D; sidebar=10e72d2c5fa6bd03252eaf0d9f87e2bc1020bb80d5d174d7a4a3ed09e7a80426a%3A2%3A%7Bi%3A0%3Bs%3A7%3A%22sidebar%22%3Bi%3A1%3Bs%3A0%3A%22%22%3B%7D; amplitude_idundefinedhelium10.com=eyJvcHRPdXQiOmZhbHNlLCJzZXNzaW9uSWQiOm51bGwsImxhc3RFdmVudFRpbWUiOm51bGwsImV2ZW50SWQiOjAsImlkZW50aWZ5SWQiOjAsInNlcXVlbmNlTnVtYmVyIjowfQ==; GleamId=OQXWz%3D2%201%40DIf%3Ch!A; ab.storage.sessionId.4d3ca359-c724-43de-9b97-cb9f1fee4769=%7B%22g%22%3A%229cb499f7-9698-bde7-990e-db265407f6b7%22%2C%22e%22%3A1597186702654%2C%22c%22%3A1597184428661%2C%22l%22%3A1597184902654%7D; _uetsid=8e467b894d64934b4c7b68658488a1a2; _uetvid=b76ad12c7103919583e4cbb7b6403cea; amplitude_id_95d3abbefaf19863dc230d5449736018helium10.com=eyJkZXZpY2VJZCI6IjdlODRjNjk5LWJhYmEtNDExYi04MTg0LWNkZjVhYjAxNzM5OVIiLCJ1c2VySWQiOiIxNTQzNjAyNjY5Iiwib3B0T3V0IjpmYWxzZSwic2Vzc2lvbklkIjoxNTk3MTg0ODUyMTUzLCJsYXN0RXZlbnRUaW1lIjoxNTk3MTg0OTAzNjU2LCJldmVudElkIjoyOCwiaWRlbnRpZnlJZCI6NDUsInNlcXVlbmNlTnVtYmVyIjo3M30=; AWSALB=yWmnGFEUoR4d72k8waRm6bQKZCwrS8P3birWKnJzTdWcP04B7whGvtEVsap//M9DCjfEc2ZAf3PnicASlQAwq3B9nwuDCslHCktpNZFkIQEFIzncO0guBU+BJ2Up; AWSALBCORS=yWmnGFEUoR4d72k8waRm6bQKZCwrS8P3birWKnJzTdWcP04B7whGvtEVsap//M9DCjfEc2ZAf3PnicASlQAwq3B9nwuDCslHCktpNZFkIQEFIzncO0guBU+BJ2Up; io=gTuyh5imrivJy-FVFt7f; intercom-session-yzizpoku=ZmxNdkxxYWFUazc2L013d1V1TWs3NXlOZkVjaGVPNkJPKzZqVzhCbXJBYS9VbmN4bHBNS3hhY3dRN1dQbVMyYy0tR1lRM2cwT21Wd3JhdUxKalBScm9wZz09--48757420da98d8d7859c6d63b5f90e5133ab7d6a; sid=bhd3n1buqj8qle2iakrm6gm5cb"
#
# }
# x = requests.post(url, data = myobj,headers=headers)
# &sortBy=default
# x=requests.post("https://members.helium10.com/black-box?searchId=c7fc76e264c1df362d4a4bc0912860c0&marketplace=ATVPDKIKX0DER&page=1&_pjax=%23black-box-pjax", data=payload,headers=headers)
# x=requests.post("https://members.helium10.com/black-box?searchId=ad01e49a586345a580aadeeb62dfcae9&marketplace=ATVPDKIKX0DER&page=1&_pjax=%23black-box-pjax",headers=headers)
# print(x.text)

headers={

"x-csrf-token": "QCeSXkF-cQJcA02Z60l5vZqTC8cIBHnVZtMp4ord5sQZUsQLGUoQTmRRKd2NHk3l0dRBjGMxEYFRqXCj5auXgQ==",
"cookie":"__distillery=b1c4564_2aa5f5a3-cdb9-4d44-95c0-488a8db3991c-5be6dbb20-2e53b3a324b4-dabb; _csrf=c2a7d8649e34a76da9ed74b0d079b83d7e2687d755179d8d5eae7bf264445715a%3A2%3A%7Bi%3A0%3Bs%3A5%3A%22_csrf%22%3Bi%3A1%3Bs%3A32%3A%22YuVUX4aL8RdDfW4XKGJKk5hT7zYAovqE%22%3B%7D; 7879928_viewed_6=3; cf:aff_sub=; cf:aff_sub2=; cf:aff_sub3=; cf:affiliate_id=; cf:cf_affiliate_id=; cf:content=; cf:medium=; cf:MzI1MDAyMzg=:visited=true; cf:name=; cf:source=; cf:term=; cf:visitor_id=c83857f0-992c-43c9-8e7c-97848fe39909; current-marketplace=5a7deede86e62213f2adae2c21dde37c8919c5317898e27c859a9080214c380fa%3A2%3A%7Bi%3A0%3Bs%3A19%3A%22current-marketplace%22%3Bi%3A1%3Bs%3A13%3A%22ATVPDKIKX0DER%22%3B%7D; GleamId=OQXWzZ89*GH6%20NAX_; sidebar=10e72d2c5fa6bd03252eaf0d9f87e2bc1020bb80d5d174d7a4a3ed09e7a80426a%3A2%3A%7Bi%3A0%3Bs%3A7%3A%22sidebar%22%3Bi%3A1%3Bs%3A0%3A%22%22%3B%7D; zvtgmpc9mr382nb2=true; _identity=3c23f0d9df2188aa1595f78e60b7ddfb5f87465ba168c282f785f8e957d14b79a%3A2%3A%7Bi%3A0%3Bs%3A9%3A%22_identity%22%3Bi%3A1%3Bs%3A81%3A%22%5B1543613976%2C%22Gsm-Nxe-_FQ4WcGrt8cBxH05X8qEV4eX%22%2C2592000%2Cnull%2Cnull%2C%2239.53.254.174%22%5D%22%3B%7D; _gcl_au=1.1.1622150552.1597935794; ab.storage.userId.4d3ca359-c724-43de-9b97-cb9f1fee4769=%7B%22g%22%3A%221543613976%22%2C%22c%22%3A1597935794254%2C%22l%22%3A1597935794254%7D; _ga=GA1.3.355721092.1597935795; _gid=GA1.3.1156987563.1597935795; _fbp=fb.1.1597935794655.5047329; ajs_user_id=%221543613976%22; ajs_anonymous_id=%220cf4ecda-56ac-471c-9b6d-57d44c1d0c71%22; amplitude_idundefinedhelium10.com=eyJvcHRPdXQiOmZhbHNlLCJzZXNzaW9uSWQiOm51bGwsImxhc3RFdmVudFRpbWUiOm51bGwsImV2ZW50SWQiOjAsImlkZW50aWZ5SWQiOjAsInNlcXVlbmNlTnVtYmVyIjowfQ==; sid=8t5vfiob5uk5itltilbm5090o8; ab.storage.sessionId.4d3ca359-c724-43de-9b97-cb9f1fee4769=%7B%22g%22%3A%228ddc50ac-6769-ed63-8218-ccd11197e7e9%22%2C%22e%22%3A1597942440662%2C%22c%22%3A1597940640664%2C%22l%22%3A1597940640664%7D; _dc_gtm_UA-75738827-2=1; _uetsid=53a3080b8bfad53742cc5e50e735407a; _uetvid=b76ad12c7103919583e4cbb7b6403cea; amplitude_id_95d3abbefaf19863dc230d5449736018helium10.com=eyJkZXZpY2VJZCI6ImM2YzkyYzQzLTY4ZDEtNGNmMy1hZGExLTg4ZjNiNzkzMWU5OVIiLCJ1c2VySWQiOiIxNTQzNjEzOTc2Iiwib3B0T3V0IjpmYWxzZSwic2Vzc2lvbklkIjoxNTk3OTQwNjQxODk0LCJsYXN0RXZlbnRUaW1lIjoxNTk3OTQwNjQxOTA5LCJldmVudElkIjoyLCJpZGVudGlmeUlkIjozLCJzZXF1ZW5jZU51bWJlciI6NX0=; AWSALB=ethHWN9rETs4uGvtIXaZlsCmUz0/40ytFgwPuD9zbexIZGkv9fKz5VeQvBA8/PUp0Fwebp+Y3aVpUJJfKM0rxjF0SJpKubaa6nW42znOXZHWspM4LogUE4XiPX+3; AWSALBCORS=ethHWN9rETs4uGvtIXaZlsCmUz0/40ytFgwPuD9zbexIZGkv9fKz5VeQvBA8/PUp0Fwebp+Y3aVpUJJfKM0rxjF0SJpKubaa6nW42znOXZHWspM4LogUE4XiPX+3; io=VeSNMxeiW0YzmUqrHe41; _gat_UA-75738827-2=1; intercom-session-yzizpoku=MTdWQ24yR2NWV3RIWU5ZQWtBb05ySlpLWHRQaUJjVEFxRk50ZGl2ei9QYnB3OUREbkpYamVRbnR4cHRhZXdnTi0tcmM0YWVrVkdZSlNmdEIzbFdEcGpoZz09--dd8030c4d814274b820967a2c4ba18b23599fb1a",
# "cookie":"cookie: __distillery=b1c4564_2aa5f5a3-cdb9-4d44-95c0-488a8db3991c-5be6dbb20-2e53b3a324b4-dabb; _csrf=223555e8937e85652fa2ed726e50f9fd3081d9ab9a6507514c1b18e8fbef1042a%3A2%3A%7Bi%3A0%3Bs%3A5%3A%22_csrf%22%3Bi%3A1%3Bs%3A32%3A%22QOC-0duynt0tjhSJVfcZZOvY2CTbpIap%22%3B%7D; 7879928_viewed_6=3; cf:aff_sub=; cf:aff_sub2=; cf:aff_sub3=; cf:affiliate_id=; cf:cf_affiliate_id=; cf:content=; cf:medium=; cf:MzI1MDAyMzg=:visited=true; cf:name=; cf:source=; cf:term=; cf:visitor_id=c83857f0-992c-43c9-8e7c-97848fe39909; current-marketplace=5a7deede86e62213f2adae2c21dde37c8919c5317898e27c859a9080214c380fa%3A2%3A%7Bi%3A0%3Bs%3A19%3A%22current-marketplace%22%3Bi%3A1%3Bs%3A13%3A%22ATVPDKIKX0DER%22%3B%7D; GleamId=OQXWz%60oXD%2C2W%3B_qqd; selected-token1543566769=6d445c2fe0b4221f065041849f1e8370f5083079915da33812065ed4ca307efaa%3A2%3A%7Bi%3A0%3Bs%3A24%3A%22selected-token1543566769%22%3Bi%3A1%3Bs%3A56%3A%22%7B%22seller%22%3A%22ANE1E3RZB3H97%22%2C%22marketplace%22%3A%22ATVPDKIKX0DER%22%7D%22%3B%7D; sidebar=10e72d2c5fa6bd03252eaf0d9f87e2bc1020bb80d5d174d7a4a3ed09e7a80426a%3A2%3A%7Bi%3A0%3Bs%3A7%3A%22sidebar%22%3Bi%3A1%3Bs%3A0%3A%22%22%3B%7D; zvtgmpc9mr382nb2=true; _identity=cb25587e68846306a4b7befd128368e8f265ec4a7b2c2af4462836b9980e04f6a%3A2%3A%7Bi%3A0%3Bs%3A9%3A%22_identity%22%3Bi%3A1%3Bs%3A80%3A%22%5B1543566769%2C%22OMbEQ6hdLOhr5LRhq12942co9H00yYTZ%22%2C2592000%2Cnull%2Cnull%2C%2239.42.130.68%22%5D%22%3B%7D; ab.storage.userId.4d3ca359-c724-43de-9b97-cb9f1fee4769=%7B%22g%22%3A%221543566769%22%2C%22c%22%3A1597676342738%2C%22l%22%3A1597676342738%7D; _gcl_au=1.1.647684886.1597676343; _ga=GA1.3.915262083.1597676343; _gid=GA1.3.1157446937.1597676343; _fbp=fb.1.1597676342975.1290933778; ajs_user_id=%221543566769%22; ajs_anonymous_id=%224d3fb65e-471a-480e-b39f-d62df6a890ab%22; amplitude_idundefinedhelium10.com=eyJvcHRPdXQiOmZhbHNlLCJzZXNzaW9uSWQiOm51bGwsImxhc3RFdmVudFRpbWUiOm51bGwsImV2ZW50SWQiOjAsImlkZW50aWZ5SWQiOjAsInNlcXVlbmNlTnVtYmVyIjowfQ==; ab.storage.sessionId.4d3ca359-c724-43de-9b97-cb9f1fee4769=%7B%22g%22%3A%22f26e6455-3936-4219-3ded-13ed369d2464%22%2C%22e%22%3A1597695299573%2C%22c%22%3A1597693499574%2C%22l%22%3A1597693499574%7D; _uetsid=50081bc059ad2678b8d010f17955e84e; _uetvid=b76ad12c7103919583e4cbb7b6403cea; amplitude_id_95d3abbefaf19863dc230d5449736018helium10.com=eyJkZXZpY2VJZCI6IjJmODlmYzlhLTJhZWMtNDRlYi05NGZjLTRjOTU2NGY3ODk3N1IiLCJ1c2VySWQiOiIxNTQzNTY2NzY5Iiwib3B0T3V0IjpmYWxzZSwic2Vzc2lvbklkIjoxNTk3NjkzNTAwODY5LCJsYXN0RXZlbnRUaW1lIjoxNTk3NjkzNTAwOTA0LCJldmVudElkIjoxNSwiaWRlbnRpZnlJZCI6MjQsInNlcXVlbmNlTnVtYmVyIjozOX0=; AWSALB=GrqTTjQ4hlDvRShfIfFP6DnL9ksEoOOsAQDeofqqXPvLVwgS4ZszAwZ4oM4tBUiwazCZtxXL1ytAvDNEfMKsK/J7w6+LzxqHcDITfMgud6n3IQHz5YRy/cqz+bRy; AWSALBCORS=GrqTTjQ4hlDvRShfIfFP6DnL9ksEoOOsAQDeofqqXPvLVwgS4ZszAwZ4oM4tBUiwazCZtxXL1ytAvDNEfMKsK/J7w6+LzxqHcDITfMgud6n3IQHz5YRy/cqz+bRy; io=mYepO6M9vu-f6hG9DmqR; intercom-session-yzizpoku=NUtTUUVqNTJkSTNnSFdmWWtDNUlXVnFpVy96QVpJWDBHWWQ0YW8vaXY2NmhaUFpsMVdDL28xZ0JvUjViSGQ5TC0tRlFlNmdZREw5MFVaTC9JV1YwMVRRQT09--b8148fcd7b7385fc9b11108e9b6c3b879dac6ccd; sid=1hksd4kb728rmhehp1gqlneprd",

}
# params={
# 'filters': '[{"id":"category","options":[1]},{"id":"monthlyRevenue","min":null,"max":null},{"id":"price","min":null,"max":null},{"id":"reviewCount","min":null,"max":null},{"id":"reviewRating","min":null,"max":null},{"id":"sizeTier","options":[]},{"id":"salesYearOverYear","min":null,"max":null},{"id":"priceChange","min":null,"max":null},{"id":"salesChange","min":null,"max":null},{"id":"bestMonth","value":null},{"id":"salesToReviews","min":null,"max":null},{"id":"monthlySales","min":null,"max":null},{"id":"salesRank","min":null,"max":null},{"id":"numberOfSellers","min":null,"max":null},{"id":"fulfillment","options":[]},{"id":"numberOfImages","min":null,"max":null},{"id":"variationCount","min":null,"max":null},{"id":"weight","min":null,"max":null},{"id":"age","min":null,"max":null},{"id":"reviewVelocity","min":null,"max":null},{"id":"titleKeyword","value":null},{"id":"titleExcludeKeyword","value":null}]'
# }


# params={
#   'filters': '[{"id":"category","options":[1,2,3]},{"id":"monthlyRevenue","min":1,"max":2},{"id":"price","min":12,"max":23},{"id":"reviewCount","min":1,"max":5},{"id":"reviewRating","min":1,"max":3},{"id":"sizeTier","options":[1,2,3]}'
# }
params={
  'filters':[{"id":"category","options":[1,2,3]},{"id":"monthlyRevenue","min":0,"max":2000},{"id":"price","min":12,"max":23},{"id":"reviewCount","min":1,"max":5},{"id":"reviewRating","min":1,"max":3},{"id":"sizeTier","options":[1,2,3]}]
}
# x=requests.post("https://members.helium10.com/black-box/set-filters",headers=headers,data=params)
# print(x.text)




x=requests.post("https://members.helium10.com/black-box?searchId=c02a7a8161d4bca0352ef587e858459c&marketplace=ATVPDKIKX0DER&page=1&_pjax=%23black-box-pjax&page=1",headers=headers)
# print(x.text)
from bs4 import BeautifulSoup
soup=BeautifulSoup(x.text,'lxml')
all_data=[]
for maindiv in soup.find_all('tbody'):
    for tr in maindiv.find_all('tr',{'class':'bb-product-row'}):
        td = tr.find_all('td')
        try:
            td_object_zero=td[0]
            media_body=td_object_zero.find('div',{'class':'media-body'})
            try:
                amazon_link_parse =td_object_zero.find('a',{'target':'_blank'})
                amazon_link=amazon_link_parse['href']
                # print(amazon_link)
            except:
                amazon_link=""
            try:
                image_parse=td_object_zero.find('img',{'class':'media-object'})
                image=image_parse['src']
                # print(image)
            except:
                image=""
            try:
                title_parse=media_body.find('h5')
                title=title_parse.text
                # print(title)
            except:
                title=""
            try:
                category_div=media_body.find('div')
                category=str(category_div.text).split('Category:')[1]
                # print(category)
            except:
                category=""
            try:
                brand_div=category_div.find_next('div')
                brand=str(brand_div.text).split('Brand:')[1]
                # print(brand)
            except:
                brand=""
            try:
                seller_div = brand_div.find_next('div')
                seller = str(seller_div.text).split('Seller:')[1]
                # print(seller)
            except:
                seller=""
            try:
                fulfillment_div = seller_div.find_next('div')
                fulfillment = str(fulfillment_div.text).split('Fulfillment:')[1]
                # print(fulfillment)
            except:
                fulfillment=""
            try:
                tier_div = fulfillment_div.find_next('div')
                size_tier = str(tier_div.text).split('Tier:')[1]
                # print(size_tier)
            except:
                size_tier=""

            try:
                number_of_images_div = tier_div.find_next('div')
                number_of_images = str(number_of_images_div.text).split('Images:')[1]
                # print(number_of_images)
            except:
                number_of_images=""

            try:
                variation_count_div = number_of_images_div.find_next('div')
                variation_count = str(variation_count_div.text).split('Count:')[1]
                # print(variation_count)
            except:
                variation_count

            try:
                weight_div = variation_count_div.find_next('div')
                weight = str(weight_div.text).split('Weight:')[1]
                # print(weight)
            except:
                weight=""
            try:
                package_dimensions_div = weight_div.find_next('div')
                package_dimensions = str(package_dimensions_div.text).split('Dimensions:')[1]
                # print(package_dimensions)
            except:
                package_dimensions=""

            try:
                storage_fee_div = package_dimensions_div.find_next('div')
                storage_fee = str(storage_fee_div.text).split(':')[1]
                # print(storage_fee)
            except:
                storage_fee=""

            try:
                age_div = storage_fee_div.find_next('div')
                age = str(age_div.text).split(':')[1]
                # print(age)
            except:
                age = ""
                # print("===========================")
        except:pass

        try:
            td_object_one = td[1]
            sellers=td_object_one.text
            # print(sellers)
        except:
            sellers=""
        try:
            td_object_two = td[2]
            price=td_object_two.text
            # print(price)
        except:
            price=""
        try:
            td_object_three = td[3]
            monthly_sales=td_object_three.text
            # print(monthly_sales)
        except:
            monthly_sales=""
        try:
            td_object_four = td[4]
            monthly_revenue=td_object_four.text
            # print(monthly_revenue)
        except:
            monthly_revenue=""
        try:
            td_object_five = td[5]
            bsr=td_object_five.text
            # print(bsr)
        except:
            bsr=""
        try:
            td_object_six = td[6]
            reviews =td_object_six.text
            # print(reviews)
        except:
            reviews=""
        data={
            "amazon_link":amazon_link,
            "image":image,
            "title":title,
            "category":category,
            "brand":brand,
            "seller":seller,
            "fulfillment":fulfillment,
            "size_tier":size_tier,
            "number_of_images":number_of_images,
            "variation_count":variation_count,
            "weight":weight,
            "package_dimensions":package_dimensions,
            "storage_fee":storage_fee,
            "age":age,
            "sellers":sellers,
            "price":price,
            "monthly_sales":monthly_sales,
            "monthly_revenue":monthly_revenue,
            "bsr":bsr,
            "reviews":reviews
        }
        all_data.append(data)
        dumps=json.dumps(all_data)
        print(type(dumps))

    #         print(data)
    #         # print("============================")
    #



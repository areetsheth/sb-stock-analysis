from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

cookie_string = "__cf_bm=y8E543CbHRRDPVyt82Xhcoa571xIaeuvxotYUUZZWvw-1707303702-1-AQvjTTuJXIVMQ+pUAef27veZ2gd4DiOKmKVB9ROECpi2K+yl+bzbKjGROHMBK1NC+yXE7vsxdJDGA0q1YAZGCp0=; _gid=GA1.2.539999847.1707303701; AMCVS_138FFF2554E6E7220A4C98C6%40AdobeOrg=1; at_check=true; sailthru_hid=; _gcl_au=1.1.1061840719.1707303702; TAsessionID=9a979de3-97b6-475c-8a93-38f72015d9b8|NEW; _cb=D--efQB6xMghF3wwM; kw.session_ts=1707303701719; _sp_ses.f5e1=*; _hjSession_1906529=eyJpZCI6IjM5YzhmMjgyLWM1YjMtNGE1YS1iOGRmLTEyZTZmMjI2ZDdkMiIsImMiOjE3MDczMDM3MDE4MDUsInMiOjAsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjoxfQ==; ccu_remote=130.126.255.233; porte_ipa=%7B%22130.126.255.233%22%3A%7B%22%22%3Atrue%7D%7D; _clck=1enfm1p%7C2%7Cfj2%7C0%7C1498; s_cc=true; __qca=P0-604607518-1707303701758; YWRhZ2UuY29t-_lr_uf_-wlb5gx=f91e6db3-6362-4cf0-b004-8ae8af84c045; cciFirstTouch=%7B%7D; _tt_enable_cookie=1; _ttp=jUz5P01icvc4eklVRS-YZ-O9MNn; s_ecid=MCMID%7C62730956340215450861334502786264948981; _hjSessionUser_1906529=eyJpZCI6IjE4ODdhMTk5LTkyMmYtNWE3MS04MDcyLTBlM2YwY2ZkNzg3NSIsImNyZWF0ZWQiOjE3MDczMDM3MDE4MDQsImV4aXN0aW5nIjp0cnVlfQ==; AMCV_138FFF2554E6E7220A4C98C6%40AdobeOrg=-2121179033%7CMCIDTS%7C19761%7CMCMID%7C62730956340215450861334502786264948981%7CMCAAMLH-1707908886%7C7%7CMCAAMB-1707908886%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1707311286s%7CNONE%7CvVersion%7C5.3.0%7CMCAID%7CNONE; _cb_svref=external; s_sq=%5B%5BB%5D%5D; cceAdvantageReturn=https://adage.com/series/2023-super-bowl-lvii/2522836; _ga_94BVKS4T4Y=GS1.1.1707303701.1.1.1707304116.0.0.0; _ga_FL9C88FXSE=GS1.1.1707303701.1.1.1707304116.23.0.0; _ga=GA1.2.1132107929.1707303701; _rdt_uuid=1707303701672.02fa3dc4-aad3-4718-b250-4708cc1338bf; s_depth=7; s_ppn=playlists%3A2023%3A%20super%20bowl%20lvii%3A2522836_2023_super_bowl_lvii; _chartbeat2=.1707303701688.1707304116762.1.CjS6wzCZW8RJ79-26DSyFrJDVSTas.4; mbox=session#18931318eb0d4e13a0b23259eb401437#1707305977|PC#18931318eb0d4e13a0b23259eb401437.34_0#1770548917; s_nr=1707304116844-New; chkcookie=1707304116846; _uetsid=462b10e0c5a811ee9e028d56b2c993e8; _uetvid=462b3800c5a811eeafd30d825b93c865; sailthru_pageviews=7; sailthru_content=7ed65d2d378dfefe0fd7b7ffc1b7cb1a30ea076835e42287f8a7838bb2ac8930012f397dfdbda0bed6fd987d8e8d64bd; sailthru_visitor=b2a7fe21-fcea-4382-93c9-a1f1e41c1540; _clsk=atleir%7C1707304117812%7C7%7C1%7Cw.clarity.ms%2Fcollect; s_ppvl=playlists%253A2022%253A%2520super%2520bowl%2520lvi%253A2435071_2022_super_bowl_lvi%2C26%2C26%2C1277%2C1278%2C1277%2C1920%2C1080%2C1%2CP; s_ppv=playlists%253A2023%253A%2520super%2520bowl%2520lvii%253A2522836_2023_super_bowl_lvii%2C36%2C26%2C1519%2C1920%2C919%2C1920%2C1080%2C1%2CP; kw.pv_session=15; _sp_id.f5e1=8dcbbe98-240c-43f6-8845-6272e9d56325.1707303702.1.1707304207.1707303702.0751e308-0185-4b7f-9459-0646ba32eced; YWRhZ2UuY29t-_lr_hb_-wlb5gx%2Fdrupal-sites={%22heartbeat%22:1707304219305}; YWRhZ2UuY29t-_lr_tabs_-wlb5gx%2Fdrupal-sites={%22sessionID%22:0%2C%22recordingID%22:%225-72e53654-d2d2-43d4-b5f9-99114c719374%22%2C%22recordingConditionThreshold%22:%2240.52746721950644%22%2C%22webViewID%22:null%2C%22lastActivity%22:1707304224538}"
cookie_list = cookie_string.split("; ")
cookies_dict = {}
for item in cookie_list:
    key, value = item.split("=", 1)
    cookies_dict[key] = value

cookie_opts = {
    "name": "myCookieName",  
    "value": "myCookieValue",  
    "path": "/",  
    "domain": "adage.com",  
    "secure": True,  
    "httpOnly": False,  
}
cookie_opts.update(cookies_dict)

urls = {2023: "https://adage.com/series/2023-super-bowl-lvii/2522836", 2022: "https://adage.com/series/2022-super-bowl-lvi/2435071", 2021: "https://adage.com/series/2021-super-bowl-lv/2377161", 2020: "https://adage.com/series/2020-super-bowl-liv/2234026", 2019: "https://adage.com/series/2019-super-bowl-liii/2206876"}
options = webdriver.ChromeOptions()
# options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--ignore-certificate-errors")
options.add_experimental_option("excludeSwitches", ["enable-logging"])
prefs = {
    "profile.default_content_settings.popups": 0,
    # "download.default_directory": raw_path,
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
}
options.add_experimental_option("prefs", prefs)

try:
    with webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()), options=options
    ) as driver:
        for url in urls:
            url_string = urls[url]
            driver.get(url_string)
            driver.add_cookie(cookie_opts)
            html_content = driver.page_source
            file_path = "sbads/" + str(url) + ".html"
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(html_content)
except Exception as e:
    print(e)

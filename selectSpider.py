# -*- coding: utf-8 -*-
"""
Created on Tue Dec 01 13:23:02 2015

@author: XuGang
"""

#import sys
#reload(sys)
#sys.setdefaultencoding('utf-8')

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
import os
import json
from selenium.webdriver.support.ui  import Select

global browser
global province_name
global city_name
global county_name

url = "http://kuailexue.com/teaching_center"
chromedriver = "C:\Program Files\Google\Chrome\Application\chromedriver.exe"
os.environ["webdriver.chrome.driver"] = chromedriver
browser = webdriver.Chrome(chromedriver)
browser.get(url)

print u"please log in..."
useless = raw_input('')

county_array = []
city_array = []

province_name = ""
city_name = ""
county_name = ""
old = None


browser.switch_to.window(browser.window_handles[-1])
provinces = browser.find_elements_by_xpath("//td[@class='con']/select[@id='province']/option")
select1 = Select(browser.find_element_by_id("province"))

f = open("school.txt","w")   

done = [u'安徽',u'北京',u'福建',u'甘肃',u'贵州',u'广东',u'广西',u'海南',u'河北',u'河南',u'黑龙江',u'湖北',u'湖南',u'吉林',u'江苏',u'江西',u'辽宁',u'内蒙古',u'宁夏',u'青海',u'山东',u'山西']
#undone = [u'北京',u'福建',u'甘肃',u'贵州',u'广东',u'广西']
for i in provinces:
#    i.click()

    time.sleep(0.1)
    province_name =  i.text
    if(province_name in done):
        continue
    print province_name
    select1.select_by_visible_text(province_name)
    cities = browser.find_elements_by_xpath("//td[@class='con']/select[@id='city']/option")
    
    city_array = []
    for j in cities:
        city_array.append(j.text)

    for j in city_array:
#        j.click()
        time.sleep(0.1)
        print j
        city_name = j
        
        select2 = Select(browser.find_element_by_id("city")) 
        select2.select_by_visible_text(j)

        ActionChains(browser).double_click(browser.find_element_by_id("first_login_msg")).perform()
        
        try:
            time.sleep(1)
            counties = browser.find_elements_by_xpath("//td[@class='con']/select[@id='county']/option")
        except:
            ActionChains(browser).double_click(browser.find_element_by_id("first_login_msg")).perform()
            time.sleep(2)
            counties = browser.find_elements_by_xpath("//td[@class='con']/select[@id='county']/option")

        county_array = []
        
        try:
            for k in counties:
    #            print k.text
                county_array.append(k.text)
        except:
            ActionChains(browser).double_click(browser.find_element_by_id("first_login_msg")).perform()
            time.sleep(2)
            counties = browser.find_elements_by_xpath("//td[@class='con']/select[@id='county']/option")
            for k in counties:
    #            print k.text
                county_array.append(k.text)            
        for k in county_array:
            time.sleep(0.1)
            print k
            county_name = k
            try:
                select3 = Select(browser.find_element_by_id("county"))
                select3.select_by_visible_text(k)
            except:
                ActionChains(browser).double_click(browser.find_element_by_id("first_login_msg")).perform()

                time.sleep(2)
                select3 = Select(browser.find_element_by_id("county"))
                time.sleep(2)
                select3.select_by_visible_text(k)                
            
#            time.sleep(0.1)
#            ActionChains(browser).double_click(k).perform()
            if(k != u"全部"):
                try:
                    time.sleep(0.5)
                    schools_text = browser.find_element_by_id("user_school")
                    ActionChains(browser).double_click(schools_text).perform()
                    
                    schools = browser.find_element_by_id("school_sug")
                except:
                    time.sleep(1)
                    schools_text = browser.find_element_by_id("user_school")
                    ActionChains(browser).double_click(schools_text).perform()
                    time.sleep(1)
                    schools = browser.find_element_by_id("school_sug")                    
    #                print schools.text
                
                while (old == schools.text):
                    print "--------------------------------------------------"
                    ActionChains(browser).double_click(browser.find_element_by_id("first_login_msg")).perform()

                    try:
                        time.sleep(2)
                        select3 = Select(browser.find_element_by_id("county"))
                        time.sleep(2)
                        select3.select_by_visible_text(k) 
                    except:
                        time.sleep(2)
                        select3 = Select(browser.find_element_by_id("county"))
                        time.sleep(2)
                        select3.select_by_visible_text(k)                
                    
        #            time.sleep(0.1)
        #            ActionChains(browser).double_click(k).perform()
                    if(k != u"全部"):
                        try:
                            time.sleep(2)
                            schools_text = browser.find_element_by_id("user_school")
                            ActionChains(browser).double_click(schools_text).perform()
                            
                            schools = browser.find_element_by_id("school_sug")
                        except:
                            time.sleep(2)
                            schools_text = browser.find_element_by_id("user_school")
                            ActionChains(browser).double_click(schools_text).perform()
                            time.sleep(2)
                            schools = browser.find_element_by_id("school_sug")                       
                
                old = schools.text
                    
                
                for school in schools.text.split():
                    
                    try:
                        string = province_name + ',' + city_name + ',' + county_name + ',' + school  + ','
                        f.writelines(string)
                        f.writelines("\n")
                        print string 
                    except:
                        continue
f.close()            
            
#       whuxugang@aliyun.com
            
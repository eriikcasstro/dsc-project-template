from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import sys
import os
import requests
import shutil
from xlsxwriter import Workbook
import wget
import time
import linecache



def click_img(driver): 
    '''click image to get the data necessary'''
    click_img = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"//div[@class='_9AhH0']")))
    click_img.click()
    
#click next
def click_next(driver):
    ''' clicks the next image '''
    click_nxt = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.LINK_TEXT,"Next")))
    click_nxt.click()


def not_now(driver): 
    ''' clicks the not now button '''
    not_now = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Not Now")]'))).click()

    
##get Description 
def get_description2(driver):
    '''gets description and cuts off hashtags and user tags'''
    ch1 = '@'
    ch2 = '#'
    description = driver.find_element(By.XPATH ,"//html/body/div[5]/div[2]/div/article/div[3]/div[1]/ul/div/li/div/div/div[2]/span[1]")
    description = description.text
    if int(description.rfind(ch1)) < int(description.rfind(ch2)):
        description = description.split(ch1)[0]
    elif int(description.rfind(ch2)) < int(description.rfind(ch1)):
        description = description.split(ch2)[0]
    if description.rfind('\n') != -1: 
        description = description.replace('\n','')
    return description


def get_description(driver): 
    ''' gets description and delets blank spaces
        returns description as a String
    '''
    try:
        description = driver.find_element(By.XPATH ,"//html/body/div[5]/div[2]/div/article/div[3]/div[1]/ul/div/li/div/div/div[2]/span[1]")
        description = description.text
        if description.rfind('\n') != -1: 
            description = description.replace('\n','')
        return description
    except Exception as e :
        description = 'error' 
        return description


#Get Tags
def get_mentions(driver): 
    ''' gets mentions 
        returns mentions as a list of strings
    '''
    tags = driver.find_element(By.XPATH ,"//html/body/div[5]/div[2]/div/article/div[3]/div[1]/ul/div/li/div/div/div[2]/span")
    tags = tags.find_elements_by_class_name('notranslate')
    tags = [tag.text for tag in tags]
    return tags




##Get Date
def get_date_time(driver): 
    '''
    Gets date and time 
    returns date and time as separate variables, both String
    '''
    date_time = driver.find_element(By.XPATH ,"//html/body/div[5]/div[2]/div/article/div[3]/div[2]/a/time")
    date_time2 = date_time.get_attribute('datetime')
    date = date_time2.split('T')[0]
    time = date_time2.split('T')[1]
    return date, time



##Hashtags 
def get_hashtags(driver):
    '''
    gets hashtags 
    returns hashtags as a list of strings
    '''
    hashtags = driver.find_elements_by_class_name("xil3i")
    hashtags = [h.text for h in hashtags ]
    return hashtags



def transform_to_int(my_string): 
    '''
    transforms the variable into an Int, deleting commas, full stops, m and k, last two are replaced with the adequate numbers
    returns the string transformed to an integer
    
    '''
    m = '000000'
    k = '000'
    ##Delete likes 
    if my_string.find('likes') != -1:
        my_string = my_string.replace('likes','')
    ## Delete views 
    if my_string.find('views') != -1:
        my_string = my_string.replace('views', '')
    ## Delete commas
    if my_string.find(',') != -1: 
        my_string = my_string.replace(',','')
    ## Delete full stop 
    if my_string.find('.') != -1: 
        my_string = my_string.replace('.', '')
        
    ## delete m for million and add 000000, if its k add 000
    if my_string.find('m') != -1: 
        my_string = my_string.replace('m',m)
    elif my_string.find('k') != -1: 
        my_string = my_string.replace('k',k)
        
    my_string = int(my_string)
    return my_string




def get_img_likes(driver):
    '''
    retrieves likes from the post. when is a normal video we cant see the likes therefore a try is catching this exception
    and passing a 0 to the variable  
    returns img_likes
    '''
    try:
        img_likes = driver.find_element_by_class_name("Nm9Fw")
        img_likes = img_likes.text
        img_likes = transform_to_int(img_likes)
    except Exception:
        img_likes = 0
    return img_likes


def username_data(driver):
    '''
    returns username metadata as a list, [0] number of posts, [1] number of followers and [2] following
    '''
    info = driver.find_elements_by_class_name('g47SY')
    account_info = []
    for i in info: 
        i = transform_to_int(i.text)
        ## adding the integer to a new list
        account_info.append(i)
    return account_info



def get_img_src(driver):
    '''
    retrieves img_src from the post, when it's a video there is no img resource, therefore a try is used to managed this Exception
    passing 'this is a video' to the string
    returns image_info as String
    '''
    try: 
        img_class = driver.find_element_by_class_name('_97aPb')
        image_info = img_class.find_element_by_tag_name('img')
        image_info =  image_info.get_attribute('src')
        return image_info
    except Exception:
        image_info = 'this is a video'
        return image_info
    


def find_username(driver): 
    '''
    finds the username 
    returns username as string
    '''
    user_name = driver.find_element(By.XPATH ,"//section/main/div/header/section/div[1]/h2")
    return user_name.text



def check_video(driver):
    '''
    checks if the post is a video,
    returns True or False
    '''
    try: 
        video = driver.find_element(By.XPATH ,"//html/body/div[5]/div[2]/div/article/div[2]/div/div/div/div/div")
        video2 = video.get_attribute('class')
        if video2 == '_5wCQW': 
            return True 
    except Exception:
        return False 


def get_views(driver): 
    '''
    This method is used when a post is a video. If the views arent accessible then the variable is set to 0 
    returns the number of views on a video
    '''
    try:
        num_of_views = driver.find_element_by_class_name('vcOH2')
        num_of_views = num_of_views.text
        num_of_views_int = transform_to_int(num_of_views)
        return num_of_views_int
    except Exception:
        num_of_views_int = 0
        return num_of_views_int



def search(name,driver): 
    '''
    name: instagram name
    
    This searches for the username in the searchbox 
    
    '''
    searchbox = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"//input[@placeholder='Search']")))
    searchbox.clear()
    #search for hasthag dogs
    searchbox.send_keys(name)
    #wait for 5 seconds
    time.sleep(2)
    searchbox.send_keys(Keys.ENTER)
    time.sleep(2)
    searchbox.send_keys(Keys.ENTER)
    



def get_all_metadata(driver): 
    '''
    uses all the methods written to get the necessary data
    returns all the data gathered
    '''
    desc = get_description(driver)
    if desc == 'error': 
        while desc == 'error': 
            desc = get_description(driver)
    
    num_of_likes = get_img_likes(driver)
    mentions = get_mentions(driver)
    num_htags = get_hashtags(driver)
    ##check if is a video or image 
    if check_video(driver): 
        media_type = 'video'
        video_views = get_views(driver)    
    else: 
        media_type = 'image'
        video_views = 0 
    date, time = get_date_time(driver)
    src_img = get_img_src(driver)
    return desc, num_of_likes, mentions,num_htags, media_type, video_views,date,time, src_img


























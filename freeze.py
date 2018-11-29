import sys
import os
from selenium import webdriver

website = sys.argv[1]
generic_name = sys.argv[2]

website_formatted = website.split("//")[1]

dir_name = "screenshots"

fellow_directories = os.listdir(".")

print "fellow directories: " + str(fellow_directories)
 
#set up screenshot directory
if dir_name not in fellow_directories:
	print "we should be making " + str(dir_name) + " dir now"
	os.system("mkdir " + dir_name)

screenshot_subdirectories = os.listdir(str(dir_name) + "/")

print "screenshot subdirectories: " + str(screenshot_subdirectories)

if str(website_formatted) not in screenshot_subdirectories:
	print "we should be making " + str(website_formatted) + " dir now"
	os.system("mkdir " + dir_name + "/" + str(website_formatted))

#go to website
driver = webdriver.Chrome("/usr/local/bin/chromedriver")
driver.get(website)
screenshot = driver.save_screenshot(str(dir_name) + "/" + str(website_formatted) + "/" + generic_name + ".png")
print "We've taken the screenshot at: " + str(website)
driver.close()

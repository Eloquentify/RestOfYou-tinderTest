from selenium import webdriver
import os
import requests
import time
import subprocess
import sys

def download_file(url, local_filename=None):
	if local_filename is None:
		local_filename = url.split('/')[-1]

	if os.path.exists(local_filename):
		return	local_filename

	if not url.startswith('http'):
		url = 'http:'+url

	r = requests.get(url,stream=True)
	with open(local_filename,'wb') as f:
		for chunk in r.iter_content(chunk_size=1024):
			if chunk:
				f.write(chunk)
	return local_filename

driver = webdriver.Firefox()
#StaleElementError -> firefox
def insta_gif(tags):
	driver.get('https://www.instagram.com/explore/tags/'+tags+'/')
	#driver.get(tags)

	for x in range(0,10):
		driver.execute_script('window.scrollTo(0,document.body.scrollHeight);')
		time.sleep(2)

	images = driver.find_elements_by_css_selector('img')

	for i,image in enumerate(images):
		url = image.get_attribute('src')

		savedname = 'mypics/' + str(i)+'.jpg'
		composedname = 'instacompose/' + str(i)+'.jpg'

		try:
			filename = download_file(url,savedname)
			subprocess.call(['convert',savedname,'-resize','293x293',savedname])

		except Exception as e:
			print e
			continue
def randompics():
	driver.get('https://unsplash.com/search/photos/random')
	#driver.get(tags)

	for x in range(0,10):
		driver.execute_script('window.scrollTo(0,document.body.scrollHeight);')
		time.sleep(2)

	images = driver.find_elements_by_css_selector('img')

	for i,image in enumerate(images):
		url = image.get_attribute('src')

		savedname = 'mypics/' + str(i)+'.jpg'
		#composedname = 'instacompose/' + str(i)+'.jpg'

		try:
			filename = download_file(url,savedname)
			subprocess.call(['convert',savedname,'-resize','293x293',savedname])

		except Exception as e:
			print e
			continue
	# 	if i > 0:	
	# 		presavedname = 'mypics/' + str(i-1)+'.jpg'
	# 		subprocess.call(['composite','-blend','40x60%',presavedname,savedname,presavedname])


	
	# subprocess.call(['convert','mypics/*.jpg','mypics/'+tags+'.gif'])


	# subprocess.call(['rm','-r','mypics/*.jpg'])
	driver.quit()

def composite_images():
	

randompics()
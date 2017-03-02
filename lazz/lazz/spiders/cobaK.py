# import scrapy
# import traceback
# import sys
# # import pdb
# import MySQLdb
# from selenium import webdriver
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.common.exceptions import TimeoutException
# from selenium.webdriver.common.keys import Keys
# # from pyvirtualdisplay import Display
# from scrapy.http import TextResponse
# from lazz.items import Lproduct
# from impala.dbapi import connect
# from kafka import KafkaConsumer, KafkaProducer

# class ProductSpider(scrapy.Spider):
# 	# pdb.set_trace()
# 	name = "lajada"
# 	allowed_domains = ["http://www.lazada.co.id/store-directory/"]
# 	start_urls = ["http://www.lazada.co.id/store-directory/"]
# 	def __init__(self): 
# 		path_to_chromedriver = 'D://chromedriver'
# 		# path_to_chromedriver='/usr/local/bin/chromedriver'
# 		self.driver = webdriver.Chrome(executable_path=path_to_chromedriver)
# 		self.driver = webdriver.PhantomJS()

# 	def parse(self, response):
# 		home = 'http://www.lazada.co.id/store-directory/'
# 		time.sleep(5)
# 		cat = 0
# 		for kat in range(0,18):
# 			cat=cat+1
# 			self.driver.get(home)
# 			time.sleep(20)
# 			for turun in range(0,50):
# 				try:
# 					self.driver.find_element_by_xpath('/html/body/div[3]/div/div['+str(cat)+']/h2/a').click()
# 					time.sleep(10)
# 					url = self.driver.current_url
# 					break
# 				except:
# 					self.driver.find_element_by_xpath('/html/body').send_keys(Keys.ARROW_DOWN + Keys.ARROW_DOWN)
# 					time.sleep(3)
# 					pass
# 				for hal in range(0,100):
# 					barang = 0
# 					response = TextResponse(url=response.url, body=self.driver.page_source, encoding='utf-8')
# 					for ba in range(0,36):#36
# 						barang = barang + 1
# 						for tutup in range(0,50)
# 							try:
# 								self.driver.find_element_by_xpath('//*[@id="faster-delivery-location-popover"]/span').click()
# 								time.sleep(2)
# 							except:
# 								self.driver.find_element_by_xpath('/html/body').send_keys(Keys.ARROW_DOWN + Keys.ARROW_DOWN)
# 								time.sleep(3)
# 						ling = response.xpath('/html/body/div[3]/div[2]/div[2]/div[1]/div[2]/div['+str(barang)+']/a/@href').extract_first()



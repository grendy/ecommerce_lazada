import scrapy
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from pyvirtualdisplay import Display
from scrapy.http import TextResponse
from impala.dbapi import connect
import traceback
import sys
# import pdb
# import MySQLdb

import time

class ProductSpider(scrapy.Spider):
	# pdb.set_trace()
	name = "lajada"
	allowed_domains = ["http://www.lazada.co.id/store-directory/"]
	start_urls = ["http://www.lazada.co.id/store-directory/"]
	def __init__(self):

        display = Display(visible=0, size=(1366, 768))
        display.start()
		self.driver = webdriver.Firefox()
		# path_to_chromedriver = 'D://chromedriver'
		# path_to_chromedriver='/usr/local/bin/chromedriver'
		# self.driver = webdriver.Chrome(executable_path=path_to_chromedriver)
		# self.driver = webdriver.PhantomJS()

	def parse(self, response):
		# home = "https://www.tokopedia.com/"
		home = 'http://www.lazada.co.id/store-directory/'
	# 	# pdb.set_trace()
	# 	# conn = connect(host="192.168.180.144", port=21050, database='data_id')
	# 	# cur = conn.cursor()
		
		
		# self.driver.find_element_by_xpath('/html/body/div[3]/div/div[1]/h2/a').click()
		# time.sleep(5)
		cat = 0
		for kat in range(0,18):
			cat=cat+1
			self.driver.get(home)
			time.sleep(5)
			for turun in range(0,18):
				try:
					# /html/body/div[3]/div/div[1]/h2/a
					# /html/body/div[3]/div/div[2]/h2/a

					# //*[@id="js_18"]/span/a
					# //*[@id="js_17"]/span/a
					# //*[@id="js_1b"]/span/a


					time.sleep(5)
					url = self.driver.current_url
					break
				except:
					self.driver.find_element_by_xpath('/html/body').send_keys(Keys.ARROW_DOWN + Keys.ARROW_DOWN)
					time.sleep(3)
					pass
			for hal in range(0,100):#100
				barang = 0
				for ba in range(0,36):#36
					for cobaklik in range(0,100):
						try:
							self.driver.find_element_by_xpath('//*[@id="faster-delivery-location-popover"]/span').click()
							time.sleep(5)
							break
						except:
							self.driver.find_element_by_xpath('/html/body').send_keys(Keys.ARROW_DOWN + Keys.ARROW_DOWN)
							time.sleep(3)
							pass
					# self.driver.find_element_by_xpath('/html/body').send_keys(Keys.PAGE_DOWN)
					# time.sleep(5)
					barang = barang+1
					print "======================================"
					print "======================================"
					print barang
					print "======================================"
					print "======================================"
					print "======================================"
					for l in range(0,100):
						time.sleep(1)
						try:
							self.driver.find_element_by_xpath('/html/body/div[3]/div[2]/div[2]/div[1]/div[2]/div['+str(barang)+']/a').click()
							
							break
						except:
							try:
								self.driver.find_element_by_xpath('/html/body/div[3]/div[2]/div[2]/div[2]/div[2]/div['+str(barang)+']/a').click()
								break
							except:
								try:
									self.driver.find_element_by_xpath('/html/body/div[3]/div[1]/div[2]/div[2]/div[1]/div[2]/div['+str(barang)+']/a').click()
									break
								except:
									try:
										self.driver.find_element_by_xpath('/html/body/div[3]/div[1]/div[2]/div[1]/div[2]/div['+str(barang)+']/a').click()
										# /html/body/div[3]/div/div[2]/div[2]/div[1]/div[2]/div[1]/a
										break
									except:
										self.driver.find_element_by_xpath('/html/body').send_keys(Keys.ARROW_DOWN)
										time.sleep(5)
										pass
					time.sleep(15)
					# response = TextResponse(url=response.url, body=self.driver.page_source, encoding='utf-8')
					# url = response.xpath('/html/body/div[3]/div[2]/div[2]/div[1]/div[3]/div[1]/a/@href').extract_first()
					# time.sleep(5)
					# self.driver.get(str(url))
					# time.sleep(30)
					# url = self.driver.current_url
					response = TextResponse(url=response.url, body=self.driver.page_source, encoding='utf-8')
					try:
						product_url = self.driver.current_url		
						penjual_url = response.xpath('//*[@id="prod_content_wrapper"]/div[2]/div[2]/div/div/div[1]/a/@href').extract_first()
						if penjual_url == None:
							penjual_url = "Lazada"
						else:
							pass	
						kategori = response.xpath('/html/body/header/footer/div[2]/div[1]/ul/li[2]/span/a/span/text()').extract_first()
						kategori_url = response.xpath('/html/body/header/footer/div[2]/div[1]/ul/li[2]/span/a/@href').extract_first()
						nama_product = response.xpath('//*[@id="prod_title"]/text()').extract_first()
						harga = response.xpath('//*[@id="special_price_box"]/text()').extract_first()
						diskon = response.xpath('//*[@id="product_saving_percentage"]/text()').extract_first()
						harga_sebelumnya = response.xpath('//*[@id="price_box"]/text()').extract_first()
						c = 0
						d=0
						spek = [0]*10
						for spk in range(0,100):
							d=d+1
							try:
								spesi = response.xpath('//*[@id="prod_content_wrapper"]/div[1]/div[1]/div/ul/li['+str(d)+']/span/text()').extract_first()
								if spesi == None:
									spesi = response.xpath('//*[@id="prod_content_wrapper"]/div[1]/div[2]/div/ul/li['+str(d)+']/span/text()').extract_first()
									spek[c] = spesi
								else:
									spek[c] = spesi
							except:
								break
							c=c+1
						spesifik = ""
						for d in range(len(spek)):
							if spek[d] == None:
								break
							elif d==0:
								try:
									spesifik =  str(spesifik) + str(spek[d])
								except UnicodeEncodeError:
									spesifik = str(spesifik) + spek[d].encode('utf-8')	
							else:
								try:
									spesifik =  str(spesifik) + ", " + str(spek[d])
								except UnicodeEncodeError:
									spesifik =  str(spesifik) + ", " + spek[d].encode('utf-8')
						spesifikasi = spesifik
						try:
							self.driver.find_element_by_xpath('/html/body').send_keys(Keys.PAGE_DOWN)
							time.sleep(1)
							try:
								self.driver.find_element_by_xpath('//*[@id="faster-delivery-popover"]/span').click()
								time.sleep(1)
							except:
								pass
							self.driver.find_element_by_xpath('//*[@id="prod_content_wrapper"]/div[2]/div[2]/div/div/div[1]/div/div/div').click()
							time.sleep(5)
							rate = response.xpath('/html/body/div[7]/div[2]/h3/text()').extract_first()
							if rate == None:
								rate = response.xpath('/html/body/div[6]/div[2]/h3/text()').extract_first()
							else:
								pass
						except:
							rate = response.xpath('/html/body/div[6]/div[2]/h3/text()').extract_first()
								# //*[@id="prod_content_wrapper"]/div[2]/div[2]/div/div/div/div/div/div[1]/div[2]
						d=0
						for tabel in range(0,50):
							d=d+1
							berat = response.xpath('//*[@id="prd-detail-page"]/div/div[3]/div[2]/div[2]/table/tbody/tr['+str(d)+']/td[1]/text()').extract_first()
							if berat == "Berat (kg)":
								berat = response.xpath('//*[@id="prd-detail-page"]/div/div[3]/div[2]/div[2]/table/tbody/tr['+str(d)+']/td[2]/text()').extract_first()
								break
							else:
								berat = response.xpath('//*[@id="prd-detail-page"]/div/div[3]/div[1]/div[2]/table/tbody/tr['+str(d)+']/td[1]/text()').extract_first()
								if berat == "Berat (kg)":
									berat = response.xpath('//*[@id="prd-detail-page"]/div/div[3]/div[1]/div[2]/table/tbody/tr['+str(d)+']/td[2]/text()').extract_first()
									break
								else:
									pass
						d=0
						for tabel in range(0,50):
							d=d+1
							ukuran = response.xpath('//*[@id="prd-detail-page"]/div/div[3]/div[2]/div[2]/table/tbody/tr['+str(d)+']/td[1]/text()').extract_first()
							if ukuran == "Ukuran (L x W x H cm)":
								ukuran = response.xpath('//*[@id="prd-detail-page"]/div/div[3]/div[2]/div[2]/table/tbody/tr['+str(d)+']/td[2]/text()').extract_first()
								break
							else:
								ukuran = response.xpath('//*[@id="prd-detail-page"]/div/div[3]/div[1]/div[2]/table/tbody/tr['+str(d)+']/td[1]/text()').extract_first()
								if ukuran == "Ukuran (L x W x H cm)":
									ukuran = response.xpath('//*[@id="prd-detail-page"]/div/div[3]/div[1]/div[2]/table/tbody/tr['+str(d)+']/td[2]/text()').extract_first()
									break
								else:
									pass
						d=0
						for tabel in range(0,50):
							d=d+1
							garansi = response.xpath('//*[@id="prd-detail-page"]/div/div[3]/div[2]/div[2]/table/tbody/tr['+str(d)+']/td[1]/text()').extract_first()
							if garansi == "Tipe garansi":
								garansi = response.xpath('//*[@id="prd-detail-page"]/div/div[3]/div[2]/div[2]/table/tbody/tr['+str(d)+']/td[2]/text()').extract_first()
								break
							else:
								garansi = response.xpath('//*[@id="prd-detail-page"]/div/div[3]/div[1]/div[2]/table/tbody/tr['+str(d)+']/td[1]/text()').extract_first()
								if garansi == "Tipe garansi":
									garansi = response.xpath('//*[@id="prd-detail-page"]/div/div[3]/div[1]/div[2]/table/tbody/tr['+str(d)+']/td[2]/text()').extract_first()
									break
								else:
									pass
						metode_pembayaran = response.xpath('//*[@id="deliveryType"]/div[2]/div/div[2]/span/text()').extract_first()

						# deskripsi = response.xpath('//*[contains(@id,"shop")]/p/text()').extract_first()					
						penjual = response.xpath('//*[@id="prod_content_wrapper"]/div[2]/div[2]/div/div/div[1]/a/span/text()').extract_first()
						if penjual == None:
							penjual = "Lazada"
						else:
							pass
						feed_nama = response.xpath('//*[@id="js_reviews_list"]/li[1]/div[3]/span[2]/text()').extract_first()
						if feed_nama==None:
							feed_nama=feed_nama = response.xpath('//*[@id="js_reviews_list"]/li[1]/div[3]/span/text()').extract_first()
						else:
							pass
						try:
							pesan = response.xpath('//*[@id="js_reviews_list"]/li[1]/div[2]/text()').extract_first()
							tanggal = response.xpath('//*[@id="js_reviews_list"]/li[1]/div[1]/span[3]/text()').extract_first()
						except:
							pass
						harga = harga.replace(".","")
						harga_sebelumnya = harga_sebelumnya.replace(".","").replace(",","").replace("RP","").replace(" ","")
						nama_product = nama_product.replace("\n","").strip()
						# nama_product = nama_product.strip()
						try:
							diskon = diskon.replace("%","").replace(" ","")
						except:
							diskon = 0
						potongan_harga = (float(diskon) / 100)*int(harga_sebelumnya)
						metode_pembayaran = metode_pembayaran.replace("\n","").strip()
						if feed_nama == None:
							pass
						else:
							feed_nama = feed_nama.replace("\n","").strip()
						if pesan == None:
							pass
						else:
							pesan = pesan.replace("\n","").strip()
						penjual = penjual.replace("\n","").strip()
						print "======================================"
						print product_url
						print nama_product
						print spesifikasi
						print "======================================"
						print berat
						print ukuran
						print garansi
						# print spek[0]
						print "======================================"
						print harga_sebelumnya
						print harga
						print potongan_harga
						print diskon
						print metode_pembayaran
						print "======================================"
						print penjual_url
						print penjual
						print rate
						print "======================================"
						print kategori
						print kategori_url
						print "======================================"
						print feed_nama
						print tanggal
						print pesan
						print "======================================"

					except:
						pass
					self.driver.get(url)
					time.sleep(10)
				for bawah in range(0,100):
					self.driver.find_element_by_xpath('/html/body').send_keys(Keys.ARROW_DOWN)
					time.sleep(2)
					try:
						self.driver.find_element_by_xpath('/html/body/div[3]/div[2]/div[2]/div[1]/div[3]/div/a[8]').click()
						
						time.sleep(25) 
						url = self.driver.current_url
						break
					except:
						try:
							self.driver.find_element_by_xpath('/html/body/div[3]/div[2]/div[2]/div[1]/div[3]/div/a[7]').click()
							
							time.sleep(25) 
							url = self.driver.current_url
							break
						except:
							try:
								self.driver.find_element_by_xpath('/html/body/div[3]/div[2]/div[2]/div[1]/div[3]/div/a[6]').click()
								time.sleep(25) 
								url = self.driver.current_url
								break
							except:
								try:
									self.driver.find_element_by_xpath('/html/body/div[3]/div[2]/div[2]/div[2]/div[3]/div/a[7]').click()
									time.sleep(25) 
									url = self.driver.current_url
								except:
									try:
										self.driver.find_element_by_xpath('/html/body/div[3]/div[1]/div[2]/div[2]/div[3]/div/a[7]').click()
										time.sleep(25) 
										url = self.driver.current_url
									except:
										try:
											self.driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/div[2]/div[1]/div[3]/div/a[7]').click()
											time.sleep(25) 
											url = self.driver.current_url
											break
										except:
											pass
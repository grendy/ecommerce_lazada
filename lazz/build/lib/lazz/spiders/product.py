import scrapy
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from scrapy.http import TextResponse
from lazz.items import Lproduct
from impala.dbapi import connect
import traceback
# import MySQLdb

import time


class ProductSpider(scrapy.Spider):
    name = "lazzada"
    allowed_domains = ["http://www.lazada.co.id/store-directory/"]
    start_urls = ["http://www.lazada.co.id/store-directory/"]
    def __init__(self): 
        path_to_chromedriver = 'D://chromedriver'
        self.driver = webdriver.Chrome(executable_path = path_to_chromedriver)
        # self.driver = webdriver.PhantomJS()
        
    def parse(self, response):
        # conn = connect(host="192.168.180.144", port=21050, database='data_id')
        # cur = conn.cursor()
        a=0
        for sc in range(0,18):
            a=a+1
            url = 'http://www.lazada.co.id/store-directory/'
            try:
                self.driver.get(url)
            except:
                print traceback.print_exc()
            time.sleep(10)
            for tidur in range(0,100):
                time.sleep(1)
                try:
                    self.driver.find_element_by_xpath('/html/body/div[2]/div/div['+str(a)+']/h2/a').click()
                    time.sleep(10)
                    url = self.driver.current_url
                    break
                except:
                    pass
            for click in range(0,240):
                response = TextResponse(url=response.url, body=self.driver.page_source, encoding='utf-8')
                b=0
                for barang in range (0,36):
                    b=b+1
                    if b==1:
                        pass
                    else:
                        try:
                            self.driver.get(url)
                            time.sleep(5)
                        except:
                            print traceback.print_exc()
                    for tidu in range(0,100):
                        time.sleep(1)
                        try:
                            self.driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[2]/div[1]/div[2]/div['+str(b)+']/a').click()
                            time.sleep(5)
                            break
                        except:
                            print traceback.print_exc()
                    time.sleep(30)
                    siap = self.driver.current_url
                    try:
                        response = TextResponse(url=response.url, body=self.driver.page_source, encoding='utf-8')
                        product_url = MySQLdb.escape_string(siap)
                        try:
                            penjual_url = MySQLdb.escape_string(response.xpath('//*[@id="prod_content_wrapper"]/div[2]/div[2]/div/div/div[1]/a/@href').extract_first())
                        except:
                            penjual_url = "Lazada"
                        kategori = MySQLdb.escape_string(response.xpath('/html/body/header/footer/div[2]/div[1]/ul/li[2]/span/a/span/text()').extract_first())
                        kategori_url = MySQLdb.escape_string(response.xpath('/html/body/header/footer/div[2]/div[1]/ul/li[2]/span/a/@href').extract_first())

                        nama_product = MySQLdb.escape_string(response.xpath('//*[@id="prod_title"]/text()').extract_first())
                        print product_url
                        print penjual_url
                        print kategori
                        print kategori_url
                        print nama_product
                        print "=============================================================================================="
                        harga = response.xpath('//*[@id="special_price_box"]/text()').extract_first()
                        
                        print harga
                        diskon = MySQLdb.escape_string(response.xpath('//*[@id="product_saving_percentage"]/text()').extract_first())
                        harga_sebelumnya = response.xpath('//*[@id="price_box"]/text()').extract_first()
                        c = 0
                        for spek in range(0,100):
                            try:
                                spek[c]= response.xpath('//*[@id="prod_content_wrapper"]/div[1]/div[2]/div/ul/li['+str(c+1)+']/span/text()').extract_first()
                                c=c+1
                            except:
                                break
                        spesifik = ""
                        for d in range(d,c):
                            spesifik =  spesifik + spek[d] + ", "
                        spesifikasi = spesifik
                        self.driver.find_element_by_xpath('//*[@id="prod_content_wrapper"]/div[2]/div[2]/div/div/div[1]/div/div/div').click()
                        rate = MySQLdb.escape_string(response.xpath('/html/body/div[6]/div[2]/h3/text()').extract_first())
                        metode_pembayaran = MySQLdb.escape_string(response.xpath('//*[@id="deliveryType"]/div[2]/div/div[2]/span/text()').extract_first())
                        d=0
                        for tabel in range(0,50):
                            d=d+1
                            berat = MySQLdb.escape_string(response.xpath('//*[@id="prd-detail-page"]/div/div[3]/div[2]/div[2]/table/tbody/tr['+str(d)+']/td[1]/text()').extract_first())
                            if berat == "Berat (kg)":
                                berat = MySQLdb.escape_string(response.xpath('//*[@id="prd-detail-page"]/div/div[3]/div[2]/div[2]/table/tbody/tr['+str(d)+']/td[2]/text()').extract_first())
                                break
                            else:
                                pass
                        d=0
                        for tabel in range(0,50):
                            d=d+1
                            ukuran = MySQLdb.escape_string(response.xpath('//*[@id="prd-detail-page"]/div/div[3]/div[2]/div[2]/table/tbody/tr['+str(d)+']/td[1]/text()').extract_first())
                            if ukuran == "Ukuran (L x W x H cm)":
                                ukuran = MySQLdb.escape_string(response.xpath('//*[@id="prd-detail-page"]/div/div[3]/div[2]/div[2]/table/tbody/tr['+str(d)+']/td[2]/text()').extract_first())
                                break
                            else:
                                pass 
                        d=0
                        for tabel in range(0,50):
                            d=d+1
                            garansi = MySQLdb.escape_string(response.xpath('//*[@id="prd-detail-page"]/div/div[3]/div[2]/div[2]/table/tbody/tr['+str(d)+']/td[1]/text()').extract_first())
                            if garansi == "Tipe garansi":
                                garansi = MySQLdb.escape_string(response.xpath('//*[@id="prd-detail-page"]/div/div[3]/div[2]/div[2]/table/tbody/tr['+str(d)+']/td[2]/text()').extract_first())
                                break
                            else:
                                pass 
                        deskripsi = MySQLdb.escape_string(response.xpath('//*[contains(@id,"shop")]/p/text()').extract_first())
                        try:   
                            penjual = MySQLdb.escape_string(response.xpath('//*[@id="prod_content_wrapper"]/div[2]/div[2]/div/div/div[1]/a/span/text()').extract_first())
                        except:
                            penjual = "Lazada"
                    except:
                        pass
                    try:
                        feed_nama = MySQLdb.escape_string(response.xpath('//*[@id="js_reviews_list"]/li/div[3]/span[2]/text()').extract_first())
                        tanggal = MySQLdb.escape_string(response.xpath('//*[@id="js_reviews_list"]/li/div[1]/span[3]/text()').extract_first())
                        #sentimen = MySQLdb.escape_string(response.xpath('//*[@id="review-container"]/li[1]/div/div/div/div[1]/div[2]/small[2]/div/div[2]/span/text()').extract_first())
                        pesan = MySQLdb.escape_string(response.xpath('//*[@id="js_reviews_list"]/li/div[2]/text()').extract_first())
                    except:
                        pass

                    # sql = "select * from tokopedia_product where product_url = '{}'".format(product_url)
                    # cur.execute(sql)
                    # results = cur.fetchall()
                    # if len(results) == 0:
                    #     sql = "INSERT INTO tokopedia_product VALUES ('{}','{}','{}','{}',{},'{}','{}','{}','{}','{}','{}')".format(product_url,kategori,kategori_url,nama_product,harga,kondisi,berat,dilihat,update_terakhir,terjual,deskripsi)
                    #     print sql
                    #     cur.execute(sql)
                    #     print "======================================"
                    #     print "[INFO] impala insert sukses : {}".format(sql)  
                    #     print "======================================"  
                    # else:
                    #     print "======================================"
                    #     print "[ERROR] impala insert failure : {}".format(sql)  
                    #     print "======================================"  
                    # ###############################
                    # sql = "select * from tokopedia_penjual where penjual_url = '{}'".format(penjual_url)
                    # cur.execute(sql)
                    # results = cur.fetchall()
                    # if len(results) == 0:
                    #     sql = "INSERT INTO tokopedia_penjual VALUES ('{}','{}','{}','{}')".format(penjual_url,penjual,lokasi,produk_terjual)
                    #     print sql
                    #     cur.execute(sql) 
                    #     print "======================================"
                    #     print "[INFO] impala insert sukses : {}".format(sql)  
                    #     print "======================================"  
                    # else:
                    #     print "======================================"
                    #     print "[ERROR] impala insert failure : {}".format(sql)  
                    #     print "======================================"  
                    # ##############################
                    # sql = "select * from tokopedia_feedback where product_url = '{}' and pesan = '{}' and penjual_url='{}'".format(product_url,feed_nama,tanggal,pesan)
                    # cur.execute(sql)
                    # results = cur.fetchall()
                    # if len(results) == 0:
                    #     sql = "INSERT INTO tokopedia_feedback VALUES ('{}','{}','{}','{}','{}')".format(product_url,penjual_url,feed_nama,tanggal,pesan)
                    #     print sql
                    #     cur.execute(sql) 
                    #     print "======================================"
                    #     print "[INFO] impala insert sukses : {}".format(sql)  
                    #     print "======================================"  
                    # else:
                    #     print "======================================"
                    #     print "[ERROR] impala insert failure : {}".format(sql)  
                    #     print "======================================"  
                    item = Lproduct()
                    item ['kategori'] = kategori
                    item ['kategori_url'] = kategori_url
                    item ['nama_product'] = nama_product
                    item ['product_url'] = product_url
                    item ['harga'] = harga
                    item ['harga_sebelumnya'] = harga_sebelumnya
                    item ['diskon'] = diskon
                    item ['spesifikasi'] = spesifikasi
                    item ['ukuran'] = ukuran
                    item ['berat'] = berat
                    item ['garansi'] = garansi
                    item ['metode_pembayaran'] = metode_pembayaran
                    item ['penjual'] = penjual
                    item ['rate'] = rate
                    item ['produk_terjual'] = produk_terjual
                    item ['feed_nama'] = feed_nama
                    item ['tanggal'] = tanggal
                    item ['pesan'] = pesan
                    yield item
                # try:
                #     self.driver.get(url)
                #     time.sleep(10)
                # except:
                #     print traceback.print_exc()
                # for lanjut in range(0,100):
                #     time.sleep(1)
                #     try:
                #         if "page" in url:
                #             try:
                #                 self.driver.find_element_by_xpath('//*[@id="product-list-container"]/div/div[2]/div/div[2]/div/ul/li[9]/a').click()
                #                 time.sleep(25) 
                #                 url = self.driver.current_url
                #                 break
                #             except:                       
                #                 self.driver.find_element_by_xpath('//*[@id="content-directory"]/div[2]/div/div[2]/div/ul/li[9]/a').click()
                #                 time.sleep(25) 
                #                 url = self.driver.current_url
                #                 break
                #         else:
                #             try:
                #                 self.driver.find_element_by_xpath('//*[@id="product-list-container"]/div/div[2]/div/div[2]/div/ul/li[8]/a').click()
                #                 time.sleep(25) 
                #                 url = self.driver.current_url
                #                 break
                #             except:
                #                 self.driver.find_element_by_xpath('//*[@id="content-directory"]/div[2]/div/div[2]/div/ul/li[8]/a').click()
                #                 time.sleep(25)
                #                 url = self.driver.current_url
                #                 break
                #     except:
                #         pass
        self.driver.close()
# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class LazzItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class Lproduct(scrapy.Item):
	kategori = scrapy.Field()
	kategori_url = scrapy.Field()
	product_url = scrapy.Field()
	penjual_url = scrapy.Field()
	nama_product = scrapy.Field()
	harga = scrapy.Field()
	diskon = scrapy.Field()
	harga_sebelumnya = scrapy.Field()
	spesifikasi = scrapy.Field()
	ukuran = scrapy.Field()
	berat = scrapy.Field()
	garansi = scrapy.Field()
	metode_pembayaran = scrapy.Field()
	penjual = scrapy.Field()
	rate = scrapy.Field()
	feed_nama = scrapy.Field()
	tanggal = scrapy.Field()
	pesan = scrapy.Field()
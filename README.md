# ecommerce_lazada
Crawling ecommerce lazada using scrapy and send json to kafka
##Understand the web structure
Must understand web structure like xpath and css selector
##Install scrapy on centos
```bash 
sudo rpm -Uvh http://dl.fedoraproject.org/pub/epel/7/x86_64/e/epel-release-7-5.noarch.rpm
yum update -y 
yum install python-pip -y 
yum install python-devel -y 
yum install gcc gcc-devel -y 
yum install libxml2 libxml2-devel -y 
yum install libxslt libxslt-devel -y 
yum install openssl openssl-devel -y 
yum install libffi libffi-devel -y 
CFLAGS="-O0" pip install lxml 
pip install scrapy 
```

##Install selenium
Selenium version must 2.53.6
```bash
pip install selenium
```
##Install xvfb and PyVirtualDisplay for running browser on background process
Python2.7 must be installed on the device
```bash
yum install xorg-x11-server-Xvfb 
pip install PyVirtualDisplay 
```
##Browser version
Browser used is Firefox browser
```bash
Firefox browser version must 45.0.2 or 45.xx.xx 
```
##Running browser on background process
To running browser on background process, install xvfb and pyVirtualDisplay
```bash
from pyvirtualdisplay import Display
display = Display(visible=0, size=(800,600)) 
display.start() 
driver = webdriver.Firefox() 
```
##Connect to mysql using MySQLdb library
Must insert mysql configuration into settings.py on scrapy </br>
```bash
conn=MySQLdb.connect(  
            host=crawler.settings['MYSQL_HOST'], 
            port=crawler.settings['MYSQL_PORT'], 
            user=crawler.settings['MYSQL_USER'],
            passwd=crawler.settings['MYSQL_PASS'],
            db=crawler.settings['MYSQL_DB'])
        return cls(conn)
```
##Take content
To take content in accordance required use xpath or css selector
```bash
response.xpath('//*[contains(@id, "frmSaveListing")]/ul/li[' + str(i) + ']//*[contains(@class, "article-right")]/span/text()').extract_first()
```
##To click button
To click , must be known id or xpath first
```bash
driver.find_element_by_id('s_imgBtnSearch').click()
```
##Running engine
To running engine use crontab for automatic scheduling
```bash
python2.7 lazada.py
```

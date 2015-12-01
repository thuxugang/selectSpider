微信/QQ群爬虫
===

一个基于Python和Selenium Webdriver的爬虫，负责获得一个用户所拥有的群的全部信息（人数/名单）。


安装方式：
---

* 安装Python 2.6+ (不支持3.0)
* 安装Selenium 2.48+ 'pip install selenium'
* 安装Chrome Webdriver
** 解压chromedriver.exe到Python的安装目录下，如C:\Python27。 
** 添加C:\Users\Administrator\AppData\Local\Google\Chrome\Application\（chrome安装路径，这里是win7下的安装路径）到环境变量path 


注意事项：
---

* 如果出现字符串混乱，请取消文件中下面的注释

<pre>
<code>
#import sys
#reload(sys)
#sys.setdefaultencoding('utf-8')
</code>
</pre>

Contributers:
---

* thuxugang

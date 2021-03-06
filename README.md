# MaoyanTop100


# 介绍
今天打算做一个小项目，爬取[猫眼电影top100](http://maoyan.com/board/4)

# 正文
**URL分析**
打开网址，发现Top100分为10页，每页10部电影，转到第二页分析URL
http://maoyan.com/board/4?offset=10
可以看到多了个offset参数，猜测是由offset来控制页面，于是转到第三页，发现offset变为20，猜测成立

**正则表达式分析**
接下来查看网页源码，可以发现所需要爬取的内容均在源码中，用requests库爬取html，然后正则表达式解析即可
![](https://img2018.cnblogs.com/blog/1318960/201809/1318960-20180904131226303-1543233641.png)
我们所需要爬取的是电影名称、主演、上映时间、评分，据此写出正则表达式如下
`regex = 'p class="name">.*?>(.*?)</a></p>.*?>(.*?)</p>.*?>(.*?)</p>.*?<i class="integer">(.*?)</i>.*?ion">(.*?)</i></p>'`
通过程序测试，爬取结果无误

**代码逻辑分析**
根据功能模块不同，将程序分为主函数、爬取函数、解析html函数、输出函数四个部分
主函数用循环传入offset的值到爬取函数,并初始化文件，为了防止因为爬取太快而被检测出爬虫，可以暂停一段时间再进行下一次爬取
```
def main():
	open('data.csv', 'w')
	for i in range(10):
		parse_html(get_html(i*10))
		print('finish', i)
		time.sleep(0.5)
	print('finish!')
```
爬取函数根据offset爬取页面html然后传给解析函数，解析函数根据正则表达式解析出所需要的内容传给输出函数，文件输出则用了比较简单的csv文件

**结果**
![](https://img2018.cnblogs.com/blog/1318960/201809/1318960-20180904131916040-1914927104.png)
部分结果贴图展示，代码和全部结果开源在[github](https://github.com/HackHarry/MaoyanTop100)上了

# 总结
这次实践是比较简单的，没有复杂的js部分，单纯解析html就好。爬取结果单从现在角度看只能用来补剧，但是如果隔段时间爬取一次，也许可以做一个数据分析，到时候可以做个Top10电影以及评分变化折线图

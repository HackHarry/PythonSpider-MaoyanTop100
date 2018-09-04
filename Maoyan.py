import requests
import re
import time
import csv

def get_html(number):
	url = 'http://maoyan.com/board/4'
	headers = {
			'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
			'Accept-Encoding': 'gzip, deflate, sdch',
			'Accept-Language': 'zh-CN,z;q=0.8'
		}
	payload = {
			'offset': number
		}
	response = requests.get(url, headers=headers, params=payload)
	if response.status_code == 200:
		return(response.text)
	return None
	
def parse_html(html):
	regex = 'p class="name">.*?>(.*?)</a></p>.*?>(.*?)</p>.*?>(.*?)</p>.*?<i class="integer">(.*?)</i>.*?ion">(.*?)</i></p>'
	
	results = re.findall(regex, html, re.S)
	print_csv(results)
	'''
	for result in results:
		for i in range(5):
			print(result[i])
	result = re.search(regex, html, re.S)
	print(result.group(1), result.group(4), result.group(5))
	'''

def print_csv(results):
	with open('data.csv', 'a') as csvfile:
		writer = csv.writer(csvfile, lineterminator='\n')
		for result in results:
			r = result[3].strip() + result[4].strip()
			writer.writerow([result[0], result[1].strip(), result[2].strip(), r])

def main():
	open('data.csv', 'w')
	for i in range(10):
		parse_html(get_html(i*10))
		print('finish', i)
		time.sleep(0.5)
	print('finish!')
	
if __name__ == '__main__':
	main()

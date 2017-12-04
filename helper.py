import requests
from fake_useragent import UserAgent
import re
from bs4 import BeautifulSoup

def read_URL(URL):
	header = {'User-Agent':str(UserAgent().chrome)}
	html = requests.get(URL, headers=header)
	return html.text

def cut_text(text, start, end):
	sloc = text.find(start)
	eloc = text[sloc:].find(end)
	return text[sloc: sloc+eloc+len(end)]

def get_URLs(text):
	# urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', text)
	soup = BeautifulSoup(text, "html.parser")
	anchors = soup.findAll("a")
	links = []
	for a in anchors:
		links.append(a["href"])
	return links

# f = open("catalog.txt", "r")
# cut = cut_text(f.read(), "<h3>Graduate Subjects</h3>", "</ul>")
# urls = get_URLs(cut)

# for i in urls:
# 	print(i)
def process_course_code(link):
	rlink = link[::-1]
	c_end = rlink.find("_")
	c = rlink[:c_end][::-1]

	rlink = rlink[c_end + 1:]
	n_start = rlink.find("_")
	n_end 	= rlink[n_start + 1:].find("_")
	n = rlink[n_start + 1: n_start + n_end + 1][::-1]
	return(n + " " + c)

def process_course(link):
	read = read_URL(link)
	print(read)

	title = cut_text(read, "id='page-title'>", "</h2>")[16:-5]
	code = process_course_code(link)

	sessions = []
	return (code, title, sessions)

# link = "https://www.umb.edu/academics/course_catalog/course_info/ugrd_ASIAN_2018 Spring_115L"
# link = "https://www.umb.edu/academics/course_catalog/course_info/ugrd_ART_2018 Spring_380"
# link = "https://www.umb.edu/academics/course_catalog/course_info/grd_SPE G_2018%20Spring_621"
link = "https://www.umb.edu/academics/course_catalog/course_info/ugrd_CS_2018 Spring_110"
print(process_course(link))
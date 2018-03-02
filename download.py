from helper import *
import json, os

URL = "https://www.umb.edu/academics/course_catalog/subjects/2018%20Spring"
SEM = "2018 Spring"
DATA = "DATA"

# Get the catalog page
text = read_URL(URL)

# Get the list of majors 
urls = get_URLs(cut_text(text, "<h3>Undergraduate Subjects</h3>", "</ul>")) \
	 + get_URLs(cut_text(text, "<h3>Graduate Subjects</h3>", "</ul>"))

for url in urls:
	if not os.path.exists(DATA): os.makedirs(DATA)
	for i in get_URLs(read_URL(url), "course_info"):
		title = i[i.find("grd_")+len("grd_"):].replace('_' + SEM + '_', '_')
		with open(DATA + "/" + title + ".txt", "w") as file:
			file.write(read_URL(i))
			print("Processed", title)

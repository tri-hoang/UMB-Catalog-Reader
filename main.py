from helper import *

URL = "https://www.umb.edu/academics/course_catalog/subjects/2018%20Spring"
SEM = "<p>2018 Spring"

# Get the catalog page
text = read_URL(URL)

# Get the list of majors
cut = cut_text(text, "<h3>Undergraduate Subjects</h3>", "</ul>")
urls = get_URLs(cut)

cut = cut_text(text, "<h3>Graduate Subjects</h3>", "</ul>")
urls += get_URLs(cut)

majors = []	
for i in urls:
	read = read_URL(i)
	title = cut_text(read, "page-title", "</h2>")[12:-5]
	m_url = cut_text(read, SEM, "</div>")
	m_urls = get_URLs(m_url)
	courses = []
	for j in m_urls:
		courses += process_course(j)
	major = {"title": title, "courses": courses}
	majors += major

print(majors)
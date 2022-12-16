#!/usr/bin/env python3

def main():

	movies = make_movie_data()

	cool_beans(movies)
	katuni(movies)

	push_changes()

from os.path import exists

def cool_beans(movies):

	title = 'Cool Beans BV'

	print(f'site({title})')

	contact = "+31 (0) 650281410"
	address = "Haarlemmerweg 315D<br>1051 LG, Amsterdam<br>Nederland"
	
	accent_color1 = "blue"
	accent_color2 = "lime"
	accent_color3 = "red"

	accent_contrast1 = "red"
	accent_contrast2 = "blue"
	accent_contrast3 = "lime"
	
	logo_url = 'https://github.com/mwinokan/RichardSites/blob/main/assets/cool_beans_logo.png?raw=true'

	text_buffer = 'Cool Beans BV is run by producers Richard Claus and Chantal Nissen, the Amsterdam animation outfit Katuni and the German Comet Film are its sister companies.</p><p>All of Cool Beans productions are international co-productions, including <i>Black Butterflies</i>, <i>The Price of Sugar</i>, <i>An Act of Defiance</i> and the recent 3D animated films <i>The Little Vampire 3D</i> (2017) in co-production with A. Film (Denmark) and <i>Ainbo</i> (2020) in co-production with Tunche Films (Peru).</p><p>The next 3D animated film coming from Cool Beans and Katuni is <i>Panda Bear in Africa</i>, which is set to start animation end of 2021. Le Pacte (France) joined the successful Dutch/German/Danish team that produced <i>The Little Vampire 3D</i> as the French co-producer in 2019, and sales agent CMG – Cinema Management Group has already sold an astonishing number of territories. There is still room for co-producers, animation studios and other partners to come on board.</p><p>Cool Beans’ development slate also includes new live action films, among others the Dutch “multiculti” comedy <i>Matties</i> and the historic drama <i>Tutuba</i>; the series <i>Panama Panic</i> and the animated series <i>The Little Vampire</i>.'

	html_buffer = create_site(address, accent_color1, accent_color2, accent_color3, accent_contrast1, accent_contrast2, accent_contrast3, contact, logo_url, title, text_buffer,movies)

	write_buffer(html_buffer,subdir='cool_beans')

def katuni(movies):
	
	title = 'Katuni Animation'

	print(f'site({title})')

	contact = "+31 (0) 650281410"
	address = "Haarlemmerweg 315D<br>1051 LG, Amsterdam<br>Nederland"
	
	accent_color1 = "tomato"
	accent_color2 = "SlateBlue"
	accent_color3 = "DarkRed"

	accent_contrast1 = "black"
	accent_contrast2 = "white"
	accent_contrast3 = "white"
	
	logo_url = 'https://github.com/mwinokan/RichardSites/blob/main/assets/katuni_logo.jpg?raw=true'

	text_buffer = 'Cool Beans BV is run by producers Richard Claus and Chantal Nissen, the Amsterdam animation outfit Katuni and the German Comet Film are its sister companies.</p><p>All of Cool Beans productions are international co-productions, including <i>Black Butterflies</i>, <i>The Price of Sugar</i>, <i>An Act of Defiance</i> and the recent 3D animated films <i>The Little Vampire 3D</i> (2017) in co-production with A. Film (Denmark) and <i>Ainbo</i> (2020) in co-production with Tunche Films (Peru).</p><p>The next 3D animated film coming from Cool Beans and Katuni is <i>Panda Bear in Africa</i>, which is set to start animation end of 2021. Le Pacte (France) joined the successful Dutch/German/Danish team that produced <i>The Little Vampire 3D</i> as the French co-producer in 2019, and sales agent CMG – Cinema Management Group has already sold an astonishing number of territories. There is still room for co-producers, animation studios and other partners to come on board.</p><p>Cool Beans’ development slate also includes new live action films, among others the Dutch “multiculti” comedy <i>Matties</i> and the historic drama <i>Tutuba</i>; the series <i>Panama Panic</i> and the animated series <i>The Little Vampire</i>.'

	html_buffer = create_site(address, accent_color1, accent_color2, accent_color3, accent_contrast1, accent_contrast2, accent_contrast3, contact, logo_url, title, text_buffer,movies)

	write_buffer(html_buffer,subdir='katuni')

def create_site(address,accent_color1,accent_color2,accent_color3,accent_contrast1,accent_contrast2,accent_contrast3,contact,logo_url,title,text_buffer,movies,max_width=4000,slideshow_auto=False,slideshow_rate=5):

	# preamble
	html_buffer = '<!DOCTYPE html>'
	html_buffer += '<html>\n'
	html_buffer += '<head>\n'
	html_buffer += f'<title>{title}</title>\n'
	html_buffer += '<meta charset="UTF-8">\n'
	html_buffer += '<meta name="viewport" content="width=device-width, initial-scale=1">\n'
	html_buffer += '<link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">\n'
	html_buffer += '<link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Oswald">\n'
	html_buffer += '<link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Open Sans">\n'
	html_buffer += '<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">\n'

	# styling
	html_buffer += '<style>\n'
	html_buffer += 'h1,h2,h3,h4,h5,h6 {font-family: "Oswald"}body {font-family: "Open Sans"}\n'
	html_buffer += '.mySlides {display:none}\n'
	html_buffer += '.w3-left, .w3-right, .w3-badge {cursor:pointer}\n'
	html_buffer += '.w3-badge {height:13px;width:13px;padding:0}\n'
	html_buffer += '</style>\n'
	html_buffer += '</head>\n'

	# begin body
	html_buffer += '<body>\n'
	html_buffer += f'<div class="w3-content" style="max-width:{max_width}px">\n'

	# top bar (one dynamic and one static)
	html_buffer += '<header>\n'
	html_buffer += '<div class="w3-top">\n'
	html_buffer += '<div class="w3-bar w3-center w3-padding-large" style="background-color:white">\n'
	html_buffer += f'<img src="{logo_url}" alt="{title} Logo" style="width:40%;max-width:200px">\n'
	html_buffer += '</div>\n'
	html_buffer += '</div>\n'
	html_buffer += '</header>\n'
	html_buffer += '<div class="w3-bar w3-center w3-padding w3-white">\n'
	html_buffer += f'<img src="{logo_url}" alt="{title} Logo" style="width:40%;max-width:200px">\n'
	html_buffer += '</div>\n'

	### screencap slideshow

	subset = [d for d in movies if d.has_screencap]
	print(f'#movies w/ screencap_url = {len(subset)}')
	assert len(subset) > 1

	# screencap slideshow
	html_buffer += f'<div class="w3-content w3-display-container w3-dark-grey" style="width:100%;max-width:{max_width}px">\n'

	for d in subset:
		html_buffer += '<div class="w3-display-container mySlides"> \n'
		html_buffer += f'<img src="{d.screencap_url}" style="width:100%">\n'
		html_buffer += f'<div class="w3-padding w3-display-bottomleft w3-text-white"><h3>{d.title}</h3></div>\n'
		html_buffer += '</div>\n'

	if not slideshow_auto:
		# arrow buttons
		html_buffer += '<div class="w3-center w3-container w3-section w3-large w3-text-white w3-display-middle" style="width:100%">\n'
		html_buffer += '<div class="w3-left" onclick="plusDivs(-1)">&#10094;</div>\n'
		html_buffer += '<div class="w3-right" onclick="plusDivs(1)">&#10095;</div>\n'
		html_buffer += '</div>\n'

	html_buffer += '</div>\n'

	if not slideshow_auto:
		# slideshow scripting (manual)
		html_buffer += '<script>\n'

		html_buffer += 'function getRandomInt(max) {\n'
		html_buffer += '  return Math.floor(Math.random() * max);\n'
		html_buffer += '}\n'
		# html_buffer += 'var slideIndex = 1;\n'
		html_buffer += f'var slideIndex = getRandomInt({len(subset)});\n'
		html_buffer += 'showDivs(slideIndex);\n'
		html_buffer += 'function plusDivs(n) {\n'
		html_buffer += '  showDivs(slideIndex += n);\n'
		html_buffer += '}\n'
		html_buffer += 'function currentDiv(n) {\n'
		html_buffer += '  showDivs(slideIndex = n);\n'
		html_buffer += '}\n'
		html_buffer += 'function showDivs(n) {\n'
		html_buffer += '  var i;\n'
		html_buffer += '  var x = document.getElementsByClassName("mySlides");\n'
		html_buffer += '  var dots = document.getElementsByClassName("demo");\n'
		html_buffer += '  if (n > x.length) {slideIndex = 1}\n'
		html_buffer += '  if (n < 1) {slideIndex = x.length}\n'
		html_buffer += '  for (i = 0; i < x.length; i++) {\n'
		html_buffer += '    x[i].style.display = "none";  \n'
		html_buffer += '  }\n'
		html_buffer += '  for (i = 0; i < dots.length; i++) {\n'
		html_buffer += '    dots[i].className = dots[i].className.replace(" w3-white", "");\n'
		html_buffer += '  }\n'
		html_buffer += '  x[slideIndex-1].style.display = "block";  \n'
		html_buffer += '  dots[slideIndex-1].className += " w3-white";\n'
		html_buffer += '}\n'
		html_buffer += '</script>\n'
	else:
		# slideshow scripting (auto)
		html_buffer += '<script>\n'
		html_buffer += 'var myIndex = 0;\n'
		html_buffer += 'carousel();\n'
		html_buffer += 'function carousel() {\n'
		html_buffer += '  var i;\n'
		html_buffer += '  var x = document.getElementsByClassName("mySlides");\n'
		html_buffer += '  for (i = 0; i < x.length; i++) {\n'
		html_buffer += '    x[i].style.display = "none";  \n'
		html_buffer += '  }\n'
		html_buffer += '  myIndex++;\n'
		html_buffer += '  if (myIndex > x.length) {myIndex = 1}    \n'
		html_buffer += '  x[myIndex-1].style.display = "block";  \n'
		html_buffer += f'  setTimeout(carousel, {slideshow_rate}000);\n'
		html_buffer += '}\n'
		html_buffer += '</script>\n'

	# text content
	html_buffer += '<div class="w3-content" style="max-width:800px">\n'
	html_buffer += '<div class="w3-container w3-padding-large">\n'
	html_buffer += '<h2>Who are we?</h2>\n'
	html_buffer += '<p>\n'

	html_buffer += text_buffer

	html_buffer += '</p>	\n'
	html_buffer += '</div>\n'
	html_buffer += '</div>\n'

	# headshots
	html_buffer += '<div class="w3-content" style="max-width:600px">\n'
	html_buffer += '<div class="w3-cell-row">\n'
	html_buffer += '<div class="w3-container w3-cell w3-center">\n'
	html_buffer += '<img src="https://github.com/mwinokan/RichardSites/blob/main/assets/Richard_Claus_1.jpg?raw=true" alt="Richard_Claus_1" style="width:100%;max-width:200px" class="w3-padding">\n'
	html_buffer += '<h4 style="color:black">Richard Claus</h4>\n'
	# html_buffer += '<p>+31 (0) 650281410\n'
	html_buffer += '<p>rc@coolbeanspix.com</p>\n'
	html_buffer += '</div>\n'
	html_buffer += '<div class="w3-container w3-cell w3-center">\n'
	html_buffer += '<img src="https://github.com/mwinokan/RichardSites/blob/main/assets/Chantal_Nissen.jpg?raw=true" alt="Chantal_Nissen" style="width:100%;max-width:200px" class="w3-padding">\n'
	html_buffer += '<h4 style="color:black">Chantal Nissen</h4>\n'
	html_buffer += '<p>cn@coolbeanspix.com</p>\n'
	html_buffer += '</div>\n'
	html_buffer += '</div>\n'
	html_buffer += '</div>\n'

	# next section heading
	# html_buffer += f'<div class="w3-content w3-topbar w3-center" style="max-width:{max_width}px">\n'
	html_buffer += '<br>\n'
	html_buffer += '<br>\n'
	html_buffer += f'<div class="w3-content w3-center w3-text-white w3-padding-large" style="max-width:{max_width}px;background-color:{accent_color1}">\n'
	html_buffer += '<h2>Projects</h2>\n'
	html_buffer += '</div>\n'
	html_buffer += '<br>\n'

	# poster grid
	html_buffer += f'<div class="w3-content w3-padding-large" style="max-width:{max_width}px">\n'
	html_buffer += '<div class="w3-container">\n'

	subset = [d for d in movies if d.has_poster]
	print(f'#movies w/ poster_url = {len(subset)}')
	assert len(subset) > 0

	start = 0
	end = len(subset)
	step = 3
	for i in range(start, end, step):
		x = i
		chunk = subset[x:x+step]

		html_buffer += '<div class="w3-row">\n'

		for d in chunk:
			# html_buffer += f'<div class="w3-display-container w3-third w3-mobile w3-padding-large" style="padding-left:0px;padding-right:0px">\n'
			html_buffer += f'<div class="w3-col l4 m12 s12 w3-padding-large" style="padding-left:0px;padding-right:0px">\n'
			
			# movie poster
			html_buffer += f'<a href="{d.target_url}"><img class="w3-card-4 w3-hover-opacity" src="{d.poster_url}" alt="{d.title} Poster" style="width:100%"></a>\n'

			# info panel
			html_buffer += f'<div class="w3-container">\n'
			html_buffer += f'<h2>{d.title}</h2>\n'
			# html_buffer += f'<div class="w3-container w3-display-container" style="padding-left:0px;padding-right:0px">\n'
			html_buffer += f'<p>{d.description}\n'
			html_buffer += f'<i id="show_{d.name}" class="fa fa-plus" style="color:{accent_color1}" onclick="showDetail(\'{d.name}\')"></i>\n'
			html_buffer += '</p>\n'
			# html_buffer += '</div>\n'

			html_buffer += f'<div id="{d.name}_detail" style="display:none">\n'
			html_buffer += f'<p>{d.description}\n'
			html_buffer += f'<i class="fa fa-close" style="color:{accent_color1}" onclick="hideDetail(\'{d.name}\')"></i>\n'
			html_buffer += '</p>\n'
			html_buffer += '</div>\n'
			# html_buffer += f'<button id="hide_{d.name}" class="w3-btn" style="background-color:{accent_color1};color:{accent_contrast1};display:none" onclick="hideDetail(\'{d.name}\')">Less</button>\n'
			html_buffer += f'<a href="{d.imdb_url}" class="w3-btn" style="background-color:{accent_color2};color:{accent_contrast2}">IMDb</a>\n'
			if d.trailer_url:
				html_buffer += f'<a href="{d.trailer_url}" class="w3-btn" style="background-color:{accent_color3};color:{accent_contrast3}">Trailer</a>\n'
			html_buffer += '</div>\n'
			html_buffer += '</div>\n'

		html_buffer += '</div>\n'

	html_buffer += '</div>\n'
	html_buffer += '</div>\n'

	html_buffer += '<script>\n'
	html_buffer += """
					function showDetail(ID) {
						document.getElementById(ID+"_detail").style.display = "block";
						document.getElementById("show_"+ID).style.display = "none";
					}
					function hideDetail(ID) {
						document.getElementById(ID+"_detail").style.display = "none";
						document.getElementById("show_"+ID).style.display = "block";
					}
					"""
	html_buffer += '</script>\n'

	# end body
	html_buffer += '</body>\n'

	# footer
	html_buffer += f'<footer class="w3-container" style="padding:32px;background-color:{accent_color1}">\n'
	html_buffer += '<div class="w3-center w3-text-white">\n'
	html_buffer += f'<p style="color:{accent_color2}"><strong>{title}</strong></p>\n'
	html_buffer += f'<p>{address}</p>\n'
	html_buffer += f'<p>{contact}</p>\n'
	html_buffer += f'</ul><a href="#" class="w3-button w3-padding w3-margin-bottom" style="background-color:{accent_color1};color:{accent_color3}"><i class="fa fa-arrow-up w3-margin-right"></i>Back to top</a>\n'
	html_buffer += '</div>\n'
	html_buffer += '</footer>\n'
	html_buffer += '</html>\n'

	return html_buffer

class Movie():
	def __init__(self,name,title,year,imdb_url,description,trailer_url=None,more_data=None):
		self.name = name
		self.title = title
		self.year = year
		self.description = description
		self.more_data = more_data
		self.trailer_url = trailer_url
		self.imdb_url = imdb_url

	@property
	def target_url(self):
		return self.trailer_url or self.imdb_url

	@property
	def has_screencap(self):
		return exists(f'assets/{self.name}_screen.jpg')

	@property
	def has_poster(self):
		return exists(f'assets/{self.name}_poster.jpg')
	
	@property
	def screencap_url(self):
		return f'https://github.com/mwinokan/RichardSites/blob/main/assets/{self.name}_screen.jpg?raw=true'

	@property
	def poster_url(self):
		return f'https://github.com/mwinokan/RichardSites/blob/main/assets/{self.name}_poster.jpg?raw=true'

def make_movie_data():
	# data
	movies = []
	movies.append(Movie('ainbo', 
		'AINBO - Spirit of the Amazon', 
		2021, 
		'https://www.imdb.com/title/tt6570098/', 
		'Ainbo was born and grew up in the deepest jungle of the Amazon. One day she discovers that her homeland is being threatened by illegal and ruthless mining. Using the help of her spirit guides Vaca and Dillo she embarks on a journey to save her land and save her people before it’s too late.',
		'https://www.youtube.com/watch?v=VtJmptdYyEk'))
	movies.append(Movie('panda',
		'Panda Bear in Africa', 
		2023, 
		'https://www.imdb.com/title/tt13616980/', 
		"A fun and adventurous young Panda travels from China to Africa to rescue his best friend, Jielong the Dragon, who has been kidnapped. On his journey he discovers a world completely unknown to him and faces frightening hippos, suspicious hyenas and wise gorillas. Relying on his wits (and some new found friends) he makes his way across Africa, before rescuing Jielong and saving his new friends' jungle home. A family entertainment comedy, a fish out of water/coming of age story."))
	movies.append(Movie('bram', 
		'Bram Fischer', 
		2017, 
		"https://www.imdb.com/title/tt6002522",
		"In apartheid-ruled South Africa, a renowned lawyer struggles to hide his secret affiliation to the nation's chief resistance movement - as he takes on defending a group of its arrested members, including its leader, Nelson Mandela.",
		'https://www.youtube.com/watch?v=uRNEaoX-SKQ'))
	movies.append(Movie('vampire', 
		'The Little Vampire 3D', 
		2017, 
		"https://www.imdb.com/title/tt4729560",
		"Rudolph, a 13-year-old vampire, meets Tony, a mortal boy his age who loves old castles, graveyards and vampires. Tony helps Rudolph to fight against a notorious vampire hunter, and together they save Rudolph's family and become friends.",
		'https://www.youtube.com/watch?v=IUDGUmJir50'))
	movies.append(Movie('sugar', 
		'Price of Sugar', 
		2013, 
		'https://www.imdb.com/title/tt2691498', 
		"The Price Of Sugar tells the alternately gripping, romantic and heart-wrenching story of Sarith and Mini-Mini as they grow up on the sugar plantations of Suriname in the latter half of the eighteenth century. Where Sarith is the most beautiful woman in the colony, the mulatto Mini-Mini is forever in her shadow, slave to her own half-sister.",
		'https://www.youtube.com/watch?v=js-lnZG74QA'))
	movies.append(Movie('butterflies', 
		'Black Butterflies', 
		2011, 
		'https://www.imdb.com/title/tt0906778', 
		"In Apartheid-torn South Africa, poet Ingrid Jonker (Carice van Houten) struggles tragically in search of love and a sense of home.",
		'https://www.youtube.com/watch?v=Fr-Op9-HZhA'))
	movies.append(Movie('thief', 
		'The Thief Lord', 
		2006, 
		'https://www.imdb.com/title/tt0430674', 
		"After their mother dies, two boys flee their mean aunt and head for Venice, Italy, where they meet Scipio, the mysterious \"Thief Lord.\" Along with a small gang of abandoned kids, the boys start robbing the rich to support themselves.",
		'https://youtu.be/KFQvMHUU3ko'))
	movies.append(Movie('heineken', 
		'De Heineken Ontvoering', 
		2015, 
		'https://www.imdb.com/title/tt2917388', 
		"The inside story of the planning, execution, rousing aftermath, and ultimate downfall of the kidnappers of beer tycoon Alfred \"Freddy\" Heineken in 1983, which resulted in the largest ransom ever paid for an individual.",
		'https://youtu.be/LttABogMVPw'))
	movies.append(Movie('vampire2000', 
		'The Little Vampire', 
		2000, 
		'https://www.imdb.com/title/tt0192255', 
		"A lonely American boy living in Scotland makes a new best friend, a fellow nine year-old who happens to be a vampire."
		'https://youtu.be/HRHWVeVFVf8'))
	movies.append(Movie('witness', 
		'Mute Witness', 
		1995, 
		'https://www.imdb.com/title/tt0110604', 
		"A mute make-up artist working on a slasher movie being shot in Moscow, is locked in the studio after hours. While there, she witnesses a brutal murder, and must escape capture.",
		'https://youtu.be/Ss5Hw3uiArs'))
	movies = sorted(movies,key=lambda x: x.year, reverse=True)
	print(f'#movies = {len(movies)}')
	return movies

def write_buffer(html_buffer,subdir=None):
	# write buffer
	if subdir:
		f = open(f'{subdir}/index.html','wt')
	else:
		f = open("index.html",'wt')
	f.write(html_buffer)

def push_changes():
	print(f"push_changes()")
	import os
	os.system(f'git add *.py assets/* */index.html; git commit -m "auto-generated"; git push')

if __name__ == '__main__':
	main()

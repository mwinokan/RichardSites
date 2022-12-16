#!/usr/bin/env python3

from os.path import exists

# parameters
max_width = 4000 # px

# urls
logo_url = 'https://github.com/mwinokan/RichardSites/blob/main/assets/cool_beans_logo.jpg?raw=true'

# detail
title = 'Cool Beans BV'

class Movie():
	def __init__(self,name,title,year,target_url,description):
		self.name = name
		self.title = title
		self.year = year
		self.target_url = target_url
		self.description = description
	
	@property
	def has_screencap(self):
		return exists(f'../assets/{self.name}_screen.jpg')

	@property
	def has_poster(self):
		return exists(f'../assets/{self.name}_poster.jpg')
	
	@property
	def screencap_url(self):
		return f'https://github.com/mwinokan/RichardSites/blob/main/assets/{self.name}_screen.jpg?raw=true'

	@property
	def poster_url(self):
		return f'https://github.com/mwinokan/RichardSites/blob/main/assets/{self.name}_poster.jpg?raw=true'

# data
movies = []

movies.append(Movie('ainbo', 'AINBO - Spirit of the Amazon', 2021, 'https://www.youtube.com/watch?v=VtJmptdYyEk', 'Ainbo was born and grew up in the deepest jungle of the Amazon. One day she discovers that her homeland is being threatened by illegal and ruthless mining. Using the help of her spirit guides Vaca and Dillo she embarks on a journey to save her land and save her people before it’s too late.'))

movies.append(Movie('panda', 'Panda Bear in Africa', 2023, 'https://www.imdb.com/title/tt13616980/', "A fun and adventurous young Panda travels from China to Africa to rescue his best friend, Jielong the Dragon, who has been kidnapped. On his journey he discovers a world completely unknown to him and faces frightening hippos, suspicious hyenas and wise gorillas. Relying on his wits (and some new found friends) he makes his way across Africa, before rescuing Jielong and saving his new friends' jungle home. A family entertainment comedy, a fish out of water/coming of age story."))

movies.append(Movie('bram', 'Bram Fischer', 2017, 'https://www.youtube.com/watch?v=uRNEaoX-SKQ', "In apartheid-ruled South Africa, a renowned lawyer struggles to hide his secret affiliation to the nation's chief resistance movement - as he takes on defending a group of its arrested members, including its leader, Nelson Mandela."))

movies.append(Movie('vampire', 'The Little Vampire 3D', 2017, 'https://www.youtube.com/watch?v=IUDGUmJir50', "Rudolph, a 13-year-old vampire, meets Tony, a mortal boy his age who loves old castles, graveyards and vampires. Tony helps Rudolph to fight against a notorious vampire hunter, and together they save Rudolph's family and become friends."))

movies.append(Movie('sugar', 'Price of Sugar', 2013, 'https://www.youtube.com/watch?v=js-lnZG74QA', "The Price Of Sugar tells the alternately gripping, romantic and heart-wrenching story of Sarith and Mini-Mini as they grow up on the sugar plantations of Suriname in the latter half of the eighteenth century. Where Sarith is the most beautiful woman in the colony, the mulatto Mini-Mini is forever in her shadow, slave to her own half-sister."))

movies.append(Movie('butterflies', 'Black Butterflies', 2011, 'https://www.youtube.com/watch?v=Fr-Op9-HZhA', "In Apartheid-torn South Africa, poet Ingrid Jonker (Carice van Houten) struggles tragically in search of love and a sense of home."))

movies = sorted(movies,key=lambda x: x.year, reverse=True)
print(f'#movies = {len(movies)}')

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
html_buffer += '<!-- <div class="w3-bar w3-center w3-padding" style="background-color:blue"> -->\n'
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

# arrow buttons
html_buffer += '<div class="w3-center w3-container w3-section w3-large w3-text-white w3-display-middle" style="width:100%">\n'
html_buffer += '<div class="w3-left w3-hover-text-black" onclick="plusDivs(-1)">&#10094;</div>\n'
html_buffer += '<div class="w3-right w3-hover-text-black" onclick="plusDivs(1)">&#10095;</div>\n'
html_buffer += '</div>\n'

html_buffer += '<div class="w3-center w3-container w3-section w3-large w3-text-white w3-display-bottommiddle" style="width:100%">\n'
for i,d in enumerate(subset):
	html_buffer += f'<span class="w3-badge demo w3-border w3-transparent w3-hover-black" onclick="currentDiv({i+1})"></span>\n'

html_buffer += '</div>\n'
html_buffer += '</div>\n'

# slideshow scripting
html_buffer += '<script>\n'
html_buffer += 'var slideIndex = 1;\n'
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

# text content
html_buffer += '<div class="w3-content" style="max-width:800px">\n'
html_buffer += '<div class="w3-container w3-padding-large">\n'
html_buffer += '<h2>Who are we?</h2>\n'
html_buffer += '<p>\n'
html_buffer += 'Cool Beans BV is run by producers Richard Claus and Chantal Nissen, the Amsterdam animation outfit Katuni and the German Comet Film are its sister companies.\n'
html_buffer += '</p><p>\n'
html_buffer += 'All of Cool Beans productions are international co-productions, including <i>Black Butterflies</i>, <i>The Price of Sugar</i>, <i>An Act of Defiance</i> and the recent 3D animated films <i>The Little Vampire 3D</i> (2017) in co-production with A. Film (Denmark) and <i>Ainbo</i> (2020) in co-production with Tunche Films (Peru).\n'
html_buffer += '</p><p>\n'
html_buffer += 'The next 3D animated film coming from Cool Beans and Katuni is <i>Panda Bear in Africa</i>, which is set to start animation end of 2021. Le Pacte (France) joined the successful Dutch/German/Danish team that produced <i>The Little Vampire 3D</i> as the French co-producer in 2019, and sales agent CMG – Cinema Management Group has already sold an astonishing number of territories. There is still room for co-producers, animation studios and other partners to come on board.\n'
html_buffer += '</p><p>\n'
html_buffer += 'Cool Beans’ development slate also includes new live action films, among others the Dutch “multiculti” comedy <i>Matties</i> and the historic drama <i>Tutuba</i>; the series <i>Panama Panic</i> and the animated series <i>The Little Vampire</i>.\n'
html_buffer += '</p>	\n'
html_buffer += '</div>\n'
html_buffer += '</div>\n'

# headshots
html_buffer += '<div class="w3-content" style="max-width:600px">\n'
html_buffer += '<div class="w3-cell-row">\n'
html_buffer += '<div class="w3-container w3-cell w3-center">\n'
html_buffer += '<img src="https://github.com/mwinokan/RichardSites/blob/main/assets/Richard_Claus_1.jpg?raw=true" alt="Richard_Claus_1" style="max-width:200px" class="w3-padding">\n'
html_buffer += '<h4 style="color:black">Richard Claus</h4>\n'
html_buffer += '</div>\n'
html_buffer += '<div class="w3-container w3-cell w3-center">\n'
html_buffer += '<img src="https://github.com/mwinokan/RichardSites/blob/main/assets/Chantal_Nissen.jpg?raw=true" alt="Chantal_Nissen" style="max-width:200px" class="w3-padding">\n'
html_buffer += '<h4 style="color:black">Chantal Nissen</h4>\n'
html_buffer += '</div>\n'
html_buffer += '</div>\n'
html_buffer += '</div>\n'

# next section heading
html_buffer += f'<div class="w3-content w3-topbar w3-center" style="max-width:{max_width}px">\n'
# html_buffer += '<h2>Current Projects</h2>\n'
html_buffer += '</div>\n'

# poster grid
html_buffer += f'<div class="w3-content w3-padding-large" style="max-width:{max_width}px">\n'
html_buffer += '<div class="w3-container">\n'

subset = [d for d in movies if d.has_poster]
print(f'#movies w/ poster_url = {len(subset)}')
assert len(subset) > 0

for d in subset:
	html_buffer += f'<div class="w3-display-container w3-third w3-mobile w3-padding-large" onclick="openCity(\'{d.name}\')" style="padding-left:0px;padding-right:0px">\n'
	
	# movie poster
	html_buffer += f'<a href="{d.target_url}"><img class="w3-card-4 w3-hover-opacity" src="{d.poster_url}" alt="{d.title} Poster" style="width:100%"></a>\n'

	# info panel
	html_buffer += f'<div id="{d.name}" class="w3-container w3-display-container">\n'
	html_buffer += f'<h2>{d.title}</h2>\n'
	html_buffer += f'<p>{d.description}</p>\n'
	html_buffer += '</div>\n'
	html_buffer += '</div>\n'

html_buffer += '</div>\n'
html_buffer += '</div>\n'

# end body
html_buffer += '</body>\n'

# footer
html_buffer += '<footer class="w3-container" style="padding:32px;background-color:blue">\n'
html_buffer += '<div class="w3-center w3-text-white">\n'
html_buffer += '<p style="color:lime"><strong>Cool Beans BV</strong></p>\n'
html_buffer += '<p>Haarlemmerweg 315D<br>1051 LG, Amsterdam<br>Nederland</p>\n'
html_buffer += '<p>+31 (0) 650281410</p>\n'
html_buffer += '</ul><a href="#" class="w3-button w3-padding w3-margin-bottom" style="background-color:blue;color:red"><i class="fa fa-arrow-up w3-margin-right"></i>Back to top</a>\n'
html_buffer += '</div>\n'
html_buffer += '</footer>\n'
html_buffer += '</html>\n'

# write buffer
f = open("index.html",'wt')
f.write(html_buffer)

import defaults as d
from pypandoc import convert_text as convert_text
from subprocess import check_output as shell
from ast import literal_eval as lit
import time

class Utilities(object):
	def __init__(self):
		"""Some utile builtins."""
		self.convert = lambda x: convert_text(x, "html", format="md")
		self.tag = lambda x: "<h3>"+x+"</h3>"
		self.sort = lambda x: sorted(x,
			key = lambda y: "".join(y.meta["Date"].split(".")[::-1]))[::-1]
		self.config = (#Name, Number of articles, URL
		("Dialectic", 2, "d.html"),
			("Issues", 1, "i.html"),
			("Letters", 1, "l.html"),
			("Review", 2, "r.html"),
			("Sciences and Mathematics", 2, "s.html"),
			("Editorial", 1, "e.html"))
		self.base = "www/"
		self.url = "https://librarian.cf/"
		self.categories = {x[0]: Type(*x) for x in self.config}
		self.tags, self.authors = {}, {}

class Type(object):
	"""A category of articles with the following attributes:
	- Place
	- Articles
	- Metadata, viz. number of articles and position on front page
	- Reduced set of metadata of articles based thereon."""

	def __init__(self, name, frontpage_number, url):
		"""__init__ function creates attributes mentioned above."""
		self.included = []
		self.place, self.name, self.fpn = url, name, frontpage_number

	def include(self, article):
		"""Include an article in a tag."""
		self.included.append(article)

	def figure(self):
		"""Writes figures."""
		self.figures = [a.h3 for a in u.sort(self.included)]
		self.box = self.figures[:self.fpn]

	def suggestions(self, article):
		"""Writes suggestions given article and category."""
		suggested = []
		remainder, counter, maximum = self.fpn, 0, len(self.included)
		while remainder and counter < maximum:
			attempt = self.included[counter]
			counter += 1
			if attempt not in article.suggested and attempt is not article:
				suggested.append(attempt)
				remainder -= 1
		self.suggested = "".join(["<h3><a class='nav' href='",
			u.url+self.place,"'>", self.name,"</a></h3>",
			*[x.h4 for x in suggested]]) \
			if len(suggested) else ""
		return self.suggested

	def output(self):
		"""Outupts topic pages."""
		figures = self.figures \
			+ ["<figure class='blank'></figure>"] \
			* (3-len(self.included)%3)
		split = "\n".join((
			"<section><aside class='fill'></aside>"+
			"\n".join(figures[x:x+3])+
			"<aside class='fill'></aside></section>"
			for x in range(0, len(self.included), 3)))
		with open(u.base+self.place, "w") as f:
			print("\n".join([d.topic[0],self.name,d.topic[1],split,d.topic[2]]),
				file = f)

class Article(object):
	"""An article with the following attributes:
	- Metadata:
		- Title eg. "The death of Chinese pluralism"
		- Author
		- Date
		- Category
		- Tags
	- The article itself."""

	def __init__(self, raw, number):
		"""__init__ function creates attributes mentioned above."""
		separated = raw.split("\n")
		self.place = "articles/" + number + "/" + number + ".html"
		self.meta, self.title = lit(separated[2]), separated[0]
		u.categories[self.meta["Category"]].include(self)
		author = self.meta["Author"]
		if author in u.authors.keys():
			u.authors[author].include(self)
		else:
			print("Creating author", author)
			u.authors[author] = Type(author, 0,
				"authors/"+author.lower().replace(" ", "-")+".html")
		tags = (self.meta["Category"],) + self.meta["Tags"]
		for tag in tags:
			if tag in u.tags.keys():
				u.tags[tag].include(self)
			else:
				print("Creating tag", tag)
				u.tags[tag] = Type(tag, 0,
					"tags/"+tag.lower().replace(" ", "-")+".html")
				u.tags[tag].include(self)
		self.h3 = "\n".join(["<figure>",
			"<a href="+u.url + self.place," class='nav'>",
			u.convert("".join(["##",self.title,
				" / <strong>",self.meta["Author"],"</strong>"]))+"</a>",
			"</figure>"])
		self.h4 = self.h3.replace("h3", "h4")
		self.authorship = "".join(["<a class='nav' href='",
			u.url,"authors/",
			self.meta["Author"].lower().replace(" ", "-")+".html",
			"'>",self.meta["Author"],"</a>"])
		try:
			if self.meta["Type"] == "Issue":
				self.body = "\n".join(separated[4:])
				print("Article", number, "is issue.")
			else:
				self.body = u.convert("\n".join(separated[4:]))
		except:
			self.body = u.convert("\n".join(separated[4:]))

	def output(self):
		"""output() function outputs page after merging attributes."""
		self.suggested = []
		for tag in self.meta["Tags"]:
			self.suggested.append(u.tags[tag].suggestions(self))
		self.suggested.append(u.authors[self.meta["Author"]].suggestions(self))
		self.suggested.append(u.categories[self.meta["Category"]].suggestions(self))
		try:
			if self.meta["Type"] == "Mathematics":
				start = d.math[0]
			elif self.meta["Type"] == "Issues":
				self.suggested = [""]
			else:
				start = d.base[0]
		except:
			start = d.base[0]
		self.html = "\n".join([
			start, self.title.translate(str.maketrans("", "", "*#_")),
			d.base[1], self.authorship, self.meta["Date"],
			d.base[2], u.convert(self.title), self.body,
			d.base[3], "\n".join(self.suggested),
			d.base[4]])
		with open(u.base + self.place, "w") as f:
			print(self.html, file = f)

class Bookshelf(object):
	"""
	A Bookshelf() is a website. It contains:
		- raw_files ie. the original MD files in each folder,
		- u, ie. a utilities object, holding:
			- methods:
				- convert (from MD to HTML)
				- tag (a string with '<h3>' and '</h3')
				- sort (some dates)
			- config
			- base of path for the site
			- url
			- categories
			- tags
			- authors
		- some other things which will be added hereto in the chronoplenty
	"""

	def __init__(self):
		self.start = time.time()
		print("Setting up.")
		count = int(shell('cd www/articles; ls -l | grep -c ^d', shell=True))
		global u
		u = Utilities()

		print("Opening and processing", count, "articles.")
		raw_files = [open(u.base+"articles/"+str(i)+
			"/"+str(i)+".md").read()
			for i in range(count)]
		print(u.url)
		articles = [Article(md, str(n)) for n, md in enumerate(raw_files)]

		self.raw_files, self.articles = raw_files, articles

	def generate(self):
		print("Generating topic pages.")
		for committee in [u.categories, u.authors, u.tags]:
			for working_group in committee.values():
				working_group.figure()
				working_group.output()

		print("Generating front page.")
		frontpage = "\n".join(["\n".join([d.front[n],
			"\n".join(u.categories[x[0]].box)])
			for n, x in enumerate(u.config)])+d.front[6]
		with open(u.base+"index.html", "w") as f:
			print(frontpage, file = f)

		print("Generating article pages.")
		for article in self.articles:
			article.output()

		print("Time:", round(time.time()-self.start, 1), "seconds.")

	def information(self):
		print("Information on this bookshelf.")
		for article in self.articles:
			print(article.title)

if __name__ == "__main__":
	librarian = Bookshelf()
	librarian.generate()
	librarian.information()

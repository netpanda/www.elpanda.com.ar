Title: Starting this blog!
Date: 2015-01-16 10:20
Category: Coding
Tags: Linux, Python, Web, Security

It has been a long time since I started my first blog (nixlife.com.ar). For a number of reasons, I never had the time to properly follow it, and keep it updated. 
But recently I changed jobs (Bye bye HP :P) and my spare time has increased dramatically jeje. So I promised myself that I will try to documment here all my thoughts, failures and successes that I have on my daily IT Security job. 

So.. the first thing that I needed to decide is.. what platform should I use?
Wordpress was the natural solution, but I didn't want to be constantly fighting against scanners, and script kiddies. So I made a decisition and went to an easier solution and I start digging in the world of static content generators. 

[Octopress](http://www.octopress.org)

![octopress](/images/octopress.jpg "Octopress")

Without doubt very easy to install and use. A derivative from [Jekyll](http://jekyllrb.com), it was my first choice, and I even installed and started writing, but then I got to this post: [Octopress 3.0 Is Coming](http://octopress.org/2015/01/15/octopress-3.0-is-coming/), and I thought, why starting using something that is going to change so much in the next release? and also.. I wasn't so confortable with Ruby.. so I start searching again the net. 

And then.. I got my answer...

[Pelican](http://blog.getpelican.com/)

![pelican](/images/pelican.png "Pelican")

Pelican is a Static Site Generator written in Python, it is great. Very simple, and fast. 
In order to install it, it is as simple as execute: 

	:::console
	sudo pip install pelican

If you don't have pip and you are using Mac OS X, simply install it with [HomeBrew](http://brew.sh/). 

After you install pelican. Go to the directory where you want to save your new blog and execute: 

	:::console
	pelican-quickstart

This will ask you some questions and create the necessary configuration packages and folders. 

Just go ahead and edit the pelicanconf.py on your favorite text editor and you are ready to write your first post. 
On the directory tree you will see a content folder. Just create a file named firs-post.md and start blogging. 


Some useful links:

+	[Pelican Docummentation](http://docs.getpelican.com/en/3.5.0/)
+	[Markdown Formatting Syntax basics](http://daringfireball.net/projects/markdown/basics)





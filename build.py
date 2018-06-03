filenames = "templates/top.html" + "content/index.html" + "templates/bottom.html" 
open("docs/index.html", "w+").write(filenames) 

filenames = "templates/top.html" + "content/blog.html" + "templates/bottom.html" 
open("docs/blog.html", "w+").write(filenames) 

filenames = "templates/top.html" + "content/projects.html" + "templates/bottom.html" 
open("docs/projects.html", "w+").write(filenames) 

filenames = "templates/top.html" + "content/contact.html" + "templates/bottom.html" 
open("docs/contact.html", "w+").write(filenames) 

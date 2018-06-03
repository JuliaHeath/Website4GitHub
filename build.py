a = open("templates/top.html").read()
b = open("content/index.html").read()
c = open("templates/bottom.html").read()

filenames1 = a + b + c

open("docs/index.html", "w+").write(filenames1) 







d = open("content/blog.html").read()

filenames2 = a + d + c

open("docs/blog.html", "w+").write(filenames2) 







e = open("content/projects.html").read()


filenames3 = a + e + c

open("docs/projects.html", "w+").write(filenames3) 






f = open("content/contact.html").read()


filenames4 = a + f + c

open("docs/contact.html", "w+").write(filenames4) 






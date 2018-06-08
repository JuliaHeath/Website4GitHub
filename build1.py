def main():
    templates_top_content_bottom = open("templates/top_content_bottom.html").read()
    content_index = open("content/index.html").read()
 

    home = templates_top_content_bottom + content_index

    open("docs/index.html", "w+").write(home) 

    
  
    content_blog = open("content/blog.html").read()

    blog = templates_top_content_bottom + content_blog

    open("docs/blog.html", "w+").write(blog) 
    
    

    content_projects = open("content/projects.html").read()

    projects = templates_top_content_bottom + content_projects

    open("docs/projects.html", "w+").write(projects) 



    content_contact = open("content/contact.html").read()

    contact = templates_top_content_bottomp + f + c

    open("docs/contact.html", "w+").write(filenames4) 
    
main()



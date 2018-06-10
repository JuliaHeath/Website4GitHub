pages = [

    {
        'content': 'content/index.html',
        'output_file': 'docs/index.html',
        'title' : 'Home',
    },
    {
        'content': 'content/blog.html',
        'output_file': 'docs/blog.html',
        'title' : 'Blog',
    },
    {
        'content': 'content/projects.html',
        'output_file': 'docs/projects.html',
        'ttile' : 'Projects',
    },
       {
        'content': 'content/contact.html',
        'output_file': 'docs/contact.html',
        'ttile' : 'Contact',
    },
]


def main():
    

    for page in pages:
        print(page['content'])
        contents_of_file = open(page['content']).read()
        print(contents_of_file)
        templates = open('templates/base.html').read()
        docs = templates.replace('{{content}}', contents_of_file)
        open(page['output_file'], 'w+').write(docs)
        
        
        
#    content_index = open("content/index.html").read()
# 

#    home = base + content_index

#    open("docs/index.html", "w+").write(home) 

#    
#  
#    content_blog = open("content/blog.html").read()

#    blog = base + content_blog

#    open("docs/blog.html", "w+").write(blog) 
#    
#    

#    content_projects = open("content/projects.html").read()

#    projects = base + content_projects

#    open("docs/projects.html", "w+").write(projects) 



#    content_contact = open("content/contact.html").read()

#    contact = base + content_contact

#    open("docs/contact.html", "w+").write(contact) 
    
main()



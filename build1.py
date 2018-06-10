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
        'title' : 'Projects',
    },
       {
        'content': 'content/contact.html',
        'output_file': 'docs/contact.html',
        'title' : 'Contact',
    },
]


def main():
    for page in pages:
       contents_of_file = open(page['content']).read()
       templates = open('templates/base.html').read()
       title_of_file = (page['title'])
       def title():
            docs = templates.replace('{{content}}', contents_of_file).replace('{{title}}', title_of_file)
            open(page['output_file'], 'w+').write(docs)
       title()   
main()



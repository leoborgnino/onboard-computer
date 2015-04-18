import web

urls = ('/','index')

class index:
        def GET(self):
           return "45.0  45.0"
        def __init__(self):
            app= web.application(urls,globals())
            app.run()



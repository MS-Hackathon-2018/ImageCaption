import service as s 
import image_service as ims
import tornado.ioloop
import tornado.web
import json
import platform
import tempfile
tempdir = '/tmp' if platform.system() == 'Darwin' else tempfile.gettempdir()

class BaseHandler(tornado.web.RequestHandler):
    def set_default_headers(self):
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "x-requested-with")
        self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS, DELETE')

    def options(self):
        self.set_status(204)
        self.finish()

class TranslateHandler(BaseHandler):
    def get(self, text, suite):
        r = s._translate(text, suite)
        print(r)
        self.write(r)

class ImageCaptionHandler(BaseHandler):
    def post(self):
        
        p = tempdir + '/tmp.jpg'
        data = self.request.body
        with open(p, 'wb') as fp:
            fp.write(data)
        ret = ims.image_caption(data)
        ret2 = ims.object_detection(p)
        print(ret, ret2)
        self.write(json.dumps(dict(c=ret, d=ret2)))
               

def make_app():
    return tornado.web.Application([
        (r"/translate/(?P<text>[^/]+)/(?P<suite>.*)", TranslateHandler),
        (r"/image-caption", ImageCaptionHandler),
        (r"/(.*)",tornado.web.StaticFileHandler, {"path": "../frontend/dist"},),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()

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
        self.write(r)

class ImageCaptionHandler(BaseHandler):
    def post(self, t=None):
        
        p = tempdir + '/tmp.jpg'
        data = self.request.body
        with open(p, 'wb') as fp:
            fp.write(data)

        if t == 'c':
            ret = ims.image_caption(p)
            self.write(json.dumps(dict(c=ret["caption"])))
        elif t == 'd':
            ret = ims.object_detection(p)
            self.write(json.dumps(dict(d=ret)))
        elif t == 'w':
            ret = ims.word_detection(p)
            self.write(json.dumps(dict(w=ret)))
        else:
            ret = ims.image_caption(p)
            ret2 = ims.object_detection(p)
            ret3 = ims.word_detection(p)
            self.write(json.dumps(dict(c=ret["caption"], d=ret2, w=ret3)))

def make_app():
    # prefix = r'/hackathon'
    prefix = r''
    return tornado.web.Application([
        (prefix + r"/translate/(?P<text>[^/]+)/(?P<suite>.*)", TranslateHandler),
        (prefix + r"/image-caption/(?P<t>.*)", ImageCaptionHandler),
        (prefix + r"/(.*)",tornado.web.StaticFileHandler, {"path": "../frontend/dist"},),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()

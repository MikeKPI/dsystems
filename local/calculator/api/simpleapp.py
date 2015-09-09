import json
import tornado.ioloop
import tornado.web


class MainHandler(tornado.web.RequestHandler):
    def prepare(self):
        # Incorporate request JSON into arguments dictionary.
        if self.request.body:
            try:
                print(self.request.body)
                json_data = json.loads(str(self.request.body, encoding='utf-8'))
                self.request.arguments.update(json_data)
            except ValueError:
                message = 'Unable to parse JSON.'
                self.send_error(400, message=message)   # Bad Request

    def post(self):
        try:
            answer = eval(self.request.arguments['equation'])
        except Exception:
            answer = 'Wrong format!'

        self.add_header('Access-Control-Allow-Origin', '*')
        print(answer)
        self.write(json.dumps({'answer': answer}))


application = tornado.web.Application([
    (r"/result", MainHandler),
], debug=True)

if __name__ == "__main__":
    application.listen(5000)
    tornado.ioloop.IOLoop.current().start()

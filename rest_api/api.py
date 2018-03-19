import falcon

app = falcon.API()


class Hello(object):
    def on_get(self, req, resp):
        """Handles GET requests"""
        resp.status = falcon.HTTP_200  # This is the default status
        resp.body = 'Hello World2!'


hello_resource = Hello()
app.add_route('/hello', hello_resource)

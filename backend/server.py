import pyjsonrpc

SERVER_HOST = 'localhost'
SERVER_PORT = 4040

class RequestHandler(pyjsonrpc.HttpRequestHandler):
    '''Test method'''
    @pyjsonrpc.rpcmethod
    def add(self,a,b):
        print 'add gets called with %d and %d' %(a,b)
        return a + b

    @pyjsonrpc.rpcmethod
    def searchArea(self, query):
        if query.isdigit():
            pass
            #TODO search in DB
        else:
            city = query.split(',')[0].strip()
            state = query.split(',')[1].strip()
            #TODO search in DB
        return ["Houser_1","Xondo_2"]

http_server = pyjsonrpc.ThreadingHttpServer(
        server_address =(SERVER_HOST,SERVER_PORT),
        RequestHandlerClass = RequestHandler)

print 'starting HTTP server ...'
print 'Listening on %s:%d' %(SERVER_HOST,SERVER_PORT)

http_server.serve_forever()

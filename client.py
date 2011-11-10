#!/usr/bin/env python

if __name__ == '__main__':
    from twisted.web.xmlrpc import Proxy
    from twisted.internet import reactor

    def printValue(value):
        print repr(value)
        reactor.stop()

    def printError(error):
        print 'error', error
        reactor.stop()

    proxy = Proxy('https://%s:%s@localhost:9870' % ('myfancyusername', 'ohmygod'))
    proxy.callRemote('mult', 2, 3).addCallbacks(printValue, printError)
    reactor.run()

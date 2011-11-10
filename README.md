What I needed to do to get this to work
---------------------------------------

* Install Twisted
* Install Zope Interfaces
* Install pyOpenSSL
* Install web2 from Twisted: (either from svn or for the Web2 package)
	svn co svn://svn.twistedmatrix.com/svn/Twisted/trunk Twisted
* Move web2 into twisted
* Make salted hash password (salt is the last 2 characters of the password)
	 from crypt import crypt
	 password = 'mypass'
	 crypt(password, password[-2:]) #(use the last two characters as the salt)
* Add username/password to httpspass.conf
* Create a Twisted Client
    from twisted.web.xmlrpc import Proxy
    from twisted.internet import reactor

    def printValue(value):
        print repr(value)
        reactor.stop()

    def printError(error):
        print 'error', error
        reactor.stop()

    proxy = Proxy('https://%s:%s@localhost:9870' % ('myfancyusername', 'ohmygod'))
    proxy.callRemote('echo', 'hello, im echoing this').addCallbacks(printValue, printError)
    reactor.run()
* Start the server:
	twistd -y xmlrpc_app.py
* Test the client:
	python client.py

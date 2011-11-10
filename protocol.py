from twisted.web2 import xmlrpc


# this is the main class which contains the xmlrpc_ functions we need
class XMLRPCProtocol(xmlrpc.XMLRPC):
  
  addSlash = True
  
  def xmlrpc_bind(self, request):
    return parse("test.conf")
  
  def xmlrpc_echo(self, request, x):
    """Return all passed args."""
    return x

  def xmlrpc_mult(self, request, x, y):
    """Return all passed args."""
    return x*y

  #add a new zone, reload the configuration
  def addZone(self, request, name):
    print 'adding new zone'
    
  def updateZone(self, request, name):
    print 'updating existing zone'
    
    
  def setTTL(self, request, name):
    print 'test'
    

import sys
sys.path.append("/path/to/app") 

import xmlrpcserver
from twisted.application import service, strports

application = service.Application("XMLRPCServer")
x = xmlrpcserver.XMLRPCService( )
XMLRPCService = x.start( )
XMLRPCService.setServiceParent(application)

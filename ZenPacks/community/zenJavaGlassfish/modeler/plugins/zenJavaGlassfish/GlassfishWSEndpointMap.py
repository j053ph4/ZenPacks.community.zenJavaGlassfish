from ZenPacks.community.zenJavaApp.lib.CommonMBeanMap import *
from ZenPacks.community.zenJavaGlassfish.Definition import *

__doc__ = """GlassfishWSEndpointMap

GlassfishWSEndpointMap detects Glassfish WS Endpoints on a per-JVM basis.

This version adds a relation to associated ipservice and javaapp components.

"""

class GlassfishWSEndpointMap(CommonMBeanMap):
    """Map JMX Client output table to model."""
    
    constr = Construct(GlassfishWSEndpointDefinition)
    relname = constr.relname
    modname = constr.zenpackComponentModule
    baseid = constr.baseid
    
    searchMBean = 'amx:pp=/mon/server-mon[server],type=WSEndpoint,name=*'
    
    def parseAddress(self, address):
        protocol, url = address.split('//')
        parts = url.split('/')
        host,port = parts[0].split(':')
        url = '/'.join(parts[1:])
        return {
                #'wsHost': host,
                'wsPort': port,
                'wsUrl': '/%s' % url
                }
    
    def postprocess(self, result, om, log):
        ''''''
        jmx = self.scan.portdict[result['port']]
        self.scan.proxy.setJMX(jmx)
        output = self.scan.proxy.getBeanAttributeValues(result['fullpath'], ['wsdlEndpointAddress'])
        address = str(output['wsdlEndpointAddress'])
        om.wsdlEndpointAddress = address
        if len(address) == 0: 
            om.monitor = False
        else:
            #try: 
            log.debug('address: %s' % address)
            addr = self.parseAddress(address)
            log.debug('addr: %s' % addr)
            om.wsPort = addr['wsPort']
            om.wsUrl = addr['wsUrl']
            #except:  pass
        om.wsHost = self.device.manageIp
        return om



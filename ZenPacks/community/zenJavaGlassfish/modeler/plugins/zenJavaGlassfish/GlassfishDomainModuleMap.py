from ZenPacks.community.zenJavaApp.lib.CommonMBeanMap import *
from ZenPacks.community.zenJavaGlassfish.Definition import *

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
    
    def process(self, device, results, log):
        log.info("got %s results" % len(results))
        #self.scan =  None
        rm = self.relMap()
        for result in results:
            enabled = result['enabled']
            result.pop('enabled')
            try:
                result['wsdlEndpointAddress'] = self.scan.getBeanAttributeValues(port=result['port'], 
                                                                        mbean=result['fullpath'], 
                                                                        attributes=['wsdlEndpointAddress'], 
                                                                        protocol=result['protocol'])['wsdlEndpointAddress']
                result.update(self.parseAddress(result['wsdlEndpointAddress']))
            except:
                pass
            om = self.objectMap(result)
            om.wsHost = device.manageIp
            om.setJavaapp = ''
            om.setIpservice = ''
            om.monitor = enabled 
            rm.append(om)
            log.debug(om)
        return rm

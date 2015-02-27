from ZenPacks.community.zenJavaApp.lib.CommonMBeanMap import *
from ZenPacks.community.zenJavaGlassfish.Definition import *

class GlassfishJ2EEModuleMap(CommonMBeanMap):
    """Map JMX Client output table to model."""
    
    constr = Construct(GlassfishJ2EEModuleDefinition)
    relname = constr.relname
    modname = constr.zenpackComponentModule
    baseid = constr.baseid
    
    searchMBean = 'amx:pp=/J2EEDomain/J2EEServer[*]/J2EEApplication[*],type=*,name=*,j2eeType=*,J2EEServer=*,J2EEApplication=*'
    
    def isEnabled(self, port, mbean, protocol, log):
        '''decide whether or not this should be monitored'''
        result = self.scan.getBeanAttributeValues(port=port, mbean=mbean, attributes=['state'], protocol=protocol)
        if 'state' in result.keys(): return True
        return False
    
    def process(self, device, results, log):
        log.info("The plugin %s returned %s results." % (self.name(), len(results)))
        rm = self.relMap()
        for result in results:
            result.pop('enabled')
            om = self.objectMap(result)
            om.setJavaapp = ''
            om.setIpservice = ''
            om.monitor = self.isEnabled(result['port'], result['fullpath'], result['protocol'], log) 
            rm.append(om)
            log.debug(om)
        return rm

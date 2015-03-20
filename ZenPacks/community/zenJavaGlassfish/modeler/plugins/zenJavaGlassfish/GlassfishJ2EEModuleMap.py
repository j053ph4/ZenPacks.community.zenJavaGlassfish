from ZenPacks.community.zenJavaApp.lib.CommonMBeanMap import *
from ZenPacks.community.zenJavaGlassfish.Definition import *

__doc__ = """GlassfishJ2EEModuleMap

GlassfishJ2EEModuleMap detects Glassfish J2EE Modules on a per-JVM basis.

This version adds a relation to associated ipservice and javaapp components.

"""

class GlassfishJ2EEModuleMap(CommonMBeanMap):
    """Map JMX Client output table to model."""
    
    constr = Construct(GlassfishJ2EEModuleDefinition)
    relname = constr.relname
    modname = constr.zenpackComponentModule
    baseid = constr.baseid
    
    searchMBean = 'amx:pp=/J2EEDomain/J2EEServer[*]/J2EEApplication[*],type=*,name=*,j2eeType=*,J2EEServer=*,J2EEApplication=*'
    
    def isEnabled(self, port, mbean, log):
        '''decide whether or not this should be monitored'''
        jmx = self.scan.portdict[port]
        self.scan.proxy.setJMX(jmx)
        result = self.scan.proxy.getBeanAttributeValues(mbean, ['state'])
        if result is None: return False
        if 'state' in result.keys(): return True
        return False
    
    def postprocess(self, result, om, log):
        ''''''
        om.monitor = self.isEnabled(result['port'], result['fullpath'], log)
        return om


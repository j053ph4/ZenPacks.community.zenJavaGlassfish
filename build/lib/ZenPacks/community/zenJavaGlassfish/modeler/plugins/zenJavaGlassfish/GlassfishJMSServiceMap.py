from ZenPacks.community.zenJavaApp.lib.CommonMBeanMap import *
from ZenPacks.community.zenJavaGlassfish.Definition import *

class GlassfishJMSServiceMap(CommonMBeanMap):
    """Map JMX Client output table to model."""
    
    constr = Construct(GlassfishJMSServiceDefinition)
    relname = constr.relname
    modname = constr.zenpackComponentModule
    baseid = constr.baseid
    
    searchMBean = 'com.sun.messaging.jms.server:type=Service,subtype=Monitor,name=*'


from ZenPacks.community.zenJavaApp.lib.CommonMBeanMap import *
from ZenPacks.community.zenJavaGlassfish.Definition import *

class GlassfishJMSConsumerManagerMap(CommonMBeanMap):
    """Map JMX Client output table to model."""
    
    constr = Construct(GlassfishJMSConsumerManagerDefinition)
    relname = constr.relname
    modname = constr.zenpackComponentModule
    baseid = constr.baseid
    
    searchMBean = 'com.sun.messaging.jms.server:type=ConsumerManager,subtype=Monitor'


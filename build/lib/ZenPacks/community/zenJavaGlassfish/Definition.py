from ZenPacks.community.ConstructionKit.BasicDefinition import *
from ZenPacks.community.ConstructionKit.Construct import *
from ZenPacks.community.zenJavaApp.Definition import getMBeanDef, addMBeanRelations


ROOT = "ZenPacks.community"
BASE = "zenJavaGlassfish"
VERSION = Version(1, 0, 0)


########### EJB MODULE ###########




def getMapValue(ob, datapoint, map):
    ''' attempt to map number to data dict'''
    try: return map[int(ob.getRRDValue(datapoint))]
    except:
        if ob.monitor is False:  return map[3]
        else: return map[-1]

def getSensorState(ob): 
    '''maps RRD values to data dictionary'''
    return ob.getMapValue('state_state', ob.sensorStatusMap)


'''The states, ordered from most to least functional are: running (4), starting (5), other (1), stopping (6), stopped (3), failed (2).'''


MODDATA = getMBeanDef(VERSION, ROOT, BASE, 'GlassfishJ2EEModule','Glassfish J2EE Module', 'Glassfish J2EE Modules')
MODDATA['componentData']['properties']['j2eeType'] = addProperty('J2EE Type',optional=False)
MODDATA['componentData']['properties']['getSensorState'] = getReferredMethod('Current State', 'getSensorState')
MODDATA['componentAttributes'] = {'sensorStatusMap':  { -1: 'UNKNOWN', 1: 'OTHER', 2: 'FAILED', 3: 'STOPPED', 4: 'RUNNING', 5: 'STARTING', 6: 'STOPPING',} }
MODDATA['componentMethods'] = [getMapValue, getSensorState]

GlassfishJ2EEModuleDefinition = type('GlassfishJ2EEModuleDefinition', (BasicDefinition,), MODDATA)
addMBeanRelations(GlassfishJ2EEModuleDefinition)


########### DOMAIN APP MBEANS ###########
GlassfishDomainModuleDefinition = type('GlassfishDomainModuleDefinition', (BasicDefinition,), 
                                       getMBeanDef(VERSION, ROOT, BASE, 'GlassfishDomainModule','Glassfish Domain Module', 'Glassfish Domain Modules'))
addMBeanRelations(GlassfishDomainModuleDefinition)


########### WSEndpoint MBEANS ###########

WSDATA = getMBeanDef(VERSION, ROOT, BASE, 'GlassfishWSEndpoint','Glassfish WS Endpoint', 'Glassfish WS Endpoints')
WSDATA['componentData']['properties']['wsdlEndpointAddress'] = addProperty('Endpoint Address',optional=False)
WSDATA['componentData']['properties']['wsHost'] = addProperty('WS Host')
WSDATA['componentData']['properties']['wsPort'] = addProperty('WS Port')
WSDATA['componentData']['properties']['wsUrl'] = addProperty('WS URL')

GlassfishWSEndpointDefinition = type('GlassfishWSEndpointDefinition', (BasicDefinition,), WSDATA)
addMBeanRelations(GlassfishWSEndpointDefinition)


########### GLASSFISH JMS ConnectionManager ###########
GlassfishJMSConnectionManagerDefinition = type('GlassfishJMSConnectionManagerDefinition', (BasicDefinition,), 
                                       getMBeanDef(VERSION, ROOT, BASE, 
                                                   'GlassfishJMSConnectionManager',
                                                   'Glassfish JMS ConnectionManager', 
                                                   'Glassfish JMS ConnectionManagers'
                                                   )
                                               )
addMBeanRelations(GlassfishJMSConnectionManagerDefinition)

########### GLASSFISH JMS ConsumerManager ###########
GlassfishJMSConsumerManagerDefinition = type('GlassfishJMSConsumerManagerDefinition', (BasicDefinition,), 
                                       getMBeanDef(VERSION, ROOT, BASE, 
                                                   'GlassfishJMSConsumerManager',
                                                   'Glassfish JMS ConsumerManager', 
                                                   'Glassfish JMS ConsumerManagers'
                                                   )
                                               )
addMBeanRelations(GlassfishJMSConsumerManagerDefinition)

########### GLASSFISH JMS DestinationManager ###########

GlassfishJMSDestinationManagerDefinition = type('GlassfishJMSDestinationManagerDefinition', (BasicDefinition,), 
                                       getMBeanDef(VERSION, ROOT, BASE, 
                                                   'GlassfishJMSDestinationManager',
                                                   'Glassfish JMS DestinationManager', 
                                                   'Glassfish JMS DestinationManagers'
                                                   )
                                               )
addMBeanRelations(GlassfishJMSDestinationManagerDefinition)



########### GLASSFISH JMS ServiceManager ###########
GlassfishJMSServiceManagerDefinition = type('GlassfishJMSServiceManagerDefinition', (BasicDefinition,), 
                                       getMBeanDef(VERSION, ROOT, BASE, 
                                                   'GlassfishJMSServiceManager',
                                                   'Glassfish JMS ServiceManager', 
                                                   'Glassfish JMS ServiceManagers'
                                                   )
                                               )
addMBeanRelations(GlassfishJMSServiceManagerDefinition)

########### GLASSFISH JMS TransactionManager ###########
GlassfishJMSTransactionManagerDefinition = type('GlassfishJMSTransactionManagerDefinition', (BasicDefinition,), 
                                       getMBeanDef(VERSION, ROOT, BASE, 
                                                   'GlassfishJMSTransactionManager',
                                                   'Glassfish JMS TransactionManager', 
                                                   'Glassfish JMS TransactionManagers'
                                                   )
                                               )
addMBeanRelations(GlassfishJMSTransactionManagerDefinition)


########### GLASSFISH JMS Destination ###########

def getSensorState(ob): 
    '''maps RRD values to data dictionary'''
    return ob.getMapValue('State_State', ob.sensorStatusMap)

DESTDATA = getMBeanDef(VERSION, ROOT, BASE, 'GlassfishJMSDestination', 'Glassfish JMS Destination', 'Glassfish JMS Destinations')
DESTDATA['componentData']['properties']['getSensorState'] = getReferredMethod('Current State', 'getSensorState')
DESTDATA['componentAttributes'] = {'sensorStatusMap':  { -1: 'UNKNOWN', 0: 'RUNNING', 1: 'CONSUMERS_PAUSED', 2: 'PRODUCERS_PAUSED', 3: 'PAUSED'} }
DESTDATA['componentMethods'] = [getMapValue, getSensorState]

GlassfishJMSDestinationDefinition = type('GlassfishJMSDestinationDefinition', (BasicDefinition,), DESTDATA)
addMBeanRelations(GlassfishJMSDestinationDefinition)

########### GLASSFISH JMS Service ###########

SVCDATA = getMBeanDef(VERSION, ROOT, BASE, 'GlassfishJMSService', 'Glassfish JMS Service', 'Glassfish JMS Services')
SVCDATA['componentData']['properties']['getSensorState'] = getReferredMethod('Current State', 'getSensorState')
SVCDATA['componentAttributes'] = {'sensorStatusMap':  { -1: 'UNKNOWN', 0: 'RUNNING', 1: 'PAUSED', 2: 'QUIESCED'}}
SVCDATA['componentMethods'] = [getMapValue, getSensorState]

GlassfishJMSServiceDefinition = type('GlassfishJMSServiceDefinition', (BasicDefinition,), SVCDATA)
addMBeanRelations(GlassfishJMSServiceDefinition)




(function(){
    var ZC = Ext.ns('Zenoss.component');

    function render_link(ob) {
        if (ob && ob.uid) {
            return Zenoss.render.link(ob.uid);
        } else {
            return ob;
        }
    }
    
    function pass_link(ob){ 
        return ob; 
    }
    
    ZC.GlassfishWSEndpointPanel = Ext.extend(ZC.ComponentGridPanel, {
        constructor: function(config) {
            config = Ext.applyIf(config||{}, {
                componentType: 'GlassfishWSEndpoint',
                autoExpandColumn: 'name', 
                fields:                 [
                    {
                        "name": "uid"
                    }, 
                    {
                        "name": "severity"
                    }, 
                    {
                        "name": "status"
                    }, 
                    {
                        "name": "name"
                    }, 
                    {
                        "name": "getIpserviceLink"
                    }, 
                    {
                        "name": "getJavaappLink"
                    }, 
                    {
                        "name": "mbean"
                    }, 
                    {
                        "name": "wsdlEndpointAddress"
                    }, 
                    {
                        "name": "usesMonitorAttribute"
                    }, 
                    {
                        "name": "monitor"
                    }, 
                    {
                        "name": "monitored"
                    }, 
                    {
                        "name": "locking"
                    }
                ]
,
                columns:                [
                    {
                        "sortable": "true", 
                        "width": 50, 
                        "header": "Events", 
                        "renderer": Zenoss.render.severity, 
                        "id": "severity", 
                        "dataIndex": "severity"
                    }, 
                    {
                        "header": "Name", 
                        "width": 70, 
                        "sortable": "true", 
                        "id": "name", 
                        "dataIndex": "name"
                    }, 
                    {
                        "sortable": "true", 
                        "width": 120, 
                        "header": "IP Service", 
                        "renderer": "pass_link", 
                        "id": "getIpserviceLink", 
                        "dataIndex": "getIpserviceLink"
                    }, 
                    {
                        "sortable": "true", 
                        "width": 120, 
                        "header": "Java App", 
                        "renderer": "pass_link", 
                        "id": "getJavaappLink", 
                        "dataIndex": "getJavaappLink"
                    }, 
                    {
                        "sortable": "true", 
                        "width": 120, 
                        "header": "MBean", 
                        "renderer": "pass_link", 
                        "id": "mbean", 
                        "dataIndex": "mbean"
                    }, 
                    {
                        "sortable": "true", 
                        "width": 120, 
                        "header": "Endpoint Address", 
                        "renderer": "pass_link", 
                        "id": "wsdlEndpointAddress", 
                        "dataIndex": "wsdlEndpointAddress"
                    }, 
                    {
                        "header": "Monitored", 
                        "width": 65, 
                        "sortable": "true", 
                        "id": "monitored", 
                        "dataIndex": "monitored"
                    }, 
                    {
                        "sortable": "true", 
                        "width": 65, 
                        "header": "Locking", 
                        "renderer": Zenoss.render.locking_icons, 
                        "id": "locking", 
                        "dataIndex": "locking"
                    }
                ]

            });
            ZC.GlassfishWSEndpointPanel.superclass.constructor.call(this, config);
        }
    });
    
    Ext.reg('GlassfishWSEndpointPanel', ZC.GlassfishWSEndpointPanel);
    ZC.registerName('GlassfishWSEndpoint', _t('Glassfish WS Endpoint'), _t('Glassfish WS Endpoints'));
    
    })();


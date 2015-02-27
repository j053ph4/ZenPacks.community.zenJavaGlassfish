
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
    
    ZC.GlassfishJ2EEModulePanel = Ext.extend(ZC.ComponentGridPanel, {
        constructor: function(config) {
            config = Ext.applyIf(config||{}, {
                componentType: 'GlassfishJ2EEModule',
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
                        "name": "getSensorState"
                    }, 
                    {
                        "name": "j2eeType"
                    }, 
                    {
                        "name": "mbean"
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
                        "header": "Current State", 
                        "renderer": "pass_link", 
                        "id": "getSensorState", 
                        "dataIndex": "getSensorState"
                    }, 
                    {
                        "sortable": "true", 
                        "width": 120, 
                        "header": "J2EE Type", 
                        "renderer": "pass_link", 
                        "id": "j2eeType", 
                        "dataIndex": "j2eeType"
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
            ZC.GlassfishJ2EEModulePanel.superclass.constructor.call(this, config);
        }
    });
    
    Ext.reg('GlassfishJ2EEModulePanel', ZC.GlassfishJ2EEModulePanel);
    ZC.registerName('GlassfishJ2EEModule', _t('Glassfish J2EE Module'), _t('Glassfish J2EE Modules'));
    
    })();


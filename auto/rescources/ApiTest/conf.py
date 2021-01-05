# -*- coding:utf-8 -*-

__author__ = "YuKwengRu"

from auto.rescources.ApiTest.conf_task_code import unit_dict

# hr, token = http_connector

agent_login = {
    "method": "POST",
    "uri": "/accountLogin/gen/unit/agent",
    "params":{
        "userType":"agent", "account":"0000", "loginMode":"job", "password":"123456", "unitId":"76"
    }
}

doctor_login = {
    "method": "POST",
    "uri": "/accountLogin/gen/unit/doctor",
    "params": {
        "userType":"doctor", "account":"0001", "loginMode":"job", "password":"123456", "unitId":"76"
    }
}

driver_login = {
    "method": "POST",
    "uri": "/accountLogin/gen/unit/driver",
    "params":{
        "userType":"driver", "account":"0002", "loginMode":"job", "password":"123456", "unitId":"76"
    }
}

to_work = {
    "method": "GET",
    "uri": "/attendance/gen/toWork?carId=48",
}

off_work = {
    "method": "GET",
    "uri": "/attendance/gen/offWork",
}

is_work = {
    "method": "GET",
    "uri": "/attendance/gen/isWork",
}
create_task_help = {
    "method": "POST",
    "uri": "/help/agent/create",
    "params": {
        "phone": "11111111111", "remark": "auto_hub_jsfj"
    }
}

assign = {
    "method": "POST",
    "uri": "/carOut/agent/assign"
}

accept = {
    "method": "GET",
    "uri": "/carOut/gen/accept?ambId=48"
}

departure = {
    "method": "GET",
    "uri": "/carOut/gen/departure?ambId=48"
}

arriveSite = {
    "method": "GET",
    "uri": "/carOut/gen/arriveSite?ambId=48"
}

returnHospital = {
    "method": "GET",
    "uri": "/carOut/gen/return?ambId=48"
}

arriveHospital ={
    "method": "GET",
    "uri": "/carOut/gen/arriveHospital?ambId=48"
}

pending = {
    "method": "GET",
    "uri": "/carOut/gen/pending?status=1"
}

onTask_my = {
    "method": "GET",
    "uri": "/help/agent/onTask",
    "params": {
        "type": 1
    }
}

complete = {
    "method": "POST",
    "uri": "/dispatch/agent/complete"    
}
cancel = {

}
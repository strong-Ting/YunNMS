
from . import models

field = {
    "name": {
        "id": "name",
        "name": "name",
        "label": "input",
        "elements": {
            "class": "form-control",
            "type": "text",
            "placeholder": "Name"
        }
    },
    "email": {
        "id": "email",
        "name": "email",
        "label": "input",
        "elements": {
            "class": "form-control",
            "type": "text",
            "placeholder": "Email"
        }
    },
    "account": {
        "id": "account",
        "name": "account",
        "label": "input",
        "elements": {
           "class": "form-control",
           "type": "text",
           "placeholder": "Account"
        }
    },
    "status": {
        "id": "status",
        "name": "status",
        "label": "select",
        "value": [
            { 
                "label": "option",
                "value": "Status",
                "elements": {
                    "value": "",
                    "selected": "selected"
                }
            },
            { 
                "label": "option",
                "value": "un-authenticated",
                "elements": { "value": "unauthenticated" }
            },
            {
                "label": "option",
                "value": "authenticated",
                "elements": { "value": "authenticated" }
            }
        ],
        "elements": {
            "class": "form-control"
        }
    },
    "text": {
        "id": "text",
        "name": "text",
        "label": "textarea",
        "elements": {
            "style": "width: 100%; height: *;",
            "rows": "15"
        }
    }
}

form = {
    "AddUserForm": {
        "method": "POST",
        "action": "user/A_Add/",
        "fields":  ["name", "email", "account"]
    },
    "ModUserForm": {
        "method": "POST",
        "action": "user/A_Modify/",
        "fields": ["name", "email", "status"]
    },
    "DelUserForm": {
        "method": "POST",
        "action": "user/A_Delete/",
        "fields": ["account"]
    },
    "BatchImportForm": {
        "method": "POST",
        "action": "user/A_BatchImport/",
        "fields": ["text"]
    }
}


def UserForm(data, formName, act):
    newDoc = {};
    for each in form[formName]['fields']:
        if each in models.action:
            action = models.action[each][act]
            if action == 'unique' and models.not_duplicate({ each: data[each]}, True if act == 'U' else False) == False:
                return {'result': None}
        newDoc[each] = data[each]
    return newDoc

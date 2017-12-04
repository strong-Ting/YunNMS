from flask import render_template,request,jsonify,redirect
from app import app
import json, traceback
from bson import ObjectId
from bson.json_util import dumps
from . import utils
from . import models as userModel
from . import forms as userForm
import os
from copy import deepcopy

#@app.route('/<regex("[0-9a-f]{1}"):test>')
@app.template_filter('underscore')
def underscore(value,arg): # date = datetime object.
    try:
        return value['_'+str(arg)]
    except:
        return 'Error/Backend/templatetags/templang/underscore'     

@app.template_filter('get')
def get(value, arg):
    try:
        _value = deepcopy(value)
        del _value[arg]
        return _value
    except:
        return 'Error/Backend/templatetabs/templang/remove'

@app.template_filter('dictGet')
def dictGet(value, arg):
    try:
        return value[str(arg)] if arg in value else 'None'
    except:
        return 'Error/Backend/templatetags/templang/dictGet'

@app.template_filter('genDOM')
def genDOM(value, arg):
    config = value[arg] if arg != None else value
    DOM = ('<' + config['label'] if 'label' in config else '')
    DOM += (' id="' + config['id'] + '"') if 'id' in config else ''
    DOM += (' name="' + config['name'] + '"') if 'name' in config else ''
    if 'elements' in config:
        for key, val in config['elements'].items():
            DOM += (' ' + key + '="' + val + '"')
    DOM += '>' if 'label' in config else ''
    if 'value' in config and type(config['value']) == list:
        for each in config['value']:
            DOM += genDOM(each,  None)
    else:
        DOM += config['value'] if 'value' in config else ''
    DOM += ('</' + config['label'] + '>') if 'label' in config else ''
    return DOM

@app.route('/user/',defaults={'action': None})
@app.route('/user/<action>/', methods=['POST','GET'])
def dashboard(action=None):
    try:
        users = userModel.find_all(None)
        print(action)
        if request.method == 'POST':
            if action == 'Add':
                result = userForm.UserForm(request.form, 'AddUserForm', 'C')
                if 'result' in result and result['result'] == None:
                    print("{'result': 'Data error'}")
                    return jsonify({'result': 'Data error'}) 
                else:
                    result['status'] = 'un-authenticated'
                    userModel.insert(result)
            elif action == 'ConfirmDelete':
                for key, value in request.form.items():
                    if 'input_id_' in key:
                        userModel.remove({'_id': ObjectId(value)})
            elif action == 'Modify':
                result = userForm.UserForm(request.form, 'ModUserForm', 'U')
                if 'result' in result and reault['result'] == None:
                    return jsonify({'result': 'Data error'}) 
                else:
                    for key, value in request.form.items():
                        if 'input_id_' in key:
                            userModel.update({'_id': ObjectId(value)}, result)
            elif action == 'BatchImport':
                docJson = request.form.get('text').replace('\'', '"')
                if utils.is_json(docJson):
                    userModel.insert_many(json.loads(docJson))
                else:
                    return jsonify({'result': 'Invalid Json data.'})
                pass
            return redirect('user/')
        else:
       #     collExtSchema = userApps.collExtSchema
            form = userForm.form
            field = userForm.field
            
            if action == 'ExportJson':
          #      downloadResponse = HttpResponse(dumps(users), content_type='application/json')
           #     downloadResponse['Content-Disposition'] = 'attachment; filename=export.json'
           #     return downloadResponse
                return jsonify(dumps(users))
        return render_template('Backend/User/dashboard.html', **locals())
    except:
        traceReport = traceback.format_exc()
        return render_template('Backend/Pages/traceback.html', **locals())

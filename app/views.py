from flask import render_template,request,jsonify,redirect
from app import app

#@app.route('/<regex("[0-9a-f]{1}"):test>')

import json, traceback
from bson import ObjectId
from bson.json_util import dumps


from . import utils

#from . import apps as userApps
from . import models as userModel
from . import forms as userForm

# Create your views here.
@app.route('/user/',defaults={'action': None})
@app.route('/user/<action>', methods=['POST','GET'])
def test(action=None):
    users = {'status':{'count':5}}
    return render_template('Backend/User/dashboard.html', **locals())


"""
def dashboard(action=None):
    try:
        users = userModel.find_all(None)
        if request.method == 'POST':
            if action == 'Add':
                result = userForm.UserForm(request.POST, 'AddUserForm', 'C')
                if 'result' in result and result['result'] == None:
                    return jsonify({'result': 'Data error'}) 
                else:
                    result['status'] = 'un-authenticated'
                    userModel.insert(result)
            elif action == 'ConfirmDelete':
                for key, value in request.POST.items():
                    if 'input_id_' in key:
                        userModel.remove({'_id': ObjectId(value)})
            elif action == 'Modify':
                result = userForm.UserForm(request.POST, 'ModUserForm', 'U')
                if 'result' in result and reault['result'] == None:
                    return jsonify({'result': 'Data error'}) 
                else:
                    for key, value in request.POST.items():
                        if 'input_id_' in key:
                            userModel.update({'_id': ObjectId(value)}, result)
            elif action == 'BatchImport':
                docJson = request.POST.get('text').replace('\'', '"')
                if utils.is_json(docJson):
                    userModel.insert_many(json.loads(docJson))
                else:
                    return jsonify({'result': 'Invalid Json data.'})
                pass
            return redirect('/backend/user/')
        else:
       #     collExtSchema = userApps.collExtSchema
            form = userForm.form
            field = userForm.field
            '''
            if action == 'ExportJson':
                downloadResponse = HttpResponse(dumps(users), content_type='application/json')
                downloadResponse['Content-Disposition'] = 'attachment; filename=export.json'
                return downloadResponse
            '''
        return render_template('Backend/User/dashboard.html', **locals())
    except:
        traceReport = traceback.format_exc()
        return render_template('Backend/Pages/traceback.html', **locals())
"""

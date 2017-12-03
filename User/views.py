import json, traceback
from bson import ObjectId
from bson.json_util import dumps
from django.shortcuts import render, redirect, HttpResponse, HttpResponseRedirect
from django.http import JsonResponse

from Backend import utils

from . import apps as userApps
from . import models as userModel
from . import forms as userForm

# Create your views here.
def dashboard(request, action=None, id=None):
    try:
        users = userModel.find_all(None)
        if request.method == 'POST':
            if action == 'Add':
                result = userForm.UserForm(request.POST, 'AddUserForm', 'C')
                if 'result' in result and result['result'] == None:
                    return JsonResponse({'result': 'Data error'}) 
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
                    return HttpResponse({'result': 'Data error'}) 
                else:
                    for key, value in request.POST.items():
                        if 'input_id_' in key:
                            userModel.update({'_id': ObjectId(value)}, result)
            elif action == 'BatchImport':
                docJson = request.POST.get('text').replace('\'', '"')
                if utils.is_json(docJson):
                    userModel.insert_many(json.loads(docJson))
                else:
                    return JsonResponse({'result': 'Invalid Json data.'})
                pass
            return redirect('/backend/user/')
        else:
            collExtSchema = userApps.collExtSchema
            form = userForm.form
            field = userForm.field
            if action == 'ExportJson':
                downloadResponse = HttpResponse(dumps(users), content_type='application/json')
                downloadResponse['Content-Disposition'] = 'attachment; filename=export.json'
                return downloadResponse
        return render(request, 'Backend/User/dashboard.html', locals())
    except:
        traceReport = traceback.format_exc()
        return render(request, 'Backend/Pages/traceback.html', locals())

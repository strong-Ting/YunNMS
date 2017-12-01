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
                addUserForm = userForm.AddUserForm(request.POST)
                if addUserForm.is_valid():
                    document = addUserForm.cleaned_data
                    document['status'] = 'unauthenticated'
                    del document['passPreset']
                    if userModel.not_duplicate({'account': document['account']}) == False:
                        return HttpResponse({'result': 'Account duplicate.'})
                    elif userModel.not_duplicate({'email': document['email']}) == False:
                        return HttpResponse({'result': 'Email duplicated.'})
                    else:
                        userModel.insert(document)
                else:
                    return JsonResponse({'result' : 'Form invalid.'})
            elif action == 'ConfirmDelete':
                for key, value in request.POST.items():
                    if 'input_id_' in key:
                        userModel.remove({'_id': ObjectId(value)})
            elif action == 'Modify':
                modUserForm = userForm.ModUserForm(request.POST)
                if modUserForm.is_valid():
                    origin_doc = userModel.find_one({'_id': ObjectId(id)})
                    document = modUserForm.cleaned_data
                    if origin_doc['email'] != document['email'] and userModel.not_duplicate({'email': document['email']}) == False:
                        return HttpResponse({'result': 'Email duplicated.'})
                    else:
                        userModel.update({'_id': ObjectId(id)}, document)
                else:
                    return JsonResponse({'result' : 'Form invalid.'})
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
            if action == 'Modify':
                modUserForm = userForm.ModUserForm(userModel.find_one({'_id': ObjectId(id)}))
            elif action == 'ExportJson':
                downloadResponse = HttpResponse(dumps(users), content_type='application/json')
                downloadResponse['Content-Disposition'] = 'attachment; filename=export.json'
                return downloadResponse
            else:
                addUserForm = userForm.AddUserForm()
                modUserForm = userForm.ModUserForm()
        return render(request, 'Backend/User/dashboard.html', locals())
    except:
        traceReport = traceback.format_exc()
        return render(request, 'Backend/Pages/traceback.html', locals())

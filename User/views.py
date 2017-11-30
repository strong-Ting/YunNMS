from bson import ObjectId
from django.shortcuts import render, redirect, HttpResponse, HttpResponseRedirect
from django.http import JsonResponse

from User import models as userModel
from User import forms as userForm

# Create your views here.
def dashboard(request, action=None, id=None):
    users = userModel.find_all(None)
    if request.method == 'POST':
        if action == 'Add':
            addUserForm = userForm.AddUserForm(request.POST)
            if addUserForm.is_valid():
                document = addUserForm.cleaned_data
                del document['passPreset'] # Remove unnecessary filed for frontend password render.
                if userModel.not_duplicate({'account': document['account']}) == False:
                    return HttpResponse({'result': 'Account duplicate.'})
                elif userModel.not_duplicate({'email': document['email']}) == False:
                    return HttpResponse({'result': 'Email duplicated.'})
                else:
                    userModel.create(document)
            else:
                return JsonResponse({'result' : 'Form invalid.'})
        elif action == 'ConfirmDelete':
            userModel.remove({'_id': ObjectId(id)})
        elif action == 'Modify':
            modUserForm = userForm.AddUserForm(request.POST)
            if modUserForm.is_valid():
                origin_doc = userModel.find_one({'_id': ObjectId(id)})
                document = modUserForm.cleaned_data
                if origin_doc['email'] != document['email'] and userModel.not_duplicate({'email': document['email']}) == False:
                    return HttpResponse({'result': 'Email duplicated.'})
                else:
                    userModel.update({'_id': ObjectId(id)}, document)
            else:
                return JsonResponse({'result' : 'Form invalid.'})
        return redirect('/backend/user/')
    else:
        if action == 'Modify':
            modUserForm = userForm.AddUserForm(userModel.find_one({'_id': ObjectId(id)}))
        elif action == 'Delete':
            document = userModel.find_one({'_id': ObjectId(id)})
            del document['passwd']
        else:
            addUserForm = userForm.AddUserForm()
    
    
    return render(request, 'Backend/User/dashboard.html', locals())

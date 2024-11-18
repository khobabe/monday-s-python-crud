from django.shortcuts import render,redirect
from .models import contactList

# Create your views here.
def home(req):
    
    if req.method == 'POST':
        name = req.POST.get('name')
        contact = req.POST.get('contact')
        newData = contactList(name=name, contact=contact)
        newData.save()
        return redirect('home-page')
            
    data = {}
    data['notes'] = contactList.objects.all()
    return render(req,"index.html",data)

def delete_work(arg, note_id):
    if arg.method == 'POST':
        contactList.objects.filter(id=note_id).delete()
        return redirect(home)
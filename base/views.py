from django.shortcuts import render, redirect
from django.conf import settings

db = settings.DB

# print('DATABASE:', settings.DB)
# dev_schema = settings.DB.create_schema('dev')

# Create your views here.
def index(request):
    devs = db.search_by_value('hackathon', 'developers', "id", "*", get_attributes=['*'])
    context = {"devs":devs}
    return render(request, 'base/index.html', context)


def dev_profile(request, pk):
    dev = db.search_by_hash('hackathon', 'developers', [pk], get_attributes=['*'])[0]
    context = {"dev":dev}
    return render(request, 'base/profile.html', context)


def add_profile(request):
    if request.method == 'POST':
        data = request.POST
        db.insert('hackathon', 'developers', [{"name":data['name']}])
        return redirect('index')
    return render(request, 'base/form.html')


def update_profile(request, pk):
    if request.method == 'POST':
        data = request.POST
        db.update('hackathon', 'developers', [{"id":pk, "name":data["name"]}])
        return redirect('index')

    dev = db.search_by_hash('hackathon', 'developers', [pk], get_attributes=['*'])[0]
    return render(request, 'base/form.html', {"dev":dev})

def delete_profile(request, pk):
    if request.method == 'POST':
        db.delete('hackathon', 'developers', [pk])
        return redirect('index')

    dev = db.search_by_hash('hackathon', 'developers', [pk], get_attributes=['*'])[0]
    return render(request, 'base/delete.html', {'dev':dev})
from django.shortcuts import render
from govern.models import Position, Role
from django.http import HttpResponseRedirect
from django.urls import reverse


# Create your views here.
def index(request):
    return render(request, 'govern/index.html')


def state(request):
    position = Position.objects.all().order_by('date')
    context = {'key': position}
    return render(request, 'govern/state.html', context)


def role(request, state_id):
    position = Position.objects.get(id=state_id)
    role = position.role_set.order_by('date')
    context = {'position': position, 'role': role}
    return render(request, 'govern/role.html', context)


def add_position(request):
    if request.method == 'POST':
        name = request.POST['name']

        add_position = Position(name=name)

        if add_position:
            add_position.save()
            return HttpResponseRedirect(reverse('index'))

    return render(request, 'govern/add_position.html', {})


def add_role(request, state_id):
    position = Position.objects.get(id=state_id)
    context = {'position': position}

    if request.method == 'POST':
        name = request.POST['name']

        add_role = Role(name=name,position=position)

        if add_role:
            add_role.save()
            return HttpResponseRedirect(reverse('role', args=state_id))

    return render(request, 'govern/add_role.html', context)

from django.shortcuts import render
from library_search.models import Library
from django.http import HttpResponse

try:
    from geopy import distance
except ImportError:
    from pip._internal import main as pip
    pip(['install', '--user', 'geopy'])
    from geopy import distance


# Create your views here.


def lsblank(request):
    return render(request, 'library_search/basicLS.html')


def location_processing(request):
    context={
        "libraries":[]
    }
    # currentcoordinate=(request.POST["la"],request.POST["lo"])
    currentcoordinate = (23.73816324407049, 90.39035984882445)
    maxdis=request.POST["dis"]
    for lib in Library.objects.all():
        libcoordinate=(lib.latitude,lib.longitude)
        print(f'{lib.latitude},{lib.longitude},{lib.id}')
        if distance.distance(currentcoordinate,libcoordinate).km <= float(maxdis):
            context["libraries"].append(lib)
    return render(request, 'library_search/listLibraries.html', context)


def libraryDetails(request,id):
    temp=Library.objects.filter(id=id)
    return render(request, 'library_search/library.html',context={"library":temp})
from django.shortcuts import render
from .models import Staff
from .models import GatedGuarded
from .models import HighRise
from .models import Complex
from .models import OurService
# Create your views here.
def index(request):
    Staffs = Staff.objects.all()
    GatedGuardeds = GatedGuarded.objects.all()
    HighRises =  HighRise.objects.all()
    Complexes = Complex.objects.all()
    Services = OurService.objects.all()
    return render(request, 'index.html',{'Staffs':Staffs,'GGS':GatedGuardeds, 'HRS': HighRises, 'CPS':Complexes, 'SRS':Services})
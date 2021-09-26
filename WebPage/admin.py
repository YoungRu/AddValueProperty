from django.contrib import admin
from .models import Staff
from .models import GatedGuarded
from .models import HighRise
from .models import Complex
from .models import OurService
# Register your models here.
admin.site.register(Staff)
admin.site.register(GatedGuarded)
admin.site.register(HighRise)
admin.site.register(Complex)
admin.site.register(OurService)


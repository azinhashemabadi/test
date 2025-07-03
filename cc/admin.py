from django.contrib import admin
from .models import Measurement
from .models import Ping
from .models import DNS
from .models import Download
from .models import Upload
from .models import Web
# Register your models here.

admin.site.register(Measurement)
admin.site.register(Ping)
admin.site.register(DNS)
admin.site.register(Download)
admin.site.register(Upload)
admin.site.register(Web)


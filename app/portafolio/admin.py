from django.contrib import admin

# Register your models here.
from .models import Project

from .models import RelProjectComment
from .models import RelProjectFeature
from .models import RelProjectUser
from .models import CatStateFeature
from .models import User
from .models import View


admin.site.register(Project)
admin.site.register(RelProjectComment)
admin.site.register(RelProjectFeature)
admin.site.register(RelProjectUser)
admin.site.register(CatStateFeature)
admin.site.register(User)
admin.site.register(View)

from django.contrib import admin
from dolweb.downloads.models import ReleaseVersion, DevVersion

class ReleaseVersionAdmin(admin.ModelAdmin):
    list_display = ('version', 'date')
    ordering = ('-date',)
    fieldsets = (
        ('Release infos', {
            'fields': ('version',),
        }),
        ('Download links', {
            'fields': ('win32_url', 'win64_url', 'osx_url'),
        }),
    )
admin.site.register(ReleaseVersion, ReleaseVersionAdmin)

class DevVersionAdmin(admin.ModelAdmin):
    list_display = ('revbranch', 'hash', 'date', 'author')
    ordering = ('-date',)
    fieldsets = (
        ('Revision infos', {
            'fields': ('branch', 'shortrev', 'hash', 'author',
                       'description', 'description_abbrev'),
        }),
        ('Download links', {
            'fields': ('win32_url', 'win64_url', 'osx_url'),
        }),
    )
admin.site.register(DevVersion, DevVersionAdmin)

from django.contrib import admin
from .models import Registros, Usuarios, Modulo, ValorCriticoHumedad, ValorCriticoPresion, ValorCriticoTemperatura


class ValorCriticoPresionAdmin(admin.ModelAdmin):
    exclude = ('usuario',)
    def save_model(self, request, obj, form, change):
        if not obj.usuario:
            obj.usuario = request.user
        super().save_model(request, obj, form, change)
    
    def has_add_permission(self, request):
        return getattr(request.user, 'es_administrador', False)

    def has_change_permission(self, request, obj=None):
        return getattr(request.user, 'es_administrador', False)

    def has_delete_permission(self, request, obj=None):
        return getattr(request.user, 'es_administrador', False)

    def has_view_permission(self, request, obj=None):
        return True

class ValorCriticoHumedadAdmin(admin.ModelAdmin):
    exclude = ('usuario',)
    def save_model(self, request, obj, form, change):
        if not obj.usuario:
            obj.usuario = request.user
        super().save_model(request, obj, form, change)
    
    def has_add_permission(self, request):
        return getattr(request.user, 'es_administrador', False)

    def has_change_permission(self, request, obj=None):
        return getattr(request.user, 'es_administrador', False)

    def has_delete_permission(self, request, obj=None):
        return getattr(request.user, 'es_administrador', False)

    def has_view_permission(self, request, obj=None):
        return True

class ValorCriticoTemperaturaAdmin(admin.ModelAdmin):
    exclude = ('usuario',)
    def save_model(self, request, obj, form, change):
        if not obj.usuario:
            obj.usuario = request.user
        super().save_model(request, obj, form, change)
    
    def has_add_permission(self, request):
        return getattr(request.user, 'es_administrador', False)

    def has_change_permission(self, request, obj=None):
        return getattr(request.user, 'es_administrador', False)

    def has_delete_permission(self, request, obj=None):
        return getattr(request.user, 'es_administrador', False)

    def has_view_permission(self, request, obj=None):
        return True

class RegistrosAdmin(admin.ModelAdmin):
    
    def has_add_permission(self, request):
        return getattr(request.user, 'es_administrador', False)

    def has_change_permission(self, request, obj=None):
        return getattr(request.user, 'es_administrador', False)

    def has_delete_permission(self, request, obj=None):
        return getattr(request.user, 'es_administrador', False)

    def has_view_permission(self, request, obj=None):
        return True

class UsuariosAdmin(admin.ModelAdmin):

    def has_add_permission(self, request):
        return getattr(request.user, 'es_administrador', False)

    def has_change_permission(self, request, obj=None):
        return getattr(request.user, 'es_administrador', False)

    def has_delete_permission(self, request, obj=None):
        return getattr(request.user, 'es_administrador', False)

    def has_view_permission(self, request, obj=None):
        return True
    
class ModuloAdmin(admin.ModelAdmin):
    
    def has_add_permission(self, request):
        return getattr(request.user, 'es_administrador', False)

    def has_change_permission(self, request, obj=None):
        return getattr(request.user, 'es_administrador', False)

    def has_delete_permission(self, request, obj=None):
        return getattr(request.user, 'es_administrador', False)

    def has_view_permission(self, request, obj=None):
        return True

admin.site.register(Registros,RegistrosAdmin)
admin.site.register(Usuarios,UsuariosAdmin)
admin.site.register(Modulo,ModuloAdmin)
admin.site.register(ValorCriticoHumedad, ValorCriticoHumedadAdmin)
admin.site.register(ValorCriticoPresion, ValorCriticoPresionAdmin)
admin.site.register(ValorCriticoTemperatura, ValorCriticoTemperaturaAdmin)
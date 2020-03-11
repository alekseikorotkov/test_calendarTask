from django.contrib import admin
from db.models import  Country,Company, Period, Agreement
from app.forms import AgreementForm
# Register your models here.

class CountryAdmin(admin.ModelAdmin):
    list_display = ['id', "name",'iso_code']
    list_filter = ['iso_code']
    search_fields = ['id', "name",'iso_code']
    class Meta:
        model = Country

class CompanyAdmin(admin.ModelAdmin):
    list_display = ['id','title','country']
    search_fields = ['id','title','country__name']
    list_filter = ['country']
    class Meta:
        model = Company

class PeriodAdmin(admin.ModelAdmin):
    list_display = ['id','start','stop','status']
    search_fields = ['id','start','stop','status']
    list_filter = ['status','start','stop']
    class Meta:
        model = Period

class AgreementAdmin(admin.ModelAdmin):
    # list_display = ['id','negotiator','company']
    list_display = ['id','negotiator','company','start','stop']
    list_filter = ['negotiator','company','start','stop']
    form = AgreementForm
    exclude = ['negotiator']
    fields = ['company', ('start','stop'),'period']
    search_fields = ['id','negotiator__username','company__title','start','stop']
    def save_model(self, request, obj, form, change):
        if not change:
            obj.negotiator = request.user
        obj.save()

    class Meta:
        model = Agreement


admin.site.register(Country,CountryAdmin)
admin.site.register(Company,CompanyAdmin)
admin.site.register(Period,PeriodAdmin)
admin.site.register(Agreement,AgreementAdmin)
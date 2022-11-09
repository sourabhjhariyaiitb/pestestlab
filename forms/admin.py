from django.contrib import admin

# Register your models here.


from .models import BasicInformationModel # NutrigardenInformationModel, factsheetInformationModel, factsheetDynamicIndicatorsModel, financialExpensesModel, outputIndicatorsModel
admin.site.register(BasicInformationModel)
# admin.site.register(NutrigardenInformationModel)
# admin.site.register(factsheetInformationModel)
# admin.site.register(factsheetDynamicIndicatorsModel)
# admin.site.register(financialExpensesModel)
# admin.site.register(outputIndicatorsModel)
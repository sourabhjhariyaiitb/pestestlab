from django.shortcuts import render
from .forms import BasicInformationForm # NutrigardenInformationForm, factsheetInformationForm, factsheetDynamicIndicatorsForm, financialExpensesForm, outputIndicatorsForm
from django.shortcuts import redirect
# Create your views here.
def basicinfo(request):
    if request.method == 'POST':
        form = BasicInformationForm(request.POST)
        if form.is_valid():
            instance = form.save()
            instance.user = request.user
            instance.save()
            print("data is saved.")
            return redirect('/')
    else:
        form = BasicInformationForm()
    return render(request,'forms/basic_forms.html',{'form':form})

# def basicinformation(request):

#     return render(request,'basic_information_form.html',{'form': form})


# def NGForm(request):
#     if request.method == 'POST':
#         form = NutrigardenInformationForm(request.POST)
#         if form.is_valid():
#             instance = form.save()
#             instance.user = request.user
#             instance.save()
#             return redirect('/nginfo')
#     else:
#         form = NutrigardenInformationForm()
#     return render(request,'forms/nutritiongarden_info.html',{'form': form})

# def factsheet(request):
#     if request.method == 'POST':
#         form = factsheetInformationForm(request.POST)
#         if form.is_valid():
#             instance = form.save()
#             instance.user = request.user
#             instance.save()
#             print("data is saved.")
#             return redirect('/home')
       
#     else:
#         form = factsheetInformationForm()
#     return render(request,'forms/factsheet.html',{'form':form})

# def factsheet_dynamic(request):
#     if request.method == 'POST':
#         form = factsheetDynamicIndicatorsForm(request.POST)
#         if form.is_valid():
#             instance = form.save()
#             instance.user = request.user
#             instance.save()
#             print("data is saved.")
#             return redirect('/home')
       
#     else:
#         form = factsheetDynamicIndicatorsForm()
#     return render(request,'forms/factsheet_dynamic.html',{'form':form})

# def financial(request):
#     if request.method == 'POST':
#         form = financialExpensesForm(request.POST)
#         if form.is_valid():
#             instance = form.save()
#             instance.user = request.user
#             instance.save()
#             print("data is saved.")
#             return redirect('/home')
       
#     else:
#         form = financialExpensesForm()
#     return render(request,'forms/financial.html',{'form':form})


# def output_indicators(request):
#     if request.method == 'POST':
#         form = outputIndicatorsForm(request.POST)
#         if form.is_valid():
#             instance = form.save()
#             instance.user = request.user
#             instance.save()
#             print("data is saved.")
#             return redirect('/home')
       
#     else:
#         form = outputIndicatorsForm()
#     return render(request,'forms/output_indicators.html',{'form':form})
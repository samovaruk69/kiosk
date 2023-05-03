from django.shortcuts import render
from .models import *


def index(request):
    return render(request,'main/index.html')

def services_home(request):
    return render(request,'main/services.html')

def tariff_home(request):
    data = Traffic_gaz.objects.all()
    return render(request,'main/TariffGAZ.html', {'data': data})

def videoOT_home(request):
    data = Video_OT.objects.filter()
    return render(request,'main/VideoOT.html',{'data': data})

def OneWindow_home(request):
    return render(request,'main/OneWindow.html')

def bank_home(request):
    return render(request,'main/OneWindow/bank.html')

def claimBook_home(request):
    return render(request,'main/OneWindow/ClaimBook.html')

def Procedure_and_time_limits_home(request):
    data = Procedure_and_time_limits.objects.all()
    return render(request,'main/OneWindow/Procedure_and_time_limits.html', {'data': data})

def Rights_and_obligations_of_citizens_in_the_implementation_of_administrative_procedures_home(request):
    data = Rights_and_obligations_of_citizens_in_the_implementation_of_administrative_procedures.objects.all()
    return render(request,'main/OneWindow/Rights_and_obligations_of_citizens_in_the_implementation_of_administrative_procedures.html', {'data': data})

def Lists_of_administrative_procedures_home(request):
    data = Lists_of_administrative_procedures.objects.all()
    return render(request,'main/OneWindow/Lists_of_administrative_procedures.html', {'data': data})

def leadership_structure_home(request):
    return render(request,'main/OneWindow/leadership_structure/leadership_structure.html')

def leadership_Polotsk_home(request):
    data = leadership_Polotsk.objects.all()
    return render(request,'main/OneWindow/leadership_structure/leadership_Polotsk.html', {'data': data})

def leadership_Oblgas_home(request):
    data = leadership_Oblgas.objects.all()
    return render(request,'main/OneWindow/leadership_structure/leadership_Oblgas.html', {'data': data})

def leadership_Minenergo_home(request):
    data = leadership_Minenergo.objects.all()
    return render(request,'main/OneWindow/leadership_structure/leadership_Minenergo.html', {'data': data})

def leadership_GPO_home(request):
    data = leadership_GPO.objects.all()
    return render(request,'main/OneWindow/leadership_structure/leadership_GPO.html', {'data': data})

def Mode_of_operation_and_schedule_of_reception_of_citizens_home(request):
    data = Mode_of_operation_and_schedule_of_reception_of_citizens.objects.all()
    return render(request,'main/OneWindow/Mode_of_operation_and_schedule_of_reception_of_citizens.html', {'data': data})


def list_of_documents_home(request):
    return render(request,'main/OneWindow/list_of_documents/list_of_documents.html')


def Document_forms_home(request):
    data = Document_forms.objects.all()
    return render(request,'main/OneWindow/Document_forms.html', {'data': data})

def BRSM_home(request):
    data = BRSM.objects.all()
    return render(request,'main/OneWindow/list_of_documents/BRSM.html', {'data': data})

def Decrees_home(request):
    data = Decrees.objects.all()
    return render(request,'main/OneWindow/list_of_documents/Decrees.html', {'data': data})

def Directives_home(request):
    data = Directives.objects.all()
    return render(request,'main/OneWindow/list_of_documents/Directives.html', {'data': data})

def Laws_home(request):
    data = Laws.objects.all()
    return render(request,'main/OneWindow/list_of_documents/Laws.html', {'data': data})

def Ordinances_home(request):
    data = Ordinances.objects.all()
    return render(request,'main/OneWindow/list_of_documents/Ordinances.html', {'data': data})

def Others_home(request):
    data = Others.objects.all()
    return render(request,'main/OneWindow/list_of_documents/Others.html', {'data': data})

def Resolutions_home(request):
    data = Resolutions.objects.all()
    return render(request,'main/OneWindow/list_of_documents/Resolutions.html', {'data': data})
from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import TemplateView


urlpatterns = [
    path('',views.index,name='index'),
    path('services/', views.services_home , name='services'),
    path('tariff/',views.tariff_home,name='tariff'),
    path('video/',views.videoOT_home,name='video'),


    path('OneWindow/',views.OneWindow_home,name='OneWindow'),
    path('OneWindow/bank/', views.bank_home, name='bank'),
    path('OneWindow/ClaimBook/', views.claimBook_home, name='claimBook'),
    path('OneWindow/Procedure_and_time_limits/', views.Procedure_and_time_limits_home, name='Procedure_and_time_limits'),
    path('OneWindow/Procedure_and_time_limits/', views.Procedure_and_time_limits_home,name='Procedure_and_time_limits'),
    path('OneWindow/Rights_and_obligations_of_citizens_in_the_implementation_of_administrative_procedures/', views.Rights_and_obligations_of_citizens_in_the_implementation_of_administrative_procedures_home,name='Rights_and_obligations_of_citizens_in_the_implementation_of_administrative_procedures'),
    path('OneWindow/Lists_of_administrative_procedures/',views.Lists_of_administrative_procedures_home,name='Lists_of_administrative_procedures'),

    path('OneWindow/leadership_structure/leadership_structure/', views.leadership_structure_home, name='leadership_structure'),
    path('OneWindow/leadership_structure/leadership_Polotsk/', views.leadership_Polotsk_home,name='leadership_Polotsk'),
    path('OneWindow/leadership_structure/leadership_Oblgas/', views.leadership_Oblgas_home,name='leadership_Oblgas'),
    path('OneWindow/leadership_structure/leadership_GPO/', views.leadership_GPO_home,name='leadership_GPO'),
    path('OneWindow/leadership_structure/leadership_Minenergo/', views.leadership_Minenergo_home,name='leadership_Minenergo'),

    path('OneWindow/Mode_of_operation_and_schedule_of_reception_of_citizens/', views.Mode_of_operation_and_schedule_of_reception_of_citizens_home,name='Mode_of_operation_and_schedule_of_reception_of_citizens'),

    path('OneWindow/list_of_documents/list_of_documents/', views.list_of_documents_home,name='list_of_documents'),

    path('OneWindow/Document_forms/', views.Document_forms_home, name='Document_forms'),
    path('OneWindow/Document_forms/BRSM/', views.BRSM_home, name='BRSM'),
    path('OneWindow/Document_forms/Decrees/', views.Decrees_home, name='Decrees'),
    path('OneWindow/Document_forms/Directives/', views.Directives_home, name='Directives'),
    path('OneWindow/Document_forms/Laws/', views.Laws_home, name='Laws'),
    path('OneWindow/Document_forms/Ordinances/', views.Ordinances_home, name='Ordinances'),
    path('OneWindow/Document_forms/Others/', views.Others_home, name='Others'),
    path('OneWindow/Document_forms/Resolutions/', views.Resolutions_home, name='Resolutions'),
    path('OneWindow/Document_forms/Video/', views.Video_home, name='Video'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
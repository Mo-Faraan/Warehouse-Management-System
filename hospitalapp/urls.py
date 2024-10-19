from django.urls import path
from . import views

urlpatterns = [
    path(route= 'home', view= views.homePageView, name='home'),
    path(route= 'login', view= views.loginPageView, name='login'),
    path(route= 'check', view= views.checkPageView, name='check'),
    path(route= 'admin', view= views.adminPageView, name='admin'),
    path(route= 'regdoc', view= views.regdocPageView, name='regdoc'),
    path(route= 'regpat', view= views.regpatPageView, name='regpat'),
    path(route= 'lisdoc', view= views.lisdocPageView, name='lisdoc'),
    path(route= 'lispat', view= views.lispatPageView, name='lispat'),
    path(route= 'docsave', view= views.docsavePageView, name='docsave'),
    path(route= 'patsave', view= views.patsavePageView, name='patsave'),

    path(route='deletedoc/<int:doctor_id>/',view = views.deleteDoctorView, name = 'deletedoctor'),
    path(route='deletepat/<int:patient_id>/',view = views.deletePatientView, name = 'deletepatient'),
    path(route='updatedoc/<int:doctor_id>/',view = views.updateDoctorView, name = 'updatedoctor'),
    path(route='updatepat/<int:patient_id>/',view = views.updatePatView, name = 'updatepatient'),

    path(route='singledoc/<int:doctor_id>/', view= views.singledocPageView, name='singledoc'),
    path(route='singlepat/<int:patient_id>/', view= views.singlepatPageView, name='singlepat'),

]
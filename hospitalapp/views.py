from django.shortcuts import render,redirect
from hospitalapp.models import doctor,patient

# Create your views here.
def homePageView(request):
    return render(request=request, template_name = 'home.html',context = {})
    if request.method == 'POST':
        return redirect('login')

def loginPageView(request):
    return render(request=request, template_name = 'login.html',context = {})

def checkPageView(request):
    if request.method == 'POST':
        # Retrieve form data
        username = request.POST['username']
        password = request.POST['password']

        print("User Name : ", username)
        print("Password : ", password)

        if username=='farhan' and password=='1234':
            print('successfull')
            return redirect('admin')

def adminPageView(request):
    return render(request=request, template_name = 'admin.html',context = {})

def regdocPageView(request):
    return render(request=request, template_name = 'regdoc.html',context = {})

def regpatPageView(request):
    return render(request=request, template_name = 'regpat.html',context = {})

def lisdocPageView(request):
    doctors = doctor.objects.all()
    context = {
        'alldoctors':doctors
    }
    return render(request=request, template_name = 'lisdoc.html',context = context)

def lispatPageView(request):
    patients = patient.objects.all()
    context = {
        'allpatients':patients
    }
    return render(request=request, template_name = 'lispat.html',context = context)

def docsavePageView(request):
    if request.method == 'POST':
        # Retrieve form data
        name = request.POST['name']
        address = request.POST['address']
        phno = request.POST['phno']
        field = request.POST['field']
        email = request.POST['email']
        """ username = request.POST['username']
        password = request.POST['password'] """

        Doctor = doctor(name=name, address=address, phno=phno, field=field, email=email)
        Doctor.save()
        return redirect('admin')

def patsavePageView(request):
    if request.method == 'POST':
        # Retrieve form data
        name = request.POST['name']
        address = request.POST['address']
        phno = request.POST['phno']
        email = request.POST['email']

        Patient = patient(name=name, address=address, phno=phno, email=email)
        Patient.save()
        return redirect('admin')

def deleteDoctorView(request,doctor_id):
    Doctor = doctor.objects.filter(pk = doctor_id)
    Doctor.delete()
    return redirect('lisdoc')

def deletePatientView(request,patient_id):
    Patient = patient.objects.filter(pk = patient_id)
    Patient.delete()
    return redirect('lispat')

def updateDoctorView(request,doctor_id):
    if request.method == 'POST':
        name = request.POST['name']
        address = request.POST['address']
        phno = request.POST['phno']
        field = request.POST['field']
        email = request.POST['email']

        Doctor = doctor.objects.get(pk = doctor_id)
        Doctor.name = name
        Doctor.address = address
        Doctor.phno = phno
        Doctor.field = field
        Doctor.email = email

        Doctor.save()
        return redirect("lisdoc")

def updatePatView(request,patient_id):
    if request.method == 'POST':
        name = request.POST['name']
        address = request.POST['address']
        phno = request.POST['phno']
        email = request.POST['email']

        pat = patient.objects.get(pk = patient_id)
        pat.name = name
        pat.address = address
        pat.phno = phno
        pat.email = email

        pat.save()
        return redirect("lispat")


def singledocPageView(request,doctor_id):
        Doc = doctor.objects.get(pk = doctor_id)
        context = {
            'singledoc': Doc
        }
        return render(request=request, template_name = 'singledoc.html',context = context)

def singlepatPageView(request,patient_id):
    pat = patient.objects.get(pk = patient_id)
    context = {
        'singlepat' : pat
    }
    return render(request=request, template_name = 'singlepat.html', context=context)



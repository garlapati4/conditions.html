from django.shortcuts import render

# Create your views here.
def condition(request):
    d={'a':20}
    return render(request,'condition.html',context=d)

def statement(request):
    d={'a':20,'b':30}
    return render(request,'statement.html',context=d)

def conditions(request):
    d={'a':20,'b':30,'c':40}
    return render(request,'conditions.html',context=d)

def statements(request):
    d={'a':50,'b':60,'c':40}
    return render(request,'statements.html',context=d)
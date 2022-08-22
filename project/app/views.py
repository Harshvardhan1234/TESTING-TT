from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def home2(request):
    num = request.POST['x']
    num2 = request.POST['y']
    if num == 'harsh' and num2 == '123':
        return render(request, 'home2.html')
    else:
        return render(request, 'home.html')
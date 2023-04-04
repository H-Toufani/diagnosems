from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt


from joblib import load
model = load('./savedModels/model.joblib')

@csrf_exempt
def page1(request): 
    if request.method == 'POST':  
        Suggestion = 'You are not suffering from MS. It is suggested that visit a neurologist for further examination.'  
        if 'pain' in request.POST:
            checkbox_value = request.POST['pain']
            if checkbox_value == 'yes':
                return render(request, 'page1.html', {'Suggestion' : Suggestion})
        elif 'illness' in request.POST:
            checkbox_value = request.POST['illness']
            if checkbox_value == 'yes':
                return render(request,'page1.html', {'Suggestion' : Suggestion})
        elif 'weight' in request.POST:
            checkbox_value = request.POST['weight']
            if checkbox_value == 'yes':
                return render(request, 'page1.html', {'Suggestion' : Suggestion})
        elif 'drug' in request.POST:
            checkbox_value = request.POST['drug']
            if checkbox_value == 'yes':
                return render(request, 'page1.html', {'Suggestion' : Suggestion})
        else:
            Suggestion = 'You need to do physical tests at a medical center and then press the button below to continue the process'
            return render(request, 'page1.html', {'Suggestion' : Suggestion})
    return render(request, 'page1.html')
     
@csrf_exempt 
def page2(request):
    if request.method == 'POST': 
        Pyramidal = request.POST['Pyramidal']
        Cerebellar = request.POST['Cerebellar']
        Brainstem = request.POST['Brainstem']
        Sensory = request.POST['Sensory']
        Bowel = request.POST['Bowel']
        Visual = request.POST['Visual']
        Mental = request.POST['Mental']
        walk = request.POST['walk']
        Y_pred = model.predict([[Pyramidal, Cerebellar, Brainstem, Sensory, Bowel, Visual, Mental, walk]])
        if Y_pred[0] == 0:
            Suggestion = 'You are not suffering from MS. It is suggested that visit a neurologist for further examination.'  
            return render(request, 'page2.html', {'Suggestion' : Suggestion})
        else:
            Suggestion = 'You need to take an MRI image at a medical center and then press the button below to continue the process'
            return render(request, 'page2.html', {'Suggestion' : Suggestion})
    return render(request, 'page2.html')

@csrf_exempt 
def page3(request):
    if request.method == 'POST': 
        number = request.POST['Number']
        Suggestion = 'You are suffering from MS.' 
        if 'one' in request.POST:
            checkbox_value = request.POST['one']
            if checkbox_value == 'yes':
                return render(request, 'page3.html', {'Suggestion' : Suggestion})
        if 'two' in request.POST:
            checkbox_value = request.POST['two']
            if checkbox_value == 'yes':
                return render(request, 'page3.html', {'Suggestion' : Suggestion})
        if 'three' in request.POST:
            checkbox_value = request.POST['three']
            if checkbox_value == 'yes':
                return render(request, 'page3.html', {'Suggestion' : Suggestion})
        if 'six' in request.POST:
            checkbox_value = request.POST['six']
            if checkbox_value == 'yes':
                return render(request, 'page3.html', {'Suggestion' : Suggestion})
        else:
            Suggestion = 'You are not suffering from MS. It is suggested that visit a neurologist for further examination.'    
            return render(request, 'page3.html', {'Suggestion' : Suggestion})
        
    return render(request, 'page3.html')


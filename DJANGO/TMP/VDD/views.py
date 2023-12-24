from django.shortcuts import render
from .forms import ImageForm
from .models import ImageModel
# Create your views here.
def home_view(request):
    context ={}
    if request.method=="POST":
        form = ImageForm(request.POST,request.FILES)
        if form.is_valid():
            name = form.cleaned_data.get("name")
            img = form.cleaned_data.get("img_field")
            obj = ImageModel.objects.create(title=name,img=img)
            obj.save()
            print(obj)
    else:
        form=ImageForm()
    context['form']=form
    return render(request, "home.html", context)
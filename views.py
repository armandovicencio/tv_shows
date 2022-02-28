
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.urls import reverse
from django.contrib import messages
from django.views import View
from shows.forms import ShowForm
from shows.models import Show

# Create your views here.

class ShowsView(View):
    def get(self, request):

        contexto = {
            'formModel': ShowForm(),
            'shows': Show.objects.all(),
        }

        return render(request, 'shows/index.html', contexto )
    def post(self, request):
        form = ShowForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Show creado correctamente')
            return redirect(reverse('shows:index'))
        else:
            messages.error(request, 'Con errores, solucionar.')
            return render(request, 'shows/index.html', {'formModel'  : form})
        
    
class ShowsDetail(View):
    def get(self, request):

        shows = Show.objects.all()
        

        contexto = {
            
            'shows': Show.objects.all(),
        }

        return render(request, 'shows/lista.html', contexto)
    
def delete_shows_api(request, id):
    show = Show.objects.get(id=id)
    show.delete()
    return JsonResponse({ 'success': True })

class ShowsEdit(View):
    def get(self, request, id):

        show = Show.objects.get(id=id)
        form = ShowForm(instance=show)

        contexto = {
            'formModel': form,
            'shows': Show.objects.all(),
        }

        return render(request, 'shows/index.html', contexto)

    def post(self, request, id):
        show = Show.objects.get(id=id)
        form = ShowForm(request.POST, instance=show)

        if form.is_valid():
            form.save()
            messages.success(request, 'Show editado correctamente')
            return redirect(reverse('shows:index'))
        else:
            messages.error(request, 'Con errores, solucionar.')
            return render(request, 'shows/index.html', {'formModel'  : form})
    
def vershow(request, id):
    if request.method == "GET":
        
      
        contexto = {
        'show': Show.objects.get(id=id)
        
        }
        return render(request, 'shows/detail.html', contexto)
    
    
    
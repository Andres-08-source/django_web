from django.shortcuts import render, redirect
from .forms import RegistroForm

def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('registro')  # Puedes cambiar esto por 'login' después
    else:
        form = RegistroForm()
    return render(request, 'usuarios/registro.html', {'form': form})



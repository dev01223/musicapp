from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST

def home_view(request):
    if request.user.is_authenticated:
        # Se o usuário estiver logado, renderize uma página específica
        return render(request, 'core/playlists.html')
    else:
        # Se o usuário não estiver logado, renderize uma página diferente
        return render(request, 'core/registro.html')


def update_saldo(request):
    user = request.user
    user.saldo += 5
    user.save()
    return JsonResponse({'status': 'success'})
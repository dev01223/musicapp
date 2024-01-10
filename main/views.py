from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.shortcuts import render
from django.utils import timezone
from datetime import timedelta




def home_view(request):
    if request.user.is_authenticated:
        now = timezone.now()
        if request.user.first_login:
            days_since_first_login = (now - request.user.first_login).days
            if days_since_first_login < 1:
                return render(request, 'core/playlists1.html')
            elif days_since_first_login < 7:
                return render(request, 'core/playlists2.html')
            else:
                return render(request, 'core/playlists.html')
        else:
            # Adicione um retorno aqui para cobrir a situação onde request.user.first_login é None
            return render(request, 'core/playlists.html')
    else:
        return render(request, 'core/registro.html')

def update_saldo(request):
    user = request.user
    user.saldo += 5
    user.save()
    return JsonResponse({'status': 'success'})


def saque(request):
    return render(request, 'core/saque.html')
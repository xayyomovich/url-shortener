from django.shortcuts import render, redirect
from django.http import HttpResponse
import hashlib
import string
import random
from .models import URL


def generate_short_code(url):
    hash_object = hashlib.md5(url.encode())
    return hash_object.hexdigest()[:6]


def random_short_code(length=6):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))


def home(request):
    if request.method == 'POST':
        original_url = request.POST.get('url')
        if not original_url.startswith(('http://', 'https://')):
            original_url = 'http://' + original_url
        try:
            url_obj = URL.objects.get(original_url=original_url)
            short_url = request.build_absolute_uri('/') + url_obj.short_code
        except URL.DoesNotExist:
            short_code = generate_short_code(original_url)
            while URL.objects.filter(short_code=short_code).exists():
                short_code = random_short_code()
            url_obj = URL.objects.create(
                short_code=short_code,
                original_url=original_url
            )
            short_url = request.build_absolute_uri('/') + short_code
        return render(request, 'shortener/index.html', {'short_url': short_url})
    return render(request, 'shortener/index.html')


def redirect_url(request, short_code):
    try:
        url_obj = URL.objects.get(short_code=short_code)
        return redirect(url_obj.original_url)
    except URL.DoesNotExist:
        return HttpResponse("URL not found", status=404)

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView, DetailView, UpdateView, DeleteView
from django.shortcuts import render
import requests
from requests_html import HTMLSession


def get_html_content(city):
    s = HTMLSession()
    city = city.replace(' ', '+')
    url = f'https://www.google.com/search?q=weather+{city}'
    r = s.get(url, headers={
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'})
    return r


def home_view(request):
    if 'city' in request.GET:
        city = request.GET.get('city')
        html_content = get_html_content(city)
        temp = html_content.html.find('span#wob_tm', first=True).text
        unit = html_content.html.find('div.vk_bk.wob-unit span.wob_t', first=True).text
        weather_type = html_content.html.find('div.wob_dcp span#wob_dc', first=True).text
        precipitatii = html_content.html.find('span#wob_pp', first=True).text
        umiditate = html_content.html.find('span#wob_hm', first=True).text
        locatie = html_content.html.find('div.wob_loc.q8U8x', first=True).text
        context = {
            "temperatura": temp,
            "unitate": unit,
            "descriere": weather_type,
            "precipitatii": precipitatii,
            "umiditate": umiditate,
            "locatie": locatie
        }
    return render(request, 'home.html', {"context":context})
# Create your views here.

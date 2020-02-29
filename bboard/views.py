from django.http import HttpResponse

from .models import Bd

def index(request):
    s = 'Список объявлений!\r\n\r\n\r\n'
    for bb in Bd.objects.order_by('-published'):
        s += bb.title + '\r\n' + bb.content + '\r\n\r\n'
    return HttpResponse(s, content_type='text/plain; charset=utf-8')
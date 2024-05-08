from django.http import HttpResponse
import logging


logger = logging.getLogger(__name__)


def index(request):
    logger.info('Index page accessed')
    html = "<h1>Добро пожаловать!</h1>" \
           "<p>It's django based site</p>"

    return HttpResponse(html)


def about(request):
    logger.info('About page accessed')
    html = "<h1>О нас:</h1>" \
           "<p>It's django based site<br>" \
           "This site was create for learning popular" \
           "<br> <b>Django framework</b><br>" \
           "because it  fun and very helpful for job search!</p>"

    return HttpResponse(html)

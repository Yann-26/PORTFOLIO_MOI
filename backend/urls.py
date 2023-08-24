from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from rest_framework import routers, viewsets
from portbackend.models import *
from portbackend.serializers import *



# Vues basées sur les viewsets
class HeaderViewSet(viewsets.ModelViewSet):
    queryset = Header.objects.all()
    serializer_class = HeaderSerializer



class CardAboutViewSet(viewsets.ModelViewSet):
    queryset = CardAbout.objects.all()
    serializer_class = CardAboutSerializer

   

class AboutViewSet(viewsets.ModelViewSet):
    queryset = About.objects.all()
    serializer_class = AboutSerializer



class CompetenceViewSet(viewsets.ModelViewSet):
    queryset = Competence.objects.all()
    serializer_class = CompetenceSerializer



class LearnMoreViewSet(viewsets.ModelViewSet):
    queryset = LearnMore.objects.all()
    serializer_class = LearnMoreSerializer



class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer



class TestimonialViewSet(viewsets.ModelViewSet):
    queryset = Testimonial.objects.all()
    serializer_class = TestimonialSerializer




# Configuration du routeur

router = routers.DefaultRouter()
router.register(r'headers', HeaderViewSet)
router.register(r'card-about', CardAboutViewSet)
router.register(r'about', AboutViewSet)
router.register(r'competence', CompetenceViewSet)
router.register(r'learn-more', LearnMoreViewSet)
router.register(r'service', ServiceViewSet)
router.register(r'testimonial', TestimonialViewSet)



# URLs

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('', include('portbackend.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

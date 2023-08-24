from rest_framework import serializers, viewsets
from portbackend.models import *


# HEADER SERALIZER
class HeaderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Header
        fields = ['url', 'me_header', 'role', 'social1', 'social2', 'social3', 'social4', 'date_add', 'date_update', 'status']

class HeaderViewSet(viewsets.ModelViewSet):
    queryset = Header.objects.all()
    serializer_class = HeaderSerializer
# END HEADER SERIALIZER

#  CARDABOUT SERIALIZER
class CardAboutSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CardAbout
        fields = ['url', 'title', 'description', 'icon', 'date_add', 'date_update', 'status']

class CardAboutViewSet(viewsets.ModelViewSet):
    queryset = CardAbout.objects.all()
    serializer_class = CardAboutSerializer
# END CARDABOUT SERIALIZER

# ABOUT SERIALIZER
class AboutSerializer(serializers.HyperlinkedModelSerializer):
    card_about = CardAboutSerializer()

    class Meta:
        model = About
        fields = ['url', 'me_about', 'card_about', 'my_bio', 'date_add', 'date_update', 'status']

class AboutViewSet(viewsets.ModelViewSet):
    queryset = About.objects.all()
    serializer_class = AboutSerializer
# END ABOUT SERIALIZER

# COMPETENCE SERIALIZER
class CompetenceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Competence
        fields = ['url', 'title', 'icone', 'competence', 'rating', 'date_add', 'date_update', 'status']

class CompetenceViewSet(viewsets.ModelViewSet):
    queryset = Competence.objects.all()
    serializer_class = CompetenceSerializer
# END COMPETENCE SERIALIZER

# LEARNMORE SERIALIZER
class LearnMoreSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = LearnMore
        fields = ['url', 'content', 'date_add', 'date_update', 'status']

class LearnMoreViewSet(viewsets.ModelViewSet):
    queryset = LearnMore.objects.all()
    serializer_class = LearnMoreSerializer
# END LEARNMORE SERIALIZER



# SERVICE SERIALIZER
class ServiceSerializer(serializers.HyperlinkedModelSerializer):
    learn_more = LearnMoreSerializer()

    class Meta:
        model = Service
        fields = ['url', 'title', 'title_details', 'photo_serv', 'learn_more', 'date_add', 'date_update', 'status']

    def create(self, validated_data):
        learn_more_data = validated_data.pop('learn_more')
        service = Service.objects.create(**validated_data)
        LearnMore.objects.create(service=service, **learn_more_data)
        return service
# END SERVICE SERIALIZER




# TESTIMONIAL SERIALIZER
class TestimonialSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Testimonial
        fields = ['url', 'image', 'review', 'date_add', 'date_update', 'status']

class TestimonialViewSet(viewsets.ModelViewSet):
    queryset = Testimonial.objects.all()
    serializer_class = TestimonialSerializer
# END TESTIMONIAL SERIALIZER

from django.contrib import admin
from portbackend.models import *


class HeaderAdmin(admin.ModelAdmin):
    list_display = ('me_header', 'role', 'social1', 'social2', 'social3', 'social4')
admin.site.register(Header,  HeaderAdmin),

# //////////////////////
class CardAboutAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'icon', 'status')
    list_filter = ('status',)
    search_fields = ('title', 'description')
admin.site.register(CardAbout, CardAboutAdmin)

# //////////////////////
class AboutAdmin(admin.ModelAdmin):
    list_display = ('me_about', 'card_about', 'my_bio', 'status')
    list_filter = ('status', 'card_about')
    search_fields = ('my_bio',)
admin.site.register(About, AboutAdmin)

# //////////////////////
class CompetenceAdmin(admin.ModelAdmin):
    list_display = ('title', 'icone', 'competence', 'rating', 'status')
    list_filter = ('status',)
    search_fields = ('title', 'competence')
admin.site.register(Competence, CompetenceAdmin)

# //////////////////////
class LearnMoreAdmin(admin.ModelAdmin):
    list_display = ('content',)
admin.site.register(LearnMore, LearnMoreAdmin)

# //////////////////////
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'title_details', 'photo_serv', 'learn_more', 'status')
    list_filter = ('status',)
    search_fields = ('title', 'title_details')
admin.site.register(Service, ServiceAdmin)

# //////////////////////
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('image', 'review', 'status')
    list_filter = ('status',)
    search_fields = ('review',)
admin.site.register(Testimonial, TestimonialAdmin)


admin.site.register(Subscriber)
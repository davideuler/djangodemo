#coding:utf-8

from models import Project, STATUS_CHOICES

from django.contrib import admin
from django import forms
from django.conf import settings
from django.utils import timezone
from django.utils.safestring import mark_safe

class HorizRadioRenderer(forms.RadioSelect.renderer):
    """ this overrides widget method to put radio buttons horizontally
        instead of vertically.
    """
    def render(self):
            """Outputs radios"""
            return mark_safe(u'\n'.join([u'%s\n' % w for w in self]))

class ProjectForm(forms.ModelForm):
    status = forms.ChoiceField(label='阶段状态',choices=STATUS_CHOICES,initial='submmiting', widget=forms.RadioSelect(renderer=HorizRadioRenderer))

    class Meta:
        model = Project

        fields = "__all__"

def sync_to_jira(modeladmin, request, queryset):
    print u"%s %s" % ("demo",queryset[0])

sync_to_jira.short_description = "同步项目信息到Jira"

###########   Admins ##################

class ProjectAdmin(admin.ModelAdmin):
    form = ProjectForm
    list_display = ('name','team','customer_name','total_fee','status',)
    list_filter = ('team','status','customer_name',)
    search_fields = ['name','team','customer_name','status',]
    actions = [sync_to_jira]

    exclude = ('id',)

admin.site.register(Project,ProjectAdmin)
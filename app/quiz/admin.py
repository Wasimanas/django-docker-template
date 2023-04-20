from django.contrib import admin
from quiz.models import QuizCategory, Question, Option, TopicsIncluded
from django import forms
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
from django.utils.html import format_html
# Register your models here.

#######################################


#Forms 

###########################################

class QuestionAdminForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = "__all__"
        widgets = {
                   'questionText': SummernoteWidget(),
                   'solution': SummernoteWidget(),

                }



###########################################
#Inlines  


class OptionInline(admin.TabularInline):
    model = Option
    extra = 1

class QuestionInline(admin.TabularInline):
    model = Question

class TopicsIncludedInline(admin.TabularInline):
    model = TopicsIncluded


###########################################






class QuizCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ['title','published']
    list_editable = ['published'] 
    inlines = [TopicsIncludedInline]





class QuestionAdmin(admin.ModelAdmin):
    list_display = ('category',"questionTextAdmin")
    inlines = [OptionInline]
    form = QuestionAdminForm 

    @admin.display()
    def questionTextAdmin(self,obj):
        return format_html(obj.questionText)


admin.site.register(QuizCategory,QuizCategoryAdmin)
admin.site.register(Question,QuestionAdmin)
admin.site.register(Option)

from django.shortcuts import render, redirect, reverse
from django.views import View
from django.http import HttpResponse
from quiz.models import QuizCategory
# Create your views here. 


class HomePage(View):
    template_name = 'quiz/homePage.html'

    def get(self, request, *args, **kwargs):
        quizCategories = QuizCategory.objects.filter(published = True)

        context = {'quizCategories':quizCategories}
        return render(request, self.template_name, context)


class AboutPage(View):
    template_name = 'quiz/about.html'

    def get(self, request, *args, **kwargs):

        return render(request, self.template_name, context)


class QuizView(View):

    template_name = 'quiz/quizView.html' 

    def get(self, request, *args, **kwargs): 
        context = {}
        quizCategorySlug = kwargs['quizCategorySlug']
        if QuizCategory.objects.filter(slug = quizCategorySlug).exists(): 
            context['quizCategorySlug']=quizCategorySlug
        else:
            return redirect(reverse('quiz:quiz'))

        return render(request, self.template_name, context)


class AboutPage(View):
    template_name = 'quiz/about.html'

    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, self.template_name, context)


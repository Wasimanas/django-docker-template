from django.urls import path
from quiz import views
app_name = 'quiz'

urlpatterns = [
        path('',views.HomePage.as_view(),name='quiz'),
        path('about/',views.AboutPage.as_view(),name='about'),
        path('about/',views.AboutPage.as_view(),name='about'),
        path('quiz/<slug:quizCategorySlug>/',views.QuizView.as_view(),name='quizView',),
        ]

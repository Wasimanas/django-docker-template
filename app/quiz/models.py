from django.db import models
from django.utils.html import format_html
# Create your models here. 


class QuizCategory(models.Model):

    title = models.CharField(max_length = 250,unique = True)
    slug = models.SlugField(unique  = True)
    published = models.BooleanField(default = False)


    def __str__(self):
        return self.title



    class Meta:
        verbose_name_plural= ' QuizCategory'
   
class Question(models.Model):
    category = models.ForeignKey(QuizCategory,on_delete = models.CASCADE,null=True,blank = True) 
    questionText = models.TextField()
    solution = models.TextField(blank = True)


    def __str__(self):
        return format_html(self.questionText)

class Option(models.Model):
    question = models.ForeignKey(Question,on_delete = models.CASCADE,null = True,blank = True,related_name='options')
    optionText = models.CharField(max_length = 250)
    isCorrect = models.BooleanField(default = False)



    def __str__(self):
        return f"{self.optionText}"







class TopicsIncluded(models.Model):
    topic = models.CharField(max_length = 250)
    category = models.ForeignKey(QuizCategory,on_delete = models.CASCADE,null = True,blank = True,related_name = 'topics') 


    def __str__(self):
        if self.category:
            return f"Category : {self.category.title}, Topic : {self.topic}"


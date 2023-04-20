from channels.generic.websocket import WebsocketConsumer
import os
import json
from quiz.models import Question, QuizCategory, Option
from django.shortcuts import get_object_or_404
from random import randint


class QuizConsumer(WebsocketConsumer):

    def connect(self):
        self.accept()
        self.score = 0
        quizCategorySlug = self.scope['url_route']['kwargs']['quizCategorySlug'] 
        self.quizCategory = get_object_or_404(QuizCategory,slug = quizCategorySlug)   
        self.sendQuestion()



    def disconnect(self,close_code):
        self.close()



    def retrieveQuestion(self):
        questions = Question.objects.filter(category = self.quizCategory)
        totalNumberOfQuestions =len(questions) - 1
        randomQuestionNumber = randint(0,totalNumberOfQuestions) 
        question = questions[randomQuestionNumber]
        return question 


    def retreiveOptions(self):
        options = self.question.options.all()
        return options 



    def sendQuestion(self):
        question = self.retrieveQuestion()
        self.question = question
        options = self.retreiveOptions()
        options = [option.optionText for option in options]
        data = {"action":"question",
                "question":question.questionText,
                "options":options,
            
                }
        jsonData = json.dumps(data)
        self.send(text_data = jsonData) 

    def getCorrectOption(self):
        options = self.retreiveOptions()
        selectedOption = [option for option in options if option.isCorrect == True]
        return selectedOption[0]




        
    def submitAnswer(self, data):
        print(data)
        solution = self.question.solution
        options = self.retreiveOptions()
        options = [[option.optionText,option.isCorrect] for option in options] 
        score = self.updateScore(data['selectedAnswer'])

        returnData = {"action":"verifyAnswer",
                      "solution": solution,
                      "options":options,
                      "score":score,
                      } 
        
        self.send(json.dumps(returnData))





    def receive(self,text_data):
        """
        receive options : 
        - client sends selected answer option.
        - report question.
        - client clicks next button.
        """ 
        data = json.loads(text_data)
        if data['action'] == 'submitAnswer':
            self.submitAnswer(data)
        elif data['action'] == 'nextQuestion':
            self.sendQuestion()




    def updateScore(self,selectedAnswerText):
        selectedOption = self.getCorrectOption()
        print(selectedOption)
        print(selectedAnswerText)
        if selectedOption.optionText == selectedAnswerText:
            self.score = self.score + 1

        else: 
            self.score = self.score - 1 
        print(self.score)

        return self.score
            
        

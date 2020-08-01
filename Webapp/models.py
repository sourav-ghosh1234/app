from django.db import models

cat=(
    ('c','C'),
    ('c++','C++'),
    ('java','JAVA'),
    )

class Question(models.Model):

    category=models.CharField(max_length=20,choices=cat,default='c')
    qno=models.CharField(max_length=200,default='NULL')
    ques=models.CharField(max_length=200)
    opt1=models.CharField(max_length=200)
    opt2=models.CharField(max_length=200)
    opt3=models.CharField(max_length=200)
    opt4=models.CharField(max_length=200)
    answer=models.CharField(max_length=200)
    
    class Meta:
        db_table="question2"


class Time(models.Model):

    s=models.IntegerField()
   

    
    class Meta:
        db_table="time"

class Sub(models.Model):

    s=models.CharField(max_length=200)
    ques=models.CharField(max_length=200)
    marks=models.CharField(max_length=200)

    
    class Meta:
        db_table="sub"


class Contact(models.Model):

    firstname=models.CharField(max_length=200)
    lastname=models.CharField(max_length=200)
    country=models.CharField(max_length=200)
    subject=models.CharField(max_length=200)
    
    class Meta:
        db_table="contact"

experience=(
    ('bad','Bad'),
    ('average','Average'),
    ('good','Good'),
    )

class Feedback(models.Model):

    experience=models.CharField(max_length=20,choices=experience,default='')
    cmnt=models.CharField(max_length=200)
    name=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    
    class Meta:
        db_table="feedback"



class QuestionAns(models.Model):

    qno=models.CharField(max_length=200,default='NULL')
    ques=models.CharField(max_length=200)
    opt1=models.CharField(max_length=200)
    opt2=models.CharField(max_length=200)
    opt3=models.CharField(max_length=200)
    opt4=models.CharField(max_length=200)
    answer=models.CharField(max_length=200)
    yanswer=models.CharField(max_length=200)
    com=models.CharField(max_length=200,default='NULL')
    class Meta:
        db_table="question_ans"



class Score2(models.Model):

    cat=models.CharField(max_length=20)
    user=models.CharField(max_length=20)
    scores=models.CharField(max_length=20)

    class Meta:
        db_table="score2"

class Max(models.Model):

    
    user=models.CharField(max_length=20)
    sc=models.IntegerField()

    class Meta:
        db_table="max2"
   

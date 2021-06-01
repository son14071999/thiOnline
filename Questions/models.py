from djongo import models
from Exams.models import Exams
# Create your models here.

# class GroupQuestion(models.Model):
#     content = models.TextField(null=False)
#     questions = models.ArrayField()


class Questions(models.Model):
    id_exam = models.ForeignKey(Exams, on_delete=models.CASCADE)
    question = models.TextField(null=True, blank=True)
    answers = models.JSONField(null=True, blank=True, default=dict)
    level_of_different = models.FloatField(default=2.5)
    link_media = models.FileField(null=True, blank=True, upload_to='exam/')
    same_questions = models.TextField(null=True, blank=True)
    subject = models.CharField(null=False, max_length=50)
    correct_answer = models.CharField(max_length=2)
from djongo import models
from Exams.models import Exams
from MyUser.models import User
# Create your models here.
class History(models.Model):
    id_exam = models.ForeignKey(Exams, on_delete=models.CASCADE)
    status = models.BooleanField(default=True)
    time_end = models.DateTimeField(auto_now_add=True)
    date = models.DateTimeField(auto_now_add=True)
    time_do = models.IntegerField(null=False)
    id_user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_list_correct_questions = models.TextField(null=True, blank=True)
    id_list_questions = models.TextField(null=False)
from djongo import models
from MyUser.models import User
# Create your models here.
#
class Exams(models.Model):
    name = models.CharField(max_length=255, null=False)
    slug = models.CharField(max_length=255, null=False)
    innitiated_date = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    id_author = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=50, null=False)
    level_of_different = models.FloatField(default=2.5)
    medium_score = models.FloatField(default=0)
    time = models.IntegerField(null=False)
    list_id_questions = models.TextField(null=True)
    list_id_questions_group = models.TextField(null=True, blank=True)
    amount_questions = models.IntegerField(null=False, default=0)
    amount_view_user = models.IntegerField(default=0)
    amount_do = models.IntegerField(default=0)
    comments = models.JSONField(null=True, blank=True, default=dict)
    options = models.JSONField(null=True, blank=True, default=dict)

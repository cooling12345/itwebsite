from django.db import models
from acc.models import User

# Create your models here.
class Board(models.Model):
    subject = models.CharField(max_length=100)
    writer = models.ForeignKey(User, null=True, default=0, on_delete=models.CASCADE)
    content = models.TextField()
    pubdate = models.DateTimeField()
    likey = models.ManyToManyField(User, blank=True, related_name="likey")


    def __str__(self):
        return f"{self.writer}의 {self.subject}"

class Reply(models.Model):
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    replyer = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()

    def __str__(self):
        return f"{self.board} 에 {self.replyer}가 남긴 댓글"

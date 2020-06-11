from django.db import models

# Create your models here.
class Poll(models.Model):
    title = models.CharField('投票主題',max_length=100)
    desc = models.TextField('說明',max_length=512)
    created = models.DateField('建立時間',auto_now_add=True)

    def __str__(self):
        return '投票主題 {}'.format( self.subject)

class Option(models.Model):
    poll_id = models.IntegerField('所屬投票主題')
    title = models.CharField('選填文字',max_length=100)
    count = models.IntegerField('票數',default=0)
    
    def __str__(self):

       return '():({}) {}'.format(self.id, self.poll_id, self.tittle)
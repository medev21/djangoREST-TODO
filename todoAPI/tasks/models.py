from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles
from pygments import highlight

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())
# Create your models here.

class Task(models.Model):
    created = models.DateTimeField(auto_now_add = True)
    title = models.CharField(max_length = 100, blank = True, default = "")
    description = models.TextField()
    owner = models.ForeignKey('auth.User', related_name = 'tasks')
    highlighted = models.TextField()

    class Meta:
        ordering = ('created',)

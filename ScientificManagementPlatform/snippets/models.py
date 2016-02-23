from __future__ import unicode_literals

from django.db import models
from pygments.lexers import get_all_lexers, get_lexer_by_name
from pygments.styles import get_all_styles
from pygments.formatters.html import HtmlFormatter
from pygments import highlight
from django.contrib.auth.models import User

# Create your models here.
LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())

class Snippet(models.Model):
	# if we do not specify primary key, django will create id as pk for us
	owner = models.ForeignKey('auth.User', related_name = 'snippets')
	created = models.DateTimeField(auto_now_add = True)

	title = models.CharField(max_length = 100, blank = True, default = '')
	code = models.TextField()
	linenos = models.BooleanField(default = False)
	language = models.CharField(choices = LANGUAGE_CHOICES, default = 'python', max_length = 100)
	style = models.CharField(choices = STYLE_CHOICES, default = 'friendly', max_length = 100)
	#add field owner to represent the user who created the code snippet, in accordance with UserSerializer fields in serializers.py

	# store highlighted field using pygments highlighting library
	highlighted = models.TextField()

	# to make sure the model is saved, we populate the highlighted field
	def save(self, *args, **kwargs):
		lexer = get_lexer_by_name(self.language)
		linenos = self.linenos and 'table' or False
		options = self.title and {'title': self.title} or {}
		formatter = HtmlFormatter(style = self.style, linenos = linenos, full = True, **options)
		self.highlighted = highlight(self.code, lexer, formatter)
		super(Snippet, self).save(*args, **kwargs)

	class Meta:
		ordering = ('created',)

	
	

from wagtail.core.models import Page
from puput.abstracts import BlogAbstract
#from puput.models import BlogPage
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel
from django.db import models

class BlogPagePipe(BlogAbstract):
    about = RichTextField(verbose_name=('about'), blank=True)
    github = models.URLField(blank=True) 
    email = models.EmailField(blank=True)
    linkedin = models.URLField(blank=True)
    instagram = models.URLField(blank=True)

    content_panels = BlogAbstract.content_panels + [ 
        FieldPanel('about'),
        FieldPanel('github'),
        FieldPanel('email'),
        FieldPanel('linkedin'),
        FieldPanel('instagram'),
    ]
    
    class Meta:
        abstract = True
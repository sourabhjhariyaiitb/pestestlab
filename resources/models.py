from django.db import models

# Create your models here.
from django.db import models
from wagtail.core.fields import StreamField
from wagtail.core.models import Page
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from . import blocks
# from wagtail.embeds.blocks import EmbedBlock
# from resources.blocks import EmbedBlock

class ResourcesPage(Page):

    templates = "resources/resources_page.html"

    content = StreamField(
        [
            ("videocards",blocks.VideoCardBlock()),
            ("articlecards",blocks.ArticleCardBlock()),
            ("weblinkcards",blocks.WeblinkCardBlock()),

        ],
        null = True,
        blank = True
    )
    
    subtitle = models.CharField(max_length = 100, blank = True, null = True )
   
    content_panels = Page.content_panels + [

        FieldPanel("subtitle"),
        StreamFieldPanel("content"),
        
    ]
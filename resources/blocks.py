from wagtail.core import blocks
from wagtail.core.blocks import StructBlock
from wagtail.embeds.blocks import EmbedBlock
from wagtail.images.blocks import ImageChooserBlock

class ArticleBlock(blocks.StructBlock):

    Title = blocks.CharBlock(required = True, help_text  = 'Add Title')
    Author = blocks.CharBlock(required = True, help_text  = 'Add Author')
    Description = blocks.TextBlock(required = True, help_text = 'Add Description')
    Article = blocks.RichTextBlock(required=True)

    class Meta:

        template = 'resources/article_card.html' 
        icon = 'edit'
        label = 'Article'


class IndlineVideoBlock(blocks.StructBlock):
    title = blocks.CharBlock(required = True, help_text  = 'Add Title')
    video = EmbedBlock(label=("Video"))
    caption = blocks.CharBlock(required=False,label=("Caption"))

   
    class Meta:
        template="resources/video_card.html"
        icon="media"
        label="Video Card"


class VideoCardBlock(blocks.StructBlock):
    
    title = blocks.CharBlock(required = True, help_text  = 'Add Title')
    cards = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("title", blocks.CharBlock(required = True, help_text  = 'Add Title')),
                ("caption", blocks.CharBlock(required = True, help_text  = 'Caption')),
                ("video", EmbedBlock(label=("Video"))),
               
            ]
            
       )
    )   
    class Meta:
        template="resources/video_card.html"
        icon="media"
        label="Video Cards"

class ArticleCardBlock(blocks.StructBlock):
    
    title = blocks.CharBlock(required = True, help_text  = 'Add Title')
    cards = blocks.ListBlock(
        blocks.StructBlock(
            [   
                ("title", blocks.CharBlock(required = True, help_text  = 'Title')),
                ("author", blocks.CharBlock(required = True, help_text  = 'Author')),
                ("description", blocks.TextBlock(required = True, help_text = 'Description')),
                ("article", blocks.RichTextBlock(required=True,help_text = 'Article'))
            ]
            
       )
    )
    
   
    class Meta:
        template="resources/article_card.html"
        icon="media"
        label="Article Card"


class WebBlock(blocks.StructBlock):
    
    Title = blocks.CharBlock(required = True, help_text  = 'Add Title')
    Description = blocks.TextBlock(required = True, help_text = 'Add Description')
    Article = blocks.RichTextBlock(required=True)

    class Meta:

        template = 'resources/web_card.html' 
        icon = 'edit'
        label = 'weblink'


class WeblinkCardBlock(blocks.StructBlock):
    
    title = blocks.CharBlock(required = True, help_text  = 'Add Title')
    cards = blocks.ListBlock(
        blocks.StructBlock(
            [   
                ("title", blocks.CharBlock(required = True, help_text  = 'Title')),
                ("description", blocks.TextBlock(required = True, help_text = 'Description')),
                ("article", blocks.RichTextBlock(required=True,help_text = 'link'))
            ]
            
       )
    )
    
   
    class Meta:
        template="resources/web_card.html"
        icon="media"
        label="Weblink Card"
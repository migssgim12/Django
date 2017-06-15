from django.db import models

# Create your models here.

class Tag(models.Model):
    """
    A media category Tag generated ny the user

    """

    name =models.CharField(max_length=256)

    def __str__(self):
        return self.name



class Media(models.Model):
    """
    
    One media file (Audio, Image, Video)
    
    """

    MEDIA_TYPES = (
        ('IMG', 'Image'),
        ('AUD', 'Audio'),
        ('VID', 'Video'),
        ('LNK', 'Link'),
    )

    name = models.CharField(max_length=256)
    type = models.CharField(max_length=3, choices= MEDIA_TYPES)
    file = models.FileField()
    created = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tag, related_name="uploads")

    def __str__(self):
        return self.name
# blog/models.py
from django.db import models
from django.urls import reverse  

# Create your models here.  
class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey( 'auth.User', on_delete=models.CASCADE)
    record_date = models.DateTimeField(auto_now_add=True) 
    image = models.ImageField(upload_to='images/')
    body = models.TextField()
    
    class Meta:
        verbose_name = 'title'
        verbose_name_plural = 'titles'
        ordering = ['id']

    def __str__(self):
        return self.title
 
    def get_absolute_url(self): 
        return reverse('post_detail', args=[str(self.id)]) 

    def delete_image(self, *args, **kwargs):
        self.image.delete() 
        super().delete(*args, **kwargs)

    
 
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.utils import timezone
from django.utils.text import slugify

# Create your models here.
class CustomUser(AbstractUser):
    """
    Custom user model that extends the default Django User model.
    This can be used to add additional fields or methods in the future.
    """
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='pfp/', blank=True, null=True)
    facebook = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.username
    
class Post(models.Model):
    """
    Model representing a blog post.
    """
    CATEGORIES = (
        ('tech', 'Tech'),
        ('lifestyle', 'Lifestyle'),
        ('travel', 'Travel'),
        ('food', 'Food'),
        ('health', 'Health'),
    )
    title = models.CharField(max_length=200)
    content = models.TextField()
    slug = models.SlugField(max_length=200, unique=True,blank=True)
    image = models.ImageField(upload_to='posts/', blank=True, null=True)
    category = models.CharField(max_length=50, choices=CATEGORIES, default='tech')
    author = models.ForeignKey(settings.AUTH_USER_MODEL,related_name="posts", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    published_time = models.DateTimeField(blank=True, null=True)
    is_published = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        
        base_slug = slugify(self.title)
        slug = base_slug
        counter = 1
        while Post.objects.filter(slug=slug).exists():
            slug = f"{base_slug}-{counter}"
            counter += 1
        self.slug = slug
        
        if self.is_published and not self.published_time:
            self.published_time = timezone.now()
        super().save(*args, **kwargs)
        
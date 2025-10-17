from django.db import models

class Contacts(models.Model):
    full_name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Contact Message from {self.email}'
    
    class Meta:
        verbose_name = 'Contacts'
        verbose_name_plural = 'Contacts'

class Projects(models.Model):
    image = models.ImageField(upload_to='project-images/')
    title = models.CharField(max_length=100)
    text = models.CharField(max_length=255)
    skills = models.JSONField(default=list)
    live_demo = models.URLField(blank=True, null=True)
    code_link = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title} Projects'
    class Meta:
        verbose_name = 'Projects'
        verbose_name_plural = 'Projects'

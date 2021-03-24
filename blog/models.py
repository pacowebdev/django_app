from django.db import models


class Post(models.Model):
    CATEGORIES = [
        ('front', 'front'),
        ('back', 'back'),
        ('framework', 'framework')
    ]
    categorie = models.CharField(max_length=50, choices=CATEGORIES)
    title = models.CharField(max_length=50)
    content = models.TextField()
    image = models.FileField(upload_to='blog')

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    pseudo = models.CharField(max_length=100)
    content = models.CharField(max_length=200)
    date = models.DateField(auto_now=True)

    def __str__(self):
        return self.pseudo

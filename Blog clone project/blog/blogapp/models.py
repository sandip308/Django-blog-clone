from django.db import models
from django.utils import timezone
from django.urls import reverse

class Post(models.Model):
    author = models.ForeignKey('auth.User',on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    text = models.TextField()
    create_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True,null=True)

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"pk": self.pk})

    def approve_comments(self):
        return self.comments.filter(approved_comment=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey('blogapp.Post',on_delete=models.CASCADE,related_name='comments')
    author = models.CharField(max_length=100)
    text = models.TextField()
    create_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse("post_list")

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text

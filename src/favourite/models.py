from django.db import models
from account.models import User
from post.models import PostModel


class FavouriteModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favourites', default=1)
    post = models.ForeignKey(PostModel, on_delete=models.CASCADE, related_name='favourites')

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return f"{self.user.name} - {self.post.id}"
from django.db import models
from django.urls import reverse_lazy

# Create your models here.


class Photo(models.Model):
    image = models.ImageField(upload_to="%Y/%m/%d/orig")
    filtered_image = models.ImageField(upload_to="%Y/%m/%d/filtered")
    content = models.TextField(max_length=500,blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        url = reverse_lazy("detail", kwargs={"pk": self.pk})
        return url

    def delete(self, *args, **kwargs):
        self.image.delete()
        self.filtered_image.delete()
        super(Photo, self).delete(*args, **kwargs)


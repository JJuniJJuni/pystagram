from django.db import models
from django.core.urlresolvers import reverse_lazy
from django.conf import settings

# Create your models here.


class Photo(models.Model):  # 각 파일의 형식 지정
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    image = models.ImageField(upload_to="%Y/%m/%d/orig")
    filtered_image = models.ImageField(upload_to="%Y/%m/%d/filtered")
    content = models.TextField(max_length=500,blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):  # 클라이언트의 사진 pk를 넣고 반환
        url = reverse_lazy("detail", kwargs={"pk": self.pk})
        return url

    def delete(self, *args, **kwargs):
        self.image.delete()
        self.filtered_image.delete()
        super(Photo, self).delete(*args, **kwargs)


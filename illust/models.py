from django.db import models
from django.utils import timezone
# Create your models here.
class Design(models.Model):
    # テーブル名の定義
    class Meta:
        db_table = "design"

    # カラム(フィールド)の定義
    title = models.CharField(verbose_name="タイトル", max_length=100)
    date = models.DateTimeField(verbose_name="時間",default=timezone.now)
    descrption = models.TextField(verbose_name='説明',null=True, blank=True)

    file = models.FileField(verbose_name="ファイル",upload_to="illust/file")

    #TODO:次回、ファイルのMIME値を保管し、その値を元にpsファイル、aiファイルのサムネイルを自動生成させる
    """
    mime = models.TextField(verbose_name="MIMEタイプ")
    thumbnail = models.ImageField(verbose_name="サムネイル")
    """


    # TODO:後々ここに投稿者のユーザーIDなどのカラム(フィールド)を定義する。


    def __str__(self):
        return self.title

from django.shortcuts import render,redirect

## Create your views here.
#from django.shortcuts import render
from django.views import View

from .models import Design
from .forms import DesignForm


#ファイルのMIMEタイプを調べるためのpython-magicをインポート
import magic

#許可するMIMEタイプのリスト
ALLOWED_MIME    = [ "application/pdf" ]

"""
MIMEについて

https://developer.mozilla.org/ja/docs/Web/HTTP/Basics_of_HTTP/MIME_types/Common_types
https://experienceleague.adobe.com/docs/experience-manager-65/assets/administer/assets-formats.html?lang=ja

photoshopは"image/vnd.adobe.photoshop"もしくはmagicを使って調べる
"""


class illustView(View):

    def get(self, request, *args, **kwargs):

        #Designクラスを使用し、DBへアクセス、データ全件閲覧
        designs = Design.objects.all()

        button1     = "Prev"
        data        = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
        category    = "カテゴリ−１"
        category2   = "カテゴリ−2"
        category3   = "カテゴリ−3"

        context = {
                   "button1":button1,
                   "data":data,
                   "category1":category,
                   "category2": category2,
                   "category3": category3,

                   "designs":designs,

                   }

        return render(request,"illust/index.html",context)

    def post(self, request, *args, **kwargs):


        #フォームクラスに、request.POST、request.FILESを引数に
        form = DesignForm(request.POST, request.FILES)

        #python-magicで投稿されたファイルのMIMEタイプを調べる
        mime_type   = magic.from_buffer(request.FILES["file"].read(1024) , mime=True)

        if form.is_valid():
            print("バリデーションOK ")

            #MIMEタイプが許可したMIMEタイプのリストに含まれるかチェック。あれば保存
            if mime_type in ALLOWED_MIME:
                form.save()
            else:
                print("このファイルは許可されていません")
        else:
            print("バリデーションNG")

        return redirect("illust:index")

index   = illustView.as_view()

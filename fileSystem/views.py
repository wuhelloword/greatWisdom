from django.shortcuts import render
from django.views import View

# 类视图
class SaveFile(View):

    template_name = 'upload.html'

    def get(self, request, *args, **kwargs):

        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        file = request.files['file']
        print(file)
        # 处理文件的逻辑，比如保存文件到服务器
        return '文件上传成功'


class SendFile(View):
    pass


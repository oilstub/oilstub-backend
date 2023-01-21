from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import View


class UploadOilStubDataView(View):
    template_name = ''

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated and request.user.isAdmin:
            return HttpResponseRedirect(reverse('home'))
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        upload_file = request.FILES.GET('upload_file')
        if not upload_file:
            return HttpResponseRedirect(reverse('support:upload_users'))


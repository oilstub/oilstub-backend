from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import View
from rest_framework import status
from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from oilandgasdata.serializers import (
    UploadFileSerializer,
    SearchSerializer
)


class UploadOilStubDataView(View):
    template_name = 'upload_files.html'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated and request.user.isAdmin:
            return HttpResponseRedirect(reverse('home'))
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        upload_file = request.FILES.get('upload_file')
        if not upload_file:
            return HttpResponseRedirect(reverse('oilandgasdata:upload_files'))
        serializer = UploadFileSerializer(data=request.FILES)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return HttpResponseRedirect(reverse('home'))


class SearchViewSet(APIView):
    permission_classes = []

    def post(self, request, *args, **kwargs):
        serializer = SearchSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            response = serializer.save()
            return Response(response, status=status.HTTP_200_OK)
        return Response({"message": 'Invalid search term'}, status=status.HTTP_400_BAD_REQUEST)

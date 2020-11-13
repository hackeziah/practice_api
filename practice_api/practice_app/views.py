from django.shortcuts import render
from practice_app.serializers import BlogSerializer, AuthorSerializer, EntrySerializer
from practice_app.models import Blog, Author, Entry
from rest_framework import generics  # METHOD 1
from rest_framework.decorators import api_view  # METHOD 2
from django.http import HttpResponse
from django.http import JsonResponse
from rest_framework import viewsets  # for model sets

from rest_framework.parsers import JSONParser, ParseError
# Lets build API views

from rest_framework.generics import (  # METHOD 1
    ListAPIView,  # for read only
    CreateAPIView,  # create POST
    RetrieveAPIView,  # get
    ListCreateAPIView,  # Update Create
    RetrieveUpdateAPIView,  # RetrieveUpdate
    DestroyAPIView,  # Delete
    UpdateAPIView  # Update
)


class Blog(generics.ListCreateAPIView):  # METHOD 1
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer


class EntryViewSet(viewsets.ModelViewSet):
    serializer_class = EntrySerializer

    def get_queryset(self):
        entries = Entry.objects.all()
        return entries

        # METHOD 2


@api_view(['GET', 'POST'])
def author_list(request):
    if request.method == 'GET':
        authors = Author.objects.all()
        name = request.GET.get('name', None)
        if name is not None:
            authors = authors.filter(name__icontains=name)
        author_serializer = AuthorSerializer(authors, many=True)
        return JsonResponse(author_serializer.data, safe=False)

    # elif request.method == 'POST':
    #     mydata = request.data
    #     data = JSONParser().parse(mydata)
    #     author_serializer = AuthorSerializer(data=data)
    #     if author_serializer.is_valid():
    #         author_serializer.save()
    #         return JsonResponse(author_serializer.data, status=status.HTTP_201_CREATED)
    #     return JsonResponse(author_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['GET', 'PUT', 'DELETE'])
# def author_detail(request, pk):
#     try:
#         authors = Author.objects.get(pk=pk)
#     except Author.DoesNotExist:
#         return JsonResponse({'message': 'The Author does not exist'}, status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET':
#         author_serializer = AuthorSerializer(authors)
#         return JsonReponse(author_serializer.data)

#     elif request.method == 'PUT':
#         author_data = JSONParser().parse(request)
#         author_serializer = AuthorSerializer(authors, data=author_data)
#         if author_serializer.is_valid:
#             author_serializer.save()
#             return JsonResponse(author_serializer.data)
#         return JsonResponse(author_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == 'DELETE':
#         authors.delete()
#         return JsonResponse({'message': 'Author was deleted successfully'}, status=status.HTTP_204_NO_CONTENT)

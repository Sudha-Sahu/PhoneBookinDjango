from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from .models import Contact
from .serializer import ContactSerializer


class ContactView(APIView):
    def post(self, request):
        new_contct = request.data
        serializer = ContactSerializer(data=new_contct)
        if not serializer.is_valid():
            return Response({'Error': "data is not validated", 'Code': 404})
        serializer.save()
        return Response({'Message': 'New Contact Added', 'Code': 200})

    def get(self, request, pk=None):
        if pk:
            contct = Contact.objects.get(id=pk)
            serializer = ContactSerializer(contct, many=False)
            return Response({'Data': serializer.data, 'Code': 200})
        contct = Contact.objects.all()
        serializer = ContactSerializer(contct, many=True)
        return Response({'Data': serializer.data, 'Code': 200})

    def delete(self, request, pk):
        data = Contact.objects.get(id=pk)
        if not data:
            return Response({'error': 'data not found', 'code': 404})
        data.delete()
        return Response({'Message': 'Data Deleted', 'Code': 200})

    def put(self, request, pk):
        contct = Contact.objects.get(id=pk)
        if not contct:
            return Response({'Error': "data not found", 'Code': 404})
        serializer = ContactSerializer(instance=contct, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
        return Response({'Message': 'Data Updated', 'Code': 200})


#
# @api_view(['GET'])
# def get_all_contact(request):
#     contct = Contact.objects.all()
#     serializer = ContactSerializer(contct, many=True)
#     return Response(serializer.data)
#
#
# @api_view(['GET'])
# def get_one_contact(request, pk):
#     contct = Contact.objects.get(id=pk)
#     serializer = ContactSerializer(contct, many=False)
#     return Response(serializer.data)
#
#
# @api_view(['POST'])
# def create_contact(request):
#     serializer = ContactSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#     return Response(serializer.data)
#
#
# @api_view(['PUT'])
# def update_contact(request, pk):
#     contct = Contact.objects.get(id=pk)
#     serializer = ContactSerializer(instance=contct, data=request.data, partial=True)
#     if serializer.is_valid():
#         serializer.save()
#     return Response(serializer.data)
#
#
# @api_view(['DELETE'])
# def delete_contact(request, pk):
#     contact = Contact.objects.get(id=pk)
#     if contact:
#         contact.delete()
#     return Response('deleted')

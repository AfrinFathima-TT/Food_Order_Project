from django.shortcuts import render,get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from Foodapp.models import FoodDb,OrderDb
from Foodapp.serializers import FoodSerializer,OrderSerializer

# Create your views here.
class FoodListCreateView(APIView):
    def get(self,request):
        qs = FoodDb.objects.all()    

        seriallizer_instance = FoodSerializer(qs,many=True)  

        return Response(data=seriallizer_instance.data)
    
    def post(self,request):
        form_data = request.data   

        serializer_instance = FoodSerializer(data=form_data)

        if  serializer_instance.is_valid():

            actual_data = serializer_instance.validated_data

            FoodDb.objects.create(**actual_data)

            return Response(data={"message" : "Food added successfully"})
        else:
            return Response(data={"errors" : serializer_instance.errors})


class FoodRetrieveUpdateDeleteView(APIView):
    def get(self,request,pk):

        qs = FoodDb.objects.get(id = pk)

        serializer_instance = FoodSerializer(qs)

        return Response(data = serializer_instance.data)

    def put(self,request,pk):
        form_data = request.data     #get data from client

        serializer_instance = FoodSerializer(data = form_data)
        if serializer_instance.is_valid():

            actual_data = serializer_instance.validated_data

            FoodDb.objects.filter(id = pk).update(**actual_data)

            return Response(data=serializer_instance.data)
        else:

            return Response(data=serializer_instance.errors)

    def delete(self,request,pk):

        FoodDb.objects.filter(id = pk).delete()

        return Response({
            "Message" : "Food deleted successfully...!"
        })

class OrderListCreateView(APIView):
    def get(self,request):
        qs = OrderDb.objects.all()
        submission_instance = OrderSerializer(qs,many=True)
        return Response(data=submission_instance.data)


    def post(self,request):
        form_data = request.data
        submission_instance = OrderSerializer(data = form_data)
        if submission_instance.is_valid():
            actual_data = submission_instance.validated_data

            OrderDb.objects.create(**actual_data)

            return Response(data ={"Message" : "food ordered  successfully...!"})
        else:
            return Response(data = {"eroors":submission_instance.errors})

class OrderRetrieveUpdateDeleteView(APIView):
    def get(self,request,pk):


        qs = get_object_or_404(OrderDb,id=pk)
        serializer_instance = OrderSerializer(qs)
        return Response(data=serializer_instance.data)

    def put(self,request,pk):

        form_data = request.data
        serializer_instance = OrderSerializer(data = form_data)
        if serializer_instance.is_valid():
            actual_data = serializer_instance.validated_data
            OrderDb.objects.filter(id = pk).update(**actual_data)
            return Response(data=serializer_instance.data)

        else:
            return Response(data=serializer_instance.errors)

    def delete(self,request,pk):
        OrderDb.objects.filter(id = pk).delete()

        return Response({"Message" : "order cancelled successfully"})

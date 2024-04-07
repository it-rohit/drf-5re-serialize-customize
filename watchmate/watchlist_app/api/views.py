from rest_framework.decorators import APIView
from rest_framework.response import Response
from rest_framework import status




from ..models import Watchlist,Streamplatform
from .serializer import WatchlistSerializer,StreamplatformSerializer


###creating view and post for Streamplatform
class Streamplatform_list(APIView):
    def get(self,request):
        platform = Streamplatform.objects.all()
        serializer1 = StreamplatformSerializer(platform, many=True)
        return Response (serializer1.data, status=status.HTTP_200_OK)
    
    def post (self,request):
        data1 =request.data
        serializer1 =StreamplatformSerializer(data = data1)
        if serializer1.is_valid():
            serializer1.save()
            return Response (serializer1.data,status=status.HTTP_201_CREATED)
        else:
            return Response (serializer1.errors,status=status.HTTP_400_BAD_REQUEST)

class Streamplatform_update(APIView):
    def get(self,request,pk):
        try:
            platform =Streamplatform.objects.get(pk=pk)
        except Streamplatform.DoesNotExist:
            return Response ({"mag":"Streamplatform not found"})
        
        sreializer1 = StreamplatformSerializer(platform)
        return Response(sreializer1.data,status=status.HTTP_200_OK)
    
    def put(self,request,pk):
        platform =Streamplatform.objects.get(pk=pk)
        data1 = request.data
        serializer1 =StreamplatformSerializer(data=data1,instance=platform)
        if serializer1.is_valid():
            serializer1.save()
            return Response (serializer1.data,status=status.HTTP_200_OK)
        else:
            return Response (serializer1.errors,status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self,request,pk):
        platform =Streamplatform.objects.get(pk=pk)
        platform.delete()
        return Response ({"msg":" sucessfully deleted"},status=status.HTTP_204_NO_CONTENT)

            


class Watchlist_View_Create(APIView):
    def get(self,request):
        movie=Watchlist.objects.all()
        serializer1=WatchlistSerializer(movie, many=True)
        return Response (serializer1.data,status=status.HTTP_200_OK)
    def post (self,request):
        data1=request.data
        serializer1 = WatchlistSerializer(data=data1)
        if serializer1.is_valid():
            serializer1.save()
            return Response(serializer1.data,status=status.HTTP_201_CREATED)
        else:
            print("hai")
            return Response(serializer1.errors,status=status.HTTP_400_BAD_REQUEST)
        
###update delete
class Watchlist_Update_Delete(APIView):
    def get(self,request,pk):
        try:

            movie = Watchlist.objects.get(pk=pk)
        except Watchlist.DoesNotExist:
            return Response ({"msg":"not found"},status = status.HTTP_404_NOT_FOUND)

        serializer1 = WatchlistSerializer(movie)                
        return Response (serializer1.data,status=status.HTTP_200_OK)
    
    def put (self,request,pk):

        movie = Watchlist.objects.get(pk=pk)
        data1=request.data
        serializer1=WatchlistSerializer(instance=movie,data=data1)
        if serializer1.is_valid():
            serializer1.save()
            return Response (serializer1.data, status=status.HTTP_200_OK)
        else:
            return Response (serializer1.errors,status=status.HTTP_400_BAD_REQUEST)
            
    def delete (self,request,pk):
        movie= Watchlist.objects.get(pk=pk)
        movie.delete()
        return Response ({"msg":" sucessfully deleted"},status=status.HTTP_204_NO_CONTENT)
    


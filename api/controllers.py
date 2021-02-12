from api.models import Breed, Dog
from api.serializers import BreedSerializer, DogSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Dog routes


class DogDetail(APIView):

    def get_object(self, pk):
        return Dog.objects.get(pk=pk)

    def get(self, request, pk, format=None):
        dog = self.get_object(pk)
        serializer = DogSerializer(dog)
        return Response(serializer.data)
    # def get(self, request, format=None):
    #     dogs = Dog.objects.all()
    #     # dogs = Dog.objects.all().filter(name = request.name)
    #     json_data = serializers.serialize('json', dogs)
    #     content = {'dogs': json_data}
    #     return HttpResponse(json_data, content_type='json')


class DogList(APIView):

    def get(self, request, format=None):
        dogs = Dog.objects.all()
        # dogs = Dog.objects.all().filter(name = request.name)
        serializer = DogSerializer(dogs)
        return Response(serializer.data)

    # def post(self, request, *args, **kwargs):
    #     print 'REQUEST DATA'
    #     print str(request.data)

    #     name = request.data.get('name')
    #     age = int(request.data.get('age'))
    #     breed = request.data.get('breed')
    #     gender = request.data.get('gender')
    #     color = request.data.get('color')
    #     favoriteFood = request.data.get('favoriteFood')
    #     favoriteToy = request.data.get('favoriteToy')

    #     requestor = request.META['REMOTE_ADDR']

    #     newDog = Dog(
    #         name=name,
    #         age=age,
    #         breed=breed_id,
    #         color=color,
    #         favoriteFood=favoriteFood,
    #         favoriteToy=favoriteToy,
    #         requestor=requestor
    #     )

    #     try:
    #         newDog.clean_fields()
    #     except ValidationError as e:
    #         # print e
    #         return Response({'success': False, 'error': e}, status=status.HTTP_400_BAD_REQUEST)

    #     newDog.save()
    #     print 'New Event Logged from: ' + requestor
    #     return Response({'success': True}, status=status.HTTP_200_OK)

    # Breed routes


# class BreedDetail(APIView):
    # permission_classes = (AllowAny,)
    # parser_classes = (parsers.JSONParser, parsers.FormParser)
    # renderer_classes = (renderers.JSONRenderer, )

    # def get(self, request, pk, format=None):
    #     # breeds = Breed.objects.all()
    #     breeds = Breed.objects.all().filter(pk=request.pk)
    #     json_data = serializers.serialize('json', breeds)
    #     content = {'breeds': json_data}
    #     return HttpResponse(json_data, content_type='json')

    # class BreedList(APIView):
    # permission_classes = (AllowAny,)
    # parser_classes = (parsers.JSONParser, parsers.FormParser)
    # renderer_classes = (renderers.JSONRenderer, )

    # def get(self, request, format=None):
    #     breeds = Breed.objects.all()
    #     json_data = serializers.serialize('json', breeds)
    #     content = {'breeds': json_data}
    #     return HttpResponse(json_data, content_type='json')

    # def post(self, request, *args, **kwargs):
    #     print 'REQUEST DATA'
    #     print str(request.data)

    #     name = request.data.get('name')
    #     size = request.data.get('size')
    #     friendliness = int(request.data.get('friendliness'))
    #     trainability = int(request.data.get('trainability'))
    #     sheddingamount = int(request.data.get('sheddingamount'))
    #     exerciseneeds = int(request.data.get('exerciseneeds'))

    #     requestor = request.META['REMOTE_ADDR']

    #     newBreed = Breed(
    #         name=name,
    #         size=size,
    #         friendliness=friendliness,
    #         trainability=trainability,
    #         sheddingamount=sheddingamount,
    #         exerciseneeds=exerciseneeds
    #     )

    #     try:
    #         newBreed.clean_fields()
    #     except ValidationError as e:
    #         print e
    #         return Response({'success': False, 'error': e}, status=status.HTTP_400_BAD_REQUEST)

    #     newBreed.save()
    #     print 'New Event Logged from: ' + requestor
    #     return Response({'success': True}, status=status.HTTP_200_OK)

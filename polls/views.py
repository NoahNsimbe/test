from polls.models import Candidates
from rest_framework import viewsets, serializers


class SerializerClass(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Candidates
        fields = ('url', 'id', 'firstName', 'lastName', 'image')


class CandidatesViewSet(viewsets.ModelViewSet):
    serializer_class = SerializerClass
    queryset = Candidates.objects.all()

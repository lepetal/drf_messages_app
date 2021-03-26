from django.shortcuts import render
from rest_framework import generics, viewsets, status
from rest_framework.settings import api_settings
from msg.serializers import MessageDetailSerializer, MessageListSerializer
from rest_framework_csv.parsers import CSVParser
from rest_framework_csv.renderers import CSVRenderer
from msg.models import Message
from msg.permissions import IsOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
class MessageCreateView(LoginRequiredMixin, generics.CreateAPIView):
    serializer_class = MessageDetailSerializer


class MessageListView(generics.ListAPIView):
    serializer_class = MessageListSerializer
    queryset = Message.objects.all()
    permission_classes = (IsAuthenticated, )

class MessageDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = MessageDetailSerializer
    queryset = Message.objects.all()
    permission_classes = (IsOwnerOrReadOnly, )

class MessageViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows talks to be viewed or edited.
    """
    queryset = Message.objects.all()
    renderer_classes = (CSVRenderer,) + tuple(api_settings.DEFAULT_RENDERER_CLASSES)
    serializer_class = MessageListSerializer

    def get_renderer_context(self):
        context = super(MessageViewSet, self).get_renderer_context()
        context['header'] = (
            self.request.GET['fields'].split(',')
            if 'fields' in self.request.GET else None)
        return context
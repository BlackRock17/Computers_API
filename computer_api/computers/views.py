from rest_framework import generics
from .models import Computer
from .serializers import ComputerSerializer


class ComputerList(generics.ListAPIView):
    serializer_class = ComputerSerializer

    def get_queryset(self):
        queryset = Computer.objects.all()
        processor = self.request.query_params.get('processor')
        gpu = self.request.query_params.get('gpu')
        motherboard = self.request.query_params.get('motherboard')
        ram = self.request.query_params.get('ram')

        if processor:
            queryset = queryset.filter(processor__icontains=processor)
        if gpu:
            queryset = queryset.filter(gpu__icontains=gpu)
        if motherboard:
            queryset = queryset.filter(motherboard__icontains=motherboard)
        if ram:
            queryset = queryset.filter(ram__iexact=ram)

        return queryset



        # filters = Q()
        # if processor:
        #     filters |= Q(processor__icontains=processor)
        # if gpu:
        #     filters |= Q(gpu__icontains=gpu)
        # if motherboard:
        #     filters |= Q(motherboard__icontains=motherboard)
        # if ram:
        #     filters |= Q(ram__icontains=ram)
        #
        # queryset = queryset.filter(filters)
        #
        # return queryset

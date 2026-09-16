from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Canvas
from .serializers import PortSerializer

@api_view(['GET'])
def get_canvas(request):
    canvas = Canvas.objects.all()

    nodes = {}

    for item in canvas:
        if item.node not in nodes:
            nodes[item.node] = []
        
        nodes[item.node].append(PortSerializer(item).data)

    response = [
        {
            'node': node,
            'ports': ports
        }
        for node, ports in nodes.items()
    ]

    return Response(response)

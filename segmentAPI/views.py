from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Canvas
from .serializers import PortSerializer
from .services import segment_formula

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

@api_view(['GET'])
def get_segments(request):
    canvas = Canvas.objects.all()
    segment_count = 0
    formula_list = []

    for item in canvas:
        if item.value is None:
            continue
        source_result, source_formula = segment_formula(item)
        if source_result is None and source_formula is None:
            continue
        else:
            formula = item.port + " - (" + source_formula + ")"
            result = item.value - source_result
            formula_list.append([formula,result])
            segment_count += 1

    result = {
        'segment_count':segment_count,
        'segments':[
            {
                'formula': formula,
                'result': result
            }
            for formula, result in formula_list
        ]
    }     

    return Response(result)
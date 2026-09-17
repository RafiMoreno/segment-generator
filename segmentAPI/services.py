from .models import Canvas

def segment_formula(port: Canvas):
    node_count = Canvas.objects.filter(node=port.node).count()
    if port.source is None and node_count <=1:
        return None, None
    elif port.source is None and node_count > 1:
        all_ports_in_node = Canvas.objects.filter(node=port.node)
        sources_formula = ""
        sources_total_value = 0
        for item in all_ports_in_node:
            if port.port != item.port:
                if sources_formula != "":
                    sources_formula += " + "
                if item.value is not None:
                    source_port_value = item.value
                    source_port_name = item.port
                else:
                    source_port_value, source_port_name = segment_formula(item)
                sources_total_value += source_port_value
                sources_formula += source_port_name
        return sources_total_value, sources_formula
    elif port.source:
        if port.source.value is None:
            return segment_formula(port.source)
        else:
            return port.source.value, port.source.port
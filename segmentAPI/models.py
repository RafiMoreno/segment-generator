from django.db import models

class Canvas(models.Model):
    node = models.TextField(max_length=100)
    port = models.TextField(max_length=100)
    value = models.CharField(max_length=100, null=True)
    source = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, related_name='source_port')
    target = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, related_name='target_port')


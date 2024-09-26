from rest_framework import serializers
class CarSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    model = serializers.CharField(max_length=50)
    price = serializers.IntegerField()
    year = serializers.IntegerField()
    created = serializers.DateTimeField()
    updated = serializers.DateTimeField()

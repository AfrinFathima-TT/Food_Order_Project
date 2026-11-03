from rest_framework import serializers
from Foodapp.models import FoodDb


class FoodSerializer(serializers.Serializer):
    
    food_name = serializers.CharField(max_length=100)
    category = serializers.CharField(max_length=100)
    description = serializers.CharField()
    price = serializers.DecimalField(max_digits=8, decimal_places=2)
    quantity = serializers.IntegerField()
    restaurant_name = serializers.CharField(max_length=100)
    is_available = serializers.BooleanField()

class OrderSerializer(serializers.Serializer):

    customer_name = serializers.CharField(max_length=100)
    customer_email = serializers.EmailField()
    mobile = serializers.CharField(max_length=15)
    food_id = serializers.IntegerField()
    food_name = serializers.CharField(max_length=100)
    quantity = serializers.IntegerField()
    total_amount = serializers.DecimalField(max_digits=8, decimal_places=2)
    order_status = serializers.CharField(max_length=50)
    ordered_at = serializers.DateTimeField(read_only=True)


    def validate(self, validate_data):

        food_id = validate_data.get("food_id")

        if not FoodDb.objects.filter(id=food_id).exists():
            raise serializers.ValidationError("Food does not exist...!")

        return validate_data
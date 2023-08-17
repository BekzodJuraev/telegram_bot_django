from rest_framework import serializers
from .models import Add_item, OrderItem, Bot

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['add_item', 'count']

class BotSerializer(serializers.ModelSerializer):
    related_diaries = OrderItemSerializer(many=True)

    class Meta:
        model = Bot
        fields = ['id_user', 'name', 'price', 'comment', 'adress', 'phone', 'order_choice','latitude','longitude','related_diaries']

    def create(self, validated_data):
        related_diaries_data = validated_data.pop('related_diaries')
        bot = Bot.objects.create(**validated_data)
        for diary_data in related_diaries_data:
            add_item = diary_data.pop('add_item')
            count = diary_data.pop('count')
            OrderItem.objects.create(order=bot, add_item=add_item, count=count, **diary_data)
        return bot
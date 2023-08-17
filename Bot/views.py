from django.forms import model_to_dict
from django.shortcuts import render
from aiogram import Bot, Dispatcher, executor, types
from .models import Add_item,Bot,OrderItem
from rest_framework.response import Response
from rest_framework.views import APIView
import json
import telegram
import requests
from .serializers import BotSerializer
from rest_framework import status

BOT_TOKEN="5550655096:AAEshSjOtMdaYWugp7Nb0Eej8Qq9RMemdT8"

bot_telegram = telegram.Bot(token=BOT_TOKEN)

class AboutAPIView(APIView):
    def get(self, request):
        bots = Bot.objects.all()
        serializer = BotSerializer(bots, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


    def post(self, request):
        serializer = BotSerializer(data=request.data)

        if serializer.is_valid():
            ##   f.write(str(serializer.initial_data) + '\n')


            chat_id = serializer.validated_data['id_user']
            price=serializer.validated_data['price']
            comment=serializer.validated_data['comment']
            adress=serializer.validated_data['adress']
            phone=serializer.validated_data['phone']
            OrderItem=serializer.validated_data['related_diaries']
            order_option=serializer.validated_data['order_choice']
            longitude=serializer.validated_data['longitude']
            latitude=serializer.validated_data['latitude']
            empty=""
            Bekzod="531080457"


            for item in OrderItem:
                add_item=str(item['add_item'])
                count=str(item['count'])
                empty+=f'{add_item}:{count}\n'








            if adress=="":
                text = f'Ваши заказы\n{empty}цена={price}сум\nкомментария={comment}\nномер={phone}\n{order_option}'
            else:
                text = f'Ваши заказы\n{empty}цена={price}сум\nкомментария={comment}\nадрес={adress}\nномер={phone}\n{order_option}'


            bot = serializer.save()
            #keyboard = [[telegram.KeyboardButton(text="Share Location", request_location=True)]]
            #reply_markup = telegram.ReplyKeyboardMarkup(keyboard)
            bot_telegram.sendMessage(chat_id=chat_id,text=text)
            bot_telegram.send_location(chat_id=chat_id,longitude=longitude,latitude=latitude)
            bot_telegram.sendMessage(chat_id=Bekzod, text=text)
            bot_telegram.send_location(chat_id=Bekzod, longitude=longitude, latitude=latitude)






            return Response({'bot': serializer.data}, status=status.HTTP_201_CREATED)
        if not serializer.is_valid():
            print(serializer.data)
            print(serializer.errors)

            with open('invalid_data.txt', 'a') as f:
                f.write(str(serializer.initial_data) + '\n')
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)








def about_view(request):

    items=Add_item.objects.all()
    bots = Bot.objects.prefetch_related('related_diaries').all()




    return render(request,"Bot/index.html",
                  {'items':items,
                   'bots':bots,})

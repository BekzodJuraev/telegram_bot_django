from django.contrib import admin
from .models import Add_item,Bot,OrderItem
# Register your models here.



class Add_item_admin(admin.ModelAdmin):
    list_display = ['name', 'price', 'created']

class DiaryInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['add_item']
    list_display = ['add_item', 'count']

class Bot_admin(admin.ModelAdmin):
    inlines = [DiaryInline]
    list_display = ['name', 'price', 'id_user', 'comment', 'created', 'adress', 'phone', 'order_choice','get_order_info'
           ]
    search_fields = ['name', 'comment']

    def get_order_info(self, obj):
        order_count =  ', '.join([str(order.count) for order in obj.related_diaries.all()])
        order_items = ', '.join([str(order.add_item) for order in obj.related_diaries.all()])


        return f"{order_items}:{order_count}"

    get_order_info.short_description = 'Order Info'

    #get_order_items.short_description = 'Order Items'













class OrderItem_admin(admin.ModelAdmin):
    list_display = ['add_item', 'count']
    readonly_fields = ['order']
    raw_id_fields = ['add_item']


admin.site.register(Add_item, Add_item_admin)
admin.site.register(OrderItem, OrderItem_admin)
admin.site.register(Bot, Bot_admin)



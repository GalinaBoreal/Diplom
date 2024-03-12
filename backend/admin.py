from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from backend.models import User, Shop, Category, Product, ProductInfo, Parameter, ProductParameter, Order, OrderItem, \
    Contact, ConfirmEmailToken


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    """
    Панель управления пользователями
    """
    model = User

    fieldsets = (
        (None, {'fields': ('email', 'password', 'type')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'company', 'position')}),
        ('Permissions', {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    list_display = ('email', 'first_name', 'last_name', 'is_staff')


@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    # pass
    model = Shop
    fieldsets = (
        (None, {'fields': ('name', 'state')}),
        ('Advanced options', {'classes': ('collapse',), 'fields': ('url', 'user')}),
    )
    list_display = ('name', 'state', 'url')

    # list_display = ('id', 'name', 'url', 'user', 'state')
    # list_filter = ('state', 'name', 'user')
    # search_fields = ('name', )


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    # pass
    model = Category
    #
    # list_display = ('id', 'name')
    # list_filter = ('name', )
    # search_fields = ('name', )


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    # pass
    model = Product
    # list_display = ['id', 'name', 'rrc', 'category']
    # filter_horizontal = ['shops']

    # list_display = ('id', 'name', 'category_id')
    # list_filter = ('name', )
    # search_fields = ('name',)
    # list_display = ('name', 'category', 'shop', 'quantity', 'price', 'price_rrc')
    # list_filter = ('shop', 'category')
    # fields = (('shop', 'category'), 'name', 'model', 'external_id', 'quantity', ('price', 'price_rrc'))
    # readonly_fields = ('category', 'shop')


@admin.register(ProductInfo)
class ProductInfoAdmin(admin.ModelAdmin):
    model = ProductInfo

    fieldsets = (
        (None, {'fields': ('product', 'model', 'external_id', 'quantity')}),
        ('Prices', {'fields': ('price', 'price_rrc')}),
    )
    list_display = ('product', 'external_id', 'price', 'price_rrc', 'quantity')
    ordering = ('external_id',)


@admin.register(Parameter)
class ParameterAdmin(admin.ModelAdmin):
    pass


@admin.register(ProductParameter)  #
class ProductParameterAdmin(admin.ModelAdmin):
    pass

@admin.register(Order)  #
class OrderAdmin(admin.ModelAdmin):
    # pass
    model = Order
    fields = ('user', 'state', 'contact')
    list_display = ('id', 'user', 'state', 'dt')
    ordering = ('dt',)

@admin.register(OrderItem)  #
class OrderItemAdmin(admin.ModelAdmin):
    pass

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'city', 'phone')

@admin.register(ConfirmEmailToken)
class ConfirmEmailTokenAdmin(admin.ModelAdmin):
    list_display = ('user', 'key', 'created_at',)

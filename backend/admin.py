from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from easy_thumbnails.fields import ThumbnailerField
from easy_thumbnails.widgets import ImageClearableFileInput

from backend.models import User, Shop, Category, Product, ProductInfo, Parameter, ProductParameter, Order, OrderItem, \
    Contact, ConfirmEmailToken, Image


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


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    model = Category
    list_display = ['id', 'name']


# @admin.register(Image)
class ImageInLine(admin.TabularInline):
    fk_name = 'product'
    model = Image
    list_displey = ['image']

    formfield_overrides = {
        ThumbnailerField: {'widget': ImageClearableFileInput},
    }

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    model = Product
    list_display = ['name', 'id', 'category_id']
    inlines = [ImageInLine]


@admin.register(ProductInfo)
class ProductInfoAdmin(admin.ModelAdmin):
    model = ProductInfo

    formfield_overrides = {
        ThumbnailerField: {'widget': ImageClearableFileInput},
    }

    fieldsets = (
        (None, {'fields': ('product', 'model', 'external_id', 'quantity')}),
        ('Prices', {'fields': ('price', 'price_rrc')}),
    )
    list_display = ('product', 'id', 'external_id', 'price', 'price_rrc', 'quantity')
    ordering = ('external_id',)


@admin.register(Parameter)
class ParameterAdmin(admin.ModelAdmin):
    pass


@admin.register(ProductParameter)  #
class ProductParameterAdmin(admin.ModelAdmin):
    model = ProductParameter
    list_display = ['product_info', 'value']


@admin.register(Order)  #
class OrderAdmin(admin.ModelAdmin):
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

# @admin.register(PartnerUpdate)
# class PartnerUpdateAdmin(PartnerUpdate):

# @admin.action(description="Import price")
# def make_published(PartnerUpdate, request, queryset):
#     queryset.update(status="p")

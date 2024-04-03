from celery import shared_task
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from requests import get
from yaml import load as load_yaml, Loader

from backend.models import Category, Parameter, ProductParameter, Product, ProductInfo, Shop

@shared_task
def send_email_task(subject, message, to):
    """
    A Celery task to send an email.
    """
    msg = EmailMultiAlternatives(
        # title:
        subject,
        # message:
        message,
        # from:
        settings.EMAIL_HOST_USER,
        # to:
        to
    )
    msg.send()


@shared_task()
def update_price(url, user_id):
    stream = get(url).content

    data = load_yaml(stream, Loader=Loader)

    shop, _ = Shop.objects.get_or_create(name=data['shop'], user_id=user_id)
    for category in data['categories']:
        category_object, _ = Category.objects.get_or_create(id=category['id'], name=category['name'])
        category_object.shops.add(shop.id)
        category_object.save()
    ProductInfo.objects.filter(shop_id=shop.id).delete()
    for item in data['goods']:
        product, _ = Product.objects.get_or_create(name=item['name'], category_id=item['category'])

        product_info = ProductInfo.objects.create(product_id=product.id,
                                                  external_id=item['id'],
                                                  model=item['model'],
                                                  price=item['price'],
                                                  price_rrc=item['price_rrc'],
                                                  quantity=item['quantity'],
                                                  shop_id=shop.id)
        for name, value in item['parameters'].items():
            parameter_object, _ = Parameter.objects.get_or_create(name=name)
            ProductParameter.objects.create(product_info_id=product_info.id,
                                            parameter_id=parameter_object.id,
                                            value=value)
    # return JsonResponse({'Status': True})
    # EncodeError(TypeError('Object of type JsonResponse is not JSON serializable'))

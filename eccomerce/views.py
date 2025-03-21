import logging, json
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from users.models import Payment, PaymentWaiting
from products.models import Cart, Order, Product
logger = logging.getLogger(__name__)

@csrf_exempt
def processPayment(request):
    logger.info("payment returned")
    callback_data = json.loads(request.body)
    response = callback_data['response']
    if callback_data["status"]:
        # create a record of transactions just incase
        Payment.objects.create(
            code = response['MpesaReceiptNumber'],
            amount = response["Amount"]
        )
        # fetch payment awaiting
        try:
            paymentwaiting = PaymentWaiting.objects.get(phone_number = response["Phone"])
            paymentExist = True
        except PaymentWaiting.DoesNotExist:
            paymentExist = False
        if paymentExist:
            username = paymentwaiting.username
            cartObject = Cart.objects.filter(username = username)
            # loop through cart create object order of them
            if cartObject.exists():
                for order in cartObject:
                    Order.objects.get_or_create(
                        title = order.title,
                        price = order.price,
                        item = order.quantity,
                        image_url = order.image,
                        status =  "Pending",
                        username = username,
                        productId = order.itemId
                    )
                    # update number bought
                    product = Product.objects.get(id = order.itemId)
                    product.number_bought = product.number_bought + order.quantity
                    product.save()
                    # delete it from cart
                    order.delete()
            paymentwaiting.delete()
            print("done")
    response_data = {"statement": "Payment statement received"}
    return JsonResponse(response_data, status=200)
from .models import Cart , CartDetail



# get or create
def get_cart_data(request):
    if request.user.is_authenticated:
        cart , created = Cart.objects.get_or_create(user=request.user,status ='in-progress')
        cart_detail = CartDetail.objects.filter(cart=cart)
        return {'cart_data':cart ,'cart_detail_data':cart_detail}
    
    else :
        return{}
    
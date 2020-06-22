import datetime
from django.conf import settings

def send_context(request):
    current_datetime=datetime.date.today()
    day=current_datetime.strftime("%A")
    sidebar_url=''
    can_use_cart='False'
    system_access='False'

    cart_type=request.session.get(settings.CART_TYPE_SESSION_ID)
    if cart_type==None or cart_type=='':
        if request.user.is_authenticated and request.user.profile.account_type in ['SA','SU'] :
            cart_type='Purchase'
        else:
            cart_type='Sale'
    
    if request.user.is_authenticated:
        sidebar_url=f'sidebar/{request.user.profile.account_type}.html'
        
        if request.user.profile.account_type in ['SA','SU']:
            system_access="True"

        if request.user.profile.account_type in ['SA','SU','CA']:
            can_use_cart='True'

    output = f'{current_datetime} - {day}'
    return { 'date':output,
            'sidebar_url':sidebar_url,
            'cart_type':cart_type,
            'can_use_cart':can_use_cart,
            'system_access':system_access,
        }
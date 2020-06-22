import re
from django.conf import settings
from django.shortcuts import redirect
from django.urls import resolve
from django.contrib import messages
from django.http import HttpResponseForbidden

# SA_VIEWS=['dashboard',
#          'product_add','product_list','product_update','product_detail','product_delete',
#          'supplier_add','supplier_list','supplier_update','supplier_detail','supplier_delete',
#          'project_add','project_list','project_update','project_detail','project_delete',
#          'company_add','company_list','company_update','company_detail','company_delete',
#          'cart_view',
#          'order_confirm_quotation','order_approve_quotation','order_confirm','order_payment_confirm',
#          'add_dn_cn','confirm_purchase','order_list','order_detail',
#          'register','update','password_change','logout'
#          ]
SU_VIEWS = ['dashboard', 'inventory',
            'product_add', 'product_list', 'product_update', 'product_detail', 'product_delete',
            'supplier_add', 'supplier_list', 'supplier_update', 'supplier_detail', 'supplier_delete',
            'project_add', 'project_list', 'project_update', 'project_detail', 'project_delete',
            'company_add', 'company_list', 'company_update', 'company_detail', 'company_delete',
            'cart_view',
            'order_approve_quotation', 'order_payment_confirm',
            'order_confirm_quotation', 'confirm_purchase', 'order_list', 'order_detail',
            'register', 'update', 'password_change', 'logout', 'view', 'user_list'

            ]

CA_VIEWS = ['dashboard', 'inventory',
            'product_detail',
            'project_list', 'project_detail',
            'company_detail',
            'cart_view',
            'order_confirm_quotation', 'order_confirm',
            'order_list', 'order_detail',
            'update', 'password_change', 'logout', 'view',
            ]

CU_VIEWS = ['dashboard', 'inventory',
            'product_detail',
            'project_list', 'project_detail',
            'company_detail',
            'order_list', 'order_detail',
            'update', 'password_change', 'logout', 'view',
            ]

YM_VIEWS = ['dashboard', 'inventory',

            'add_dn_cn', 'order_list', 'order_detail',
            'update', 'password_change', 'logout', 'view',
            ]

PM_VIEWS = ['dashboard', 'inventory',
            'project_list', 'project_detail',
            'add_dn_cn', 'order_list', 'order_detail',
            'update', 'password_change', 'logout', 'view',
            ]


class LoginControlMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        assert hasattr(request, 'user')
        path = request.path_info
        view = resolve(path).url_name

        if request.user.is_authenticated and view in settings.LOGIN_NOT_REQUIRED_VIEWS:
            return redirect('dashboard')
        elif request.user.is_authenticated or view in settings.LOGIN_NOT_REQUIRED_VIEWS:

            # User logged in

            return None
        else:
            if view != 'dashboard':
                messages.error(request, 'Error ! Login required ')
            return redirect('login')


class AccessControlMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        assert hasattr(request, 'user')
        path = request.path_info
        view = resolve(path).url_name
        temp = path.lstrip('/')
        temp = temp.split('/')
        print(temp[0])
        if request.user.is_authenticated:
            account_type = request.user.profile.account_type
            if view == None:  # Static image retrieval view
                return None
            if account_type == 'SA' and temp[0] == 'admin':
                return None

            if account_type == 'SA' and view in SU_VIEWS:
                return None
            elif account_type == 'SU' and view in SU_VIEWS:
                return None
            elif account_type == 'CA' and view in CA_VIEWS:
                return None
            elif account_type == 'CU' and view in CU_VIEWS:
                return None
            elif account_type == 'YM' and view in YM_VIEWS:
                return None
            elif account_type == 'PM' and view in PM_VIEWS:
                return None
            else:
                return HttpResponseForbidden("Access Denied")

"""middle ware catalog"""
# Django 
from django.shortcuts import redirect
from django.urls import reverse


class ProfileCompletitionMiddleware:
    """Profile completion middleware
        Ensure every user that is interaction whit the app have profile and biograpy
    """
    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request):
        """code to be execute for eac request vefore the viw is called"""
        if not request.user.is_anonymous:
            if not request.user.is_staff:
                profile = request.user.profile
                if not profile.picture or not profile.biograpy :
                    if request.path not in [reverse('users:update'), reverse('users:logout'), reverse('admin')]:
                        return redirect('users:update')
            
        response = self.get_response(request)
        return response

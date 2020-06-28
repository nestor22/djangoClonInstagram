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
            profile = request.user.profile
            if not profile.picture or not profile.biograpy :
                if request.path not in [reverse('update_profile'), reverse('logout')]:
                    return redirect('update_profile')
            
        response = self.get_response(request)
        return response
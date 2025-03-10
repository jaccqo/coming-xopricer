from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .models import SiteConfig,Subscriber
import json
def coming_soon(request):
    site_config = SiteConfig.objects.first()
    return render(request, 'landing/coming_soon.html', {'site_config': site_config})


def subscribe(request):
    if request.method == "POST":
        data = json.loads(request.body)
        email = data.get("email")

        if not email:
            return JsonResponse({"status": "error", "message": "Email is required."}, status=400)

        if Subscriber.objects.filter(email=email).exists():
            return JsonResponse({"status": "error", "message": "You're already subscribed! Stay tuned for updates."}, status=400)

        Subscriber.objects.create(email=email)
        return JsonResponse({"status": "success", "message": "Thank you for subscribing! We'll notify you when we launch."})

    return JsonResponse({"status": "error", "message": "Invalid request"}, status=400)
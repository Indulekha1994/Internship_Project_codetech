from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import WebsiteUsage
from django.db.models import Sum
from datetime import timedelta
from django.utils.timezone import now
from urllib.parse import urlparse

PRODUCTIVE = ["github.com", "leetcode.com", "google.com", "stackoverflow.com"]
UNPRODUCTIVE = ["facebook.com", "youtube.com", "twitter.com", "tiktok.com"]

def classify(site):
    site = site.lower()
    domain = urlparse(site).netloc

    if any(p in domain for p in PRODUCTIVE):
        return "productive"
    elif any(u in domain for u in UNPRODUCTIVE):
        return "unproductive"
    return "neutral"

@api_view(['POST'])
def save_usage(request):
    website = request.data['website']
    time_spent = request.data['time']
    
    category = classify(website)
    print("DEBUG:", website, "→", category)
    
    WebsiteUsage.objects.create(
        website=website,
        time_spent=time_spent,
        category=category
    )
    return Response({"status": "saved"})

@api_view(['GET'])
def weekly_report(request):
    week_ago = now() - timedelta(days=7)
    data = WebsiteUsage.objects.filter(date__gte=week_ago)

    productive = data.filter(category="productive").aggregate(Sum('time_spent'))
    unproductive = data.filter(category="unproductive").aggregate(Sum('time_spent'))
    neutral = data.filter(category="neutral").aggregate(Sum('time_spent'))

    return Response({
        "productive": productive['time_spent__sum'] or 0,
        "unproductive": unproductive['time_spent__sum'] or 0,
        "neutral": neutral['time_spent__sum'] or 0
    })
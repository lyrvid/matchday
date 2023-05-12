import requests

from rest_framework.decorators import api_view
from rest_framework.request import Request
from django.http import JsonResponse, HttpResponseNotFound, HttpResponseServerError
from .models import Quote, Author
from .serializers import QuoteSerializer, AuthorSerializer


@api_view(['GET'])
def get_random_quote(request: Request):
    # Order randomly and select first
    random_quote = Quote.objects.order_by("?").first()
    serializer = QuoteSerializer(random_quote)
    return JsonResponse(serializer.data)


@api_view(['GET'])
def get_all_authors(request: Request):
    all_authors = Author.objects.all()
    serializer = AuthorSerializer(all_authors, many=True)
    return JsonResponse({"authors": serializer.data})


@api_view(['GET'])
def get_random_quote_for_author(request: Request, author_name: str):
    first_name, last_name = author_name.split(' ')
    # Filter to supplied author, order randomly and select first
    random_quote = Quote.objects.filter(
        author__first_name=first_name,
        author__last_name=last_name
    ).order_by("?").first()

    # if no quote, return 404 response
    if not random_quote:
        return HttpResponseNotFound()

    serializer = QuoteSerializer(random_quote)
    return JsonResponse(serializer.data)


@api_view(['GET'])
def get_random_quote_from_zen(request: Request):
    response = requests.get("https://zenquotes.io/api/random")

    # If the response from Zen Quotes is not 2xx, something went wrong
    if response.status_code < 200 or response.status_code > 299:
        return HttpResponseServerError()

    json = response.json()[0]
    f_name, l_name = json["a"].split(' ')
    quote = {
        "quote": json["q"],
        "author": {
            "first_name": f_name,
            "last_name": l_name,
        }
    }

    return JsonResponse(quote)

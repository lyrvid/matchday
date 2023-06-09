"""
URL configuration for matchday project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

import matchday.routes

urlpatterns = [
    path("admin/", admin.site.urls),
    path("qotd/", matchday.routes.get_random_quote),
    path("authors/", matchday.routes.get_all_authors),
    path("quotd/zen", matchday.routes.get_random_quote_from_zen),
    path("quotd/<str:author_name>", matchday.routes.get_random_quote_for_author),
]

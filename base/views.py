from django.shortcuts import render
from .models import Domain, Topic


def home(request):
    domains = Domain.objects.all()
    context = {"domains": domains}
    return render(request, "base/home.html", context)


def domain(request, slug):
    domain = Domain.objects.prefetch_related("topics").get(slug=slug)

    context = {"domain": domain}

    return render(request, "base/domain.html", context)


def topic(request, domainSlug, topicSlug):
    topic = Topic.objects.select_related("domain").get(
        slug=topicSlug, domain__slug=domainSlug
    )

    context = {"topic": topic, "domain": topic.domain}

    return render(request, "base/topic.html", context)

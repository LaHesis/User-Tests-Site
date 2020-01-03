"""Main app views."""
from django.shortcuts import render


def static_test_list(request):
    """Static tests list."""
    return render(request, 'main/static_test_list.html', {})

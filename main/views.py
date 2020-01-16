"""Main app views."""
from django.shortcuts import render


def static_tests_list(request):
    """Handle static main page."""
    return render(request, 'main/static_test_lists.html', {})

from django.http import JsonResponse

def greetings(request):
    result = {"message": "Welcome to ciphers service!"}
    return JsonResponse(result)
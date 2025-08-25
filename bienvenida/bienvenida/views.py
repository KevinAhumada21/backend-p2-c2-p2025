from django.http import HttpResponse

def inicio(request):
    nombre = "Kevin Merino"
    return HttpResponse(f"¡Bienvenidos a mi primera app Django, {nombre}!")

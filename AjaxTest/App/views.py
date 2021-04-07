from django.shortcuts import render,redirect
from App.models import datos

def Home(request):
    ctx = {"Name": 'pedro',
           "Category": 'estudiante',
           'Quantity': 20,
           }

    return render(request, 'HomePageForm.html', ctx)

def formulario(request):
    print('************* FORM *************')

    Nombre = request.GET['name']
    Categoria = request.GET['category']
    Cantidad = request.GET['quantity']

    Newvector = datos(nombre=Nombre,categoria=Categoria,cantidad=Cantidad)
    Newvector.save()


    ctx = {"Name": Nombre,
           "Category": Categoria,
           'Quantity': Cantidad,
           }
    return redirect("HomePage")
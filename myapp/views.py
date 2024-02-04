from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseNotFound
from .models import Entity
from data.entities_data import entities

def main_page(request):
    endpoints_info = {
        'entity_list': '/entity/',
        'entity_profile': '/entity/:id',
        'create_entity': '/entity/',
        'delete_entity': '/entity/:id/delete/'
    }
    return render(request, 'main_page.html', {'endpoints_info': endpoints_info})

def entity_list(request):
    return render(request, 'entity_list.html', {'entities': entities})

def entity_profile(request, id):
    try:
        entity = next((e for e in entities if e['id'] == int(id)), None)
        if entity:
            return render(request, 'entity_profile.html', {'entity': entity})
        else:
            return HttpResponseNotFound("Entity not found")
    except ValueError:
        return HttpResponseNotFound("Invalid entity ID")

def image_view(request):
    try:
        return render(request, 'image.html')
    except Exception as e:
        return HttpResponseNotFound("Image not found")

def create_entity(request):
    if request.method == 'POST':
        try:
            name = request.POST.get('name')
            description = request.POST.get('description')
            entity = Entity.objects.create(name=name, description=description)
            entities.append({'id': entity.id, 'name': entity.name, 'description': entity.description})
            return redirect('entity_list')
        except Exception as e:
            return HttpResponseNotFound("Failed to create entity")
    return render(request, 'create_entity.html')

def delete_entity(request, id):
    try:
        entity = Entity.objects.get(id=id)
        entity.delete()

       
        for e in entities:
            if e['id'] == int(id):
                entities.remove(e)
                break

        return redirect('entity_list')
    except Entity.DoesNotExist:
        return HttpResponseNotFound("Entity not found")
    except Exception as e:
        return HttpResponseNotFound("Failed to delete entity")  
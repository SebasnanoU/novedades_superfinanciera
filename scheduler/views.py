from django.http import HttpResponse
from datetime import datetime
from novedades.models import Novedades
from circulares.models import Circulares
from scheduler.scraping import get_superfinanciera, update_novedades, update_circulares


def update(request):
    print("Actualizando novedades y circulares...")
    print("Hora de ejecución:", datetime.now())
    
    try:
        # Actualizar novedades
        novedades_data = update_novedades(get_superfinanciera())
        print("Novedades agregadas:", len(novedades_data), get_superfinanciera().status_code)
        for novedad in novedades_data:
            novedad.save()
        
        # Actualizar circulares
        circulares_nuevas = update_circulares(get_superfinanciera())
        print("Nuevas circulares agregadas:", len(circulares_nuevas), get_superfinanciera().status_code)
        for circular in circulares_nuevas:
            try:
                circular.save()
            except Exception as e:
                print(f"Error al guardar circular: {e}")
        
        return HttpResponse("Actualización de novedades y circulares completada.")
    
    except Exception as e:
        print(f"Error al actualizar novedades y circulares: {e}")
        return HttpResponse("Ocurrió un error al actualizar novedades y circulares.")

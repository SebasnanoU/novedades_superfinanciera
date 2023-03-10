from django.http import HttpResponse
from .scheduler import Scheduler
import schedule
from scheduler.scraping import update_novedades, update_circulares


def start(request):
    scheduler = Scheduler()
    
    # Programamos la tarea para que se ejecute cada día a las 6:00 pm.
    novedades_task = scheduler.add_task(update_novedades, 86400)
    circulares_task = scheduler.add_task(update_circulares, 86400)

    novedades_task.run()
    circulares_task.run()

    return HttpResponse("Tarea programada con éxito.")

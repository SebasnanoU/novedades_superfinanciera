import schedule
import time

class Scheduler:
    def __init__(self):
        self.tasks = []

    def add_task(self, task, interval):
        """
        Agrega una tarea a la lista de tareas programadas para ejecución.

        :param task: función que se ejecutará
        :param interval: intervalo de tiempo entre ejecuciones (en segundos)
        """
        new_task = schedule.every(interval).seconds.do(task)
        self.tasks.append(new_task)
        return new_task

    def start(self):
        """
        Inicia el programador de tareas y ejecuta las tareas programadas en su horario correspondiente.
        """
        for task, interval in self.tasks:
            schedule.every(interval).seconds.do(task)

        while True:
            schedule.run_pending()
            time.sleep(1)

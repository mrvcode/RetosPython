import datetime
import time
import os
import threading


def countdown(target_date):

    while True:

        now_date_utc = datetime.datetime.now(datetime.timezone.utc)

        remaining_time = target_date_utc - now_date_utc

        if remaining_time.total_seconds() <= 0:
            print("\nCuenta atrás finalizada!!")
            break

        day, seconds = divmod(remaining_time.total_seconds(), 86400)
        hours, seconds = divmod(seconds, 3600)
        minutes, seconds = divmod(seconds, 60)

        os.system("cls")

        print(
            f"Tiempo restante: {int(day)} días, {int(hours)} horas, {int(minutes)} minutos, {int(seconds)} segundos"
        )

        time.sleep(1)


local_date = datetime.datetime(2025, 3, 9, 8, 34, 40)
local_date = local_date.replace(tzinfo=datetime.datetime.now().astimezone().tzinfo)

target_date_utc = local_date.astimezone(datetime.timezone.utc)

countdown_thread = threading.Thread(target=countdown, args=(target_date_utc,))
countdown_thread.start()
countdown_thread.join()  # no se parara hasta que kill terminal

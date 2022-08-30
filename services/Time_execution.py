import time

class Time_execution:

    def start_time():
        return time.time()

    def end_time():
        return time.time()

    def calculate_time_execution(start_time, end_time, operation_title):
        time = round(end_time - start_time, 2)
        print(f'Tempo de execução da operação {operation_title}: {time} segundos')

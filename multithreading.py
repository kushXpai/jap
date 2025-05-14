import threading
import random
import time

generated_number = None

number_generated_event = threading.Event()

class NumberGeneratorThread(threading.Thread):
    def run(self):
        global generated_number
        generated_number = random.randint(1, 100)
        print(f"Generated number: {generated_number}")
        number_generated_event.set()

class SquarePrinterThread(threading.Thread):
    def run(self):
        number_generated_event.wait()
        global generated_number
        if generated_number % 2 == 0:
            square = generated_number ** 2
            print(f"Square of {generated_number}: {square}")
        else:
            print(f"The number {generated_number} is odd, so square is not printed.")

class CubePrinterThread(threading.Thread):
    def run(self):
        number_generated_event.wait()
        global generated_number
        if generated_number % 2 != 0:
            cube = generated_number ** 3
            print(f"Cube of {generated_number}: {cube}")
        else:
            print(f"The number {generated_number} is even, so cube is not printed.")

def main():

    generator_thread = NumberGeneratorThread()
    square_thread = SquarePrinterThread()
    cube_thread = CubePrinterThread()

    generator_thread.start()
    square_thread.start()
    cube_thread.start()

    generator_thread.join()
    square_thread.join()
    cube_thread.join()

if __name__ == "__main__":
    main()

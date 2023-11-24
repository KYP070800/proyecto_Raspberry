import RPi.GPIO as GPIO
import time

# Configuración de pines
sensores = [14(8), 16(36), 18(12), 23(16), 25(22)]  # Pines GPIO para configurar los sensores, ventana sala, incendio, ventana habitacion, puerta principal y salida, sensor de gas 
alarma = 2  # Pin GPIO para configurar como salida
interruptor = 21  # Pin GPIO para el interruptor ender y apagar el sistema

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

# Configuración de la biblioteca RPi.GPIO
GPIO.setup(sensores, GPIO.IN)
GPIO.setup(alarma, GPIO.OUT)
GPIO.setup(interruptor, GPIO.IN)

try:
    while True:
        # Leer el estado de los pines de entrada
        estados_entrada = [GPIO.input(pin) for pin in sensores]
        print("Estados de pines de entrada:", estados_entrada)

        # Leer el estado del interruptor
        estado_interruptor = GPIO.input(interruptor)
        print("Estado del interruptor:", estado_interruptor)

        # Cambiar el estado del pin de salida cada segundo
        GPIO.output(alarma, not GPIO.input(alarma))
        time.sleep(1)

except KeyboardInterrupt:
    print("Programa interrumpido por el usuario")

finally:
    # Limpiar configuración al salir
    GPIO.cleanup()        
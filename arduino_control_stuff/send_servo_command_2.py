import lgpio
import time

# Set the GPIO pin (e.g., GPIO17)
gpio_pin = 17

# Initialize the GPIO chip (use 0 for the default chip)
h = lgpio.gpiochip_open(0)

# Set the GPIO pin as an output
lgpio.gpio_claim_output(h, gpio_pin)

try:
    while True:
        # Send a HIGH signal
        lgpio.gpio_write(h, gpio_pin, 1)
        # time.sleep(1)

        # Send a LOW signal
        # lgpio.gpio_write(h, gpio_pin, 0)
        # time.sleep(1)

except KeyboardInterrupt:
    lgpio.gpiochip_close(h)

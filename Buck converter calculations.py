Buck Converter Calculator
Power Electronics - Electrical Engineering

import math

def calculate_buck_converter(Vin, Vout, frequency, delta_I, delta_V, load_resistance):
"""
Calculate important parameters of an ideal Buck Converter.

Vin             : Input voltage (V)
Vout            : Desired output voltage (V)
frequency       : Switching frequency (Hz)
delta_I         : Allowed inductor ripple current (A)
delta_V         : Allowed output voltage ripple (V)
load_resistance : Load resistance (ohm)

Returns:
    Duty cycle
    Output current
    Inductor value
    Capacitor value
"""

# Duty cycle for ideal buck converter
duty_cycle = Vout / Vin

# Output current
Iout = Vout / load_resistance

# Inductor value
# L = (Vin - Vout) * D / (f * delta_I)
L = ((Vin - Vout) * duty_cycle) / (frequency * delta_I)

# Output capacitor value
# C = delta_I / (8 * f * delta_V)
C = delta_I / (8 * frequency * delta_V)

return duty_cycle, Iout, L, C


print("=" * 55)
print(" BUCK CONVERTER CALCULATOR")
print(" POWER ELECTRONICS")
print("=" * 55)

try:
Vin = float(input("Enter input voltage Vin (V): "))
Vout = float(input("Enter desired output voltage Vout (V): "))
frequency = float(input("Enter switching frequency (Hz): "))
delta_I = float(input("Enter allowed inductor ripple current (A): "))
delta_V = float(input("Enter allowed output voltage ripple (V): "))
load_resistance = float(input("Enter load resistance (ohm): "))

# Input validation
if Vin <= 0:
    raise ValueError("Input voltage must be positive.")

if Vout <= 0:
    raise ValueError("Output voltage must be positive.")

if Vout >= Vin:
    raise ValueError(
        "For an ideal buck converter, Vout must be less than Vin."
    )

if frequency <= 0:
    raise ValueError("Switching frequency must be positive.")

if delta_I <= 0:
    raise ValueError("Ripple current must be positive.")

if delta_V <= 0:
    raise ValueError("Ripple voltage must be positive.")

if load_resistance <= 0:
    raise ValueError("Load resistance must be positive.")

# Calculate converter parameters
duty_cycle, Iout, L, C = calculate_buck_converter(
    Vin,
    Vout,
    frequency,
    delta_I,
    delta_V,
    load_resistance
)

# Convert units
L_uH = L * 1e6
C_uF = C * 1e6

print("\n" + "=" * 55)
print("                    RESULTS")
print("=" * 55)

print(f"Input Voltage              : {Vin:.2f} V")
print(f"Output Voltage             : {Vout:.2f} V")
print(f"Duty Cycle                 : {duty_cycle:.4f}")
print(f"Duty Cycle (%)             : {duty_cycle * 100:.2f} %")
print(f"Output Current             : {Iout:.3f} A")
print(f"Required Inductor          : {L_uH:.3f} uH")
print(f"Required Output Capacitor  : {C_uF:.3f} uF")

print("=" * 55)


except ValueError as error:
print(f"\nError: {error}")

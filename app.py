import numpy as np

def simulate_gate(temp):
    target_temp = 35
    if temp >= target_temp:
        # حساب التمدد (افتراضياً)
        opening_degree = min(90, (temp - target_temp) * 5)
        return f"Open ({opening_degree} degrees)"
    return "Closed"

print(f"Status at 37°C: {simulate_gate(37)}")

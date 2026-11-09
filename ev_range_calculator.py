print("--- EV Battery Range Calculator ---")

battery_capacity = float(input("Enter battery capacity (in kWh, e.g., 30 or 40): "))
driving_mode = input("Choose driving mode (Eco / Normal / Sport): ").strip().lower()

if driving_mode == "eco":
    energy_consumption = 120  
    print("Mode Selected: Eco Mode (Maximum Range)")
elif driving_mode == "sport":
    energy_consumption = 180  
    print("Mode Selected: Sport Mode (High Power, Lower Range)")
else:
    energy_consumption = 145  
    print("Mode Selected: Normal Mode")

total_energy_wh = battery_capacity * 1000
estimated_range = total_energy_wh / energy_consumption

print(f"\nCalculated EV Driving Range: {round(estimated_range, 2)} Kilometers (KM)")
print("---------------------------------")
  

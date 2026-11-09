print("--- Automotive Braking Distance Calculator ---")

speed_kmh = float(input("Enter vehicle speed (in km/h, e.g., 60 or 80): "))
speed_ms = speed_kmh * (5 / 18)

print("\nSelect Road Condition:")
print("1. Dry Road (High Friction)")
print("2. Wet Road (Medium Friction)")
print("3. Icy Road (Very Low Friction)")
choice = input("Enter choice (1/2/3): ").strip()

if choice == "1":
    mu = 0.7  
    road_type = "Dry Road"
elif choice == "2":
    mu = 0.4  
    road_type = "Wet Road"
elif choice == "3":
    mu = 0.15  
    road_type = "Icy Road"
else:
    mu = 0.6  
    road_type = "Standard Road"

g = 9.81
braking_distance = (speed_ms ** 2) / (2 * mu * g)

print(f"\n--- Calculation Results ({road_type}) ---")
print(f"Vehicle Speed: {speed_kmh} km/h")
print(f"Calculated Stopping Distance: {round(braking_distance, 2)} Meters")
print("--------------------------------------------------")

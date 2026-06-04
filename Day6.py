# Initial server room metrics in Addis Ababa data hub
current_temperature = 38
target_goal = 24

# 1. Custom Function for Active Cooling Status (Passes temp as a parameter)
def ay_see_bicha(temp):
    print(f"❄️ [ቅዝቃዜ] AC is running dynamically... Temperature dropped to: {temp}°C")

# 2. Custom Function for Final Confirmation
def maregagecha():
    print("\n==================================================")
    print("✅ [ማረጋገጫ] Target safety temperature reached: 24°C!")
    print("🔒 Server racks stabilized. Switching to low-power mode.")
    print("==================================================")

print("🚀 Ethio Data Center Climate Control Engine Active...\n")

# 3. The Controlled Loop Engine
while current_temperature > target_goal:
    # Print the current temperature status before dropping it
    ay_see_bicha(current_temperature)
    
    # Lower the server room temperature by 2 degrees
    current_temperature -= 2

# 4. Call the final confirmation function once the loop finishes successfully
maregagecha()
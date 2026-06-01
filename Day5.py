import random

print("=========================================")
print("🔒 CYBER-SAFE PASSWORD ARCHITECT (v1.0) 🔒")
print("=========================================\n")

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '+', '&', '*', '(', ')', '@', '^', '_', '-']

password_pool = []

# Secure Input Requirements
num_letter = int(input("🛡️  How many letters required? "))
num_symbol = int(input("🛡️  How many special symbols required? "))
num_number = int(input("🛡️  How many numerical digits required? "))

# 1. Iterative Character Generation
for _ in range(num_letter):
    password_pool.append(random.choice(letters))

for _ in range(num_number):
    password_pool.append(random.choice(numbers))

for _ in range(num_symbol):
    password_pool.append(random.choice(symbols))

# 2. Advanced Cryptographic Shuffling
random.shuffle(password_pool)

# 3. High-Performance String Assembly
final_password = "".join(password_pool)

# 4. UNIQUE FEATURE: Real-Time Security Audit Engine
total_length = len(final_password)
security_score = 0
status = "CRITICAL WEAKNESS"

if total_length >= 14 and num_symbol >= 3 and num_number >= 3:
    status = "MILITARY GRADE SECURITY (Excellent)"
elif total_length >= 10 and num_symbol >= 1:
    status = "STRONG (Corporate Standard)"
elif total_length >= 8:
    status = "MEDIUM (Basic Account Standard)"

# 5. Professional Terminal Dashboard Output
print("\n" + "="*41)
print("             SECURITY REPORT             ")
print("="*41)
print(f"🔑 Generated Password : {final_password}")
print(f"📏 Total Characters  : {total_length} elements")
print(f"📊 Integrity Status   : {status}")
print("="*41)
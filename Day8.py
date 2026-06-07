alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
             'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 
             'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(original_text, shift_amount, encode_or_decode):
    output_text = ""
    
    # Defensive Control: If decoding, reverse the shift direction
    if encode_or_decode == "decode":
        shift_amount *= -1
        
    for letter in original_text:
        # Preserve numbers, spaces, and symbols exactly as they are
        if letter not in alphabet:
            output_text += letter
        else:
            # Shift the letter index securely
            shifted_position = alphabet.index(letter) + shift_amount
            # Use modulo (%) to prevent index out of range errors if index loops past 'z'
            shifted_position %= len(alphabet)
            output_text += alphabet[shifted_position]
            
    print(f"🔒 Resulting message: {output_text}")

# --- SYSTEM TERMINAL INTERFACE ---
print("=========================================")
print("     SECURE CAESAR CIPHER ENGINE v1.0    ")
print("=========================================")

should_continue = True

while should_continue:
    direction = input("Type 'encode' to encrypt, 'decode' to decrypt:\n").lower().strip()
    
    # Validation check for correct operational modes
    if direction not in ["encode", "decode"]:
        print("❌ Invalid selection. Please restart or select a valid mode.")
        continue
        
    text = input("Type your message:\n").lower()
    
    # Bug prevention: Handle cases where users enter non-numeric strings for shift
    try:
        shift = int(input("Type the shift number:\n"))
    except ValueError:
        print("❌ Shift factor must be a valid integer.")
        continue

    # Execute the core function
    caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)
    
    restart = input("\nType 'yes' to go again. Otherwise type 'no' to exit:\n").lower().strip()
    if restart == "no":
        should_continue = False
        print("\n=========================================")
        print("  System offline. Connections secured.   ")
        print("=========================================")
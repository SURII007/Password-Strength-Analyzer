import argparse
from zxcvbn import zxcvbn

def analyze_password(password):
    # Analyze password using zxcvbn for entropy and strength [cite: 61]
    results = zxcvbn(password)
    score = results['score'] # Scale of 0-4
    crack_time = results['crack_times_display']['offline_slow_hashing_1e4_per_second']
    
    print(f"\n--- Password Analysis ---")
    print(f"Password: {password}")
    print(f"Strength Score: {score}/4")
    print(f"Estimated Crack Time: {crack_time}")
    print(f"Suggestions: {', '.join(results['feedback']['suggestions'])}")

def generate_wordlist(name, dob, pet_name):
    # Generate custom wordlist based on user inputs [cite: 62]
    # Includes patterns like leetspeak and appending years [cite: 63]
    base_words = [name, dob, pet_name]
    wordlist = []
    
    for word in base_words:
        if word:
            wordlist.append(word)
            wordlist.append(word + "123")
            wordlist.append(word + "2024")
            # Simple leetspeak pattern [cite: 63]
            wordlist.append(word.replace('a', '@').replace('s', '5').replace('o', '0'))
            
    # Export in .txt format for cracking tools [cite: 64]
    with open("custom_wordlist.txt", "w") as f:
        for item in wordlist:
            f.write(f"{item}\n")
    print(f"\n[+] Success! Wordlist saved to 'custom_wordlist.txt' [cite: 66]")

if __name__ == "__main__":
    print("Elevate Labs Internship: Password Analyzer & Wordlist Generator [cite: 1, 58]")
    pwd = input("Enter a password to test: ")
    analyze_password(pwd)
    
    print("\n--- Generate Custom Wordlist ---")
    u_name = input("Enter target name: ")
    u_dob = input("Enter birth year: ")
    u_pet = input("Enter pet name: ")
    generate_wordlist(u_name, u_dob, u_pet)
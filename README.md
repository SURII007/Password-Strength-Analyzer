Password Strength Analyzer & Custom Wordlist Generator
🛡️ Project Overview
This project was developed as part of a 2-week cybersecurity internship project. The objective is to build a tool that evaluates password security and demonstrates how personal information can be used to generate custom wordlists for security testing.


📋 Features

Password Scoring: Analyzes user passwords using the zxcvbn library to determine entropy and strength.
Crack Time Estimation: Provides a realistic estimate of how long a password would take to cracks
Wordlist Generation: Allows user inputs like names, dates, and pet names to create a custom attack-specific wordlist.
Pattern Matching: Includes common patterns such as "leetspeak" and year appending.
Export Function: Automatically exports results in a .txt format compatible with cracking tools.

🛠️ Tools & Technologies

Language: Python 
Libraries: zxcvbn, argparse, NLTK 
Interface: Command Line Interface (CLI) 

🚀 How to Run
1.Clone the repository: git clone https://github.com/SURII007/Password-Strength-Analyzer.git
2.Install dependencies: pip install -r requirements.txt
3.Execute the script: python main.py



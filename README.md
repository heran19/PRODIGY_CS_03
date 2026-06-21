# Password Complexity Checker
 
A Python program that assesses the strength of a password based on multiple security criteria. This project was completed as part of the **Prodigy InfoTech Cybersecurity Internship** (Task-03).
 
## About
 
This project evaluates how strong or weak a given password is by checking it against common security best practices. It provides instant feedback to the user, highlighting what makes the password strong and suggesting specific improvements where needed.
 
## Features
 
- Checks password length (minimum 8 characters recommended)
- Verifies presence of uppercase letters
- Verifies presence of lowercase letters
- Verifies presence of numeric digits
- Verifies presence of special characters
- Provides a strength rating: Very Weak, Weak, Moderate, Strong, or Very Strong
- Gives actionable feedback on how to improve weak passwords
 
## How It Works
 
The program checks the password against five criteria, awarding one point for each criterion met:
 
1. Length ≥ 8 characters
2. Contains at least one uppercase letter (A–Z)
3. Contains at least one lowercase letter (a–z)
4. Contains at least one digit (0–9)
5. Contains at least one special character (e.g., `!@#$%^&*`)
 
The total score (0–5) is then mapped to a strength rating, and any unmet criteria are listed as suggestions for improvement.
 
## Requirements
 
- Python 3.x (uses only the built-in `re` module)
 
## Usage
 
1. Clone this repository or download the script.
 
```bash
git clone https://github.com/your-username/password-checker.git
cd password-checker
```
 
2. Run the script:
 
```bash
python password_checker.py
```
 
3. Follow the prompt:
 
```
Enter a password to check: Hello123
 
Password Strength: Moderate
Suggestions:
- Add at least one special character.
```
 
## Example
 
| Password | Strength | Feedback |
|----------|----------|----------|
| `abc` | Very Weak | Too short, missing uppercase, numbers, special characters |
| `Hello123` | Moderate | Missing special character |
| `Hello@123` | Strong | Meets most criteria |
| `H3llo@World!` | Very Strong | Meets all criteria |
 
## File Structure
 
```
password-checker/
│
├── password_checker.py   # Main program
└── README.md             # Project documentation
```
 
## Learning Outcomes
 
- Using regular expressions (regex) for pattern matching in Python
- Designing simple scoring/rule-based evaluation systems
- Understanding what constitutes a strong password and why
- Practical application of cybersecurity best practices in code
 
## Acknowledgements
 
This project was completed as part of the Cybersecurity Internship offered by **Prodigy InfoTech**.
 
## License
 
This project is open source and available for educational purposes.

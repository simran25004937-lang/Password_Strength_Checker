# Password Strength Checker

## Project Description
A Python-based application that checks password strength using password length and character variety.

## Features
- Checks password length (minimum 8 characters).
- Detects uppercase letters.
- Detects lowercase letters.
- Detects numbers.
- Detects special characters.
- Classifies passwords as Weak, Medium, or Strong.
- Handles empty password input.

## Package Structure
```text
Password_Strength_Checker/
├── main.py
└── password_pkg/
    ├── __init__.py
    └── ActualTask.py
```

## Functions
1. `check_length()` – Checks password length.
2. `character_score()` – Calculates character variety.
3. `strength_result()` – Determines password strength.

## Technologies Used
- Python
- Visual Studio Code
- GitHub

## How to Run
Open Terminal in the project folder and run:

```bash
python3 main.py
```

## Test Cases
| Input | Expected Result |
|---|---|
| abc123 | Weak Password |
| Simran123 | Medium Password |
| Simran@123 | Strong Password |
| Empty input | Password cannot be empty |

## Conclusion
This project demonstrates Python packages, reusable functions, conditional statements, and input validation.

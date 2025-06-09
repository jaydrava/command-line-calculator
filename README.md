# Command Line Calculator
A straightforward Python command-line Calculator designed to perform basic arithmetic operations - addition, subtraction, multiplication, and division with user-friendly prompts and robust input validation.

## What This Project Does

- Runs in a continuous loop, allowing you to perform multiple calculations
- Validates user inputs to ensure numbers and supported operations
- Handles errors gracefully, including division by zero
- Clear and simple interface to enhance user experience
- Parameterized unit tests with 100% coverage
- GitHub Actions CI pipeline

# Project Layout
````
command-line-calculator/
│
├── calculator/               # Custom module for core math operations
│   ├── __init__.py           # Makes calculator a package
│   └── operation.py          # add, subtract, multiply, divide functions
│
├── tests/                    # Test folder with all unit test files
│   └── test_operations.py    # Parameterized tests using pytest
│
├── main.py                   # Main CLI program where calculator runs
├── README.md                 # Instructions, setup guide, and usage info
└── .gitignore                # Keeps venv, __pycache__, etc. out of Git
````
# Getting Started 

### 1. Clone the Repository 

```
git clone git@github.com:your-username/command-line-calculator.git
cd command-line-calculator
```
# 2. Create & Activate Virtual Environment

python -m venv venv

*# On macOS/Linux*

    source venv/bin/activate

*# On Windows (Command Prompt)*

    venv\Scripts\activate.bat

*# On Windows (PowerShell)*

    venv\Scripts\Activate.ps1

### 3. Install Dependencies
    pip install -r requirements.txt

### 4. Running Test 
    pytest --cov=calculator

### 5. Run the Calculator
    python main.py

### 6. GitHub Actions CI/CD
 ```
    Test automatically run on each push using GitHub Actions. CI fails if :
    Any test fails  
    Test coverage is less than 100%
 ```
# 7. Example Session
```
Welcome to the Command Line Calculator!
Available operations: add, subtract, multiply, divide
Type 'q' to quit the calculator.

Enter operation (add, subtract, multiply, divide): add
Enter first number: 5
Enter second number: 3
The result of add between 5.0 and 3.0 is: 8.0
```
# 8. Contact
```
    For questions or suggestions, feel free to reach out at [jraval.0901@gmail.com]
```


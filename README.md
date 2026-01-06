# Python Calculator – Terminal-Based

Python Calculator is a simple, interactive terminal-based calculator designed for users who want to perform basic arithmetic operations. The calculator allows users to add, subtract, multiply, or divide two numbers while validating input and handling errors such as division by zero.

he main purpose of this application is to demonstrate Python fundamentals, including functions, loops, conditional statements, input validation, and user interaction in a terminal environment. It is targeted toward students, beginners, and individuals learning Python essentials. The project is fully compatible with the Python Essentials Template and can be deployed to Heroku.

## Features 

### Existing Features

- __Terminal Menu__
  
- Options 1–4 for operations: Addition, Subtraction, Multiplication, Division
- Option 5 to exit the program

Provides clear instructions for users and communicates the available operations.

![Full Result](https://github.com/cscode07/my-calculator/blob/main/media/full%20example.png)



- __Option For Operation__
  
Chose the option for operation.
 
![Option](https://github.com/cscode07/my-calculator/blob/main/media/step1.png)



- __First Number__
  
Chose the first number.
 
![Number1](https://github.com/cscode07/my-calculator/blob/main/media/step2.png)



- __Second Number__
  
Chose the second number.
 
![Number2](https://github.com/cscode07/my-calculator/blob/main/media/step3.png)



- __Exit Option__
  
- Option 5 allows the user to safely exit the calculator.
- Displays a friendly goodbye message.
 
![Result](https://github.com/cscode07/my-calculator/blob/main/media/full%20example.png)



- __Features Left to Implement__

- Extended operations (exponentiation, modulo)
- History of past calculations
- Option to use in a graphical interface (outside of terminal template)
- Additional error handling for edge cases (e.g., very large numbers)

## User Stories
- User1: I want to perform basic arithmetic operations quickly.
  
- User2: I want to know when I enter invalid input.
  
- User3 (Student): I want a simple, terminal-based calculator to practice Python.
  
- User4 (Beginner): I want clear instructions in the terminal for each operation.  



## Testing 


### Validator Testing 

- Python
  - No errors were returned when passing through the official [PEP8CI](https://pep8ci.herokuapp.com/)

![Pep8](https://github.com/cscode07/my-calculator/blob/main/media/pep8.png)


### Manual Testing 

| Feature            | Test Performed                     | Expected Outcome                 | Result      |
| ------------------ | --------------------------------- | --------------------------------  | ----------- |
| Addition           | Enter 1, numbers 10 & 5           | Result = 15                       | ✅ Pass     |
| Subtraction        | Enter 2, numbers 20 & 8           | Result = 12                       | ✅ Pass     |
| Multiplication     | Enter 3, numbers 6 & 7            | Result = 42                       | ✅ Pass     |
| Division           | Enter 4, numbers 12 & 4           | Result = 3                        | ✅ Pass     |
| Division by zero   | Enter 4, numbers 10 & 0           | Error message displayed           | ✅ Pass     |
| Invalid input      | Enter letters instead of numbers  | Error message displayed           | ✅ Pass     |
| Exit               | Enter 5                           | Goodbye message displayed         | ✅ Pass     |


### Browser Compatibility

Tested successfully on:
-Chrome 
-Firefox
-Edge
-Safari

 ### Device Responsiveness

- The mock terminal provided by the template works on:
  - iPhone SE, iPhone 16
  - iPad
  - Desktop (1366px, 1440px, 1920px)
- Layout displays correctly in all devices supported by the template.
 
## Deployment

Technologies Used
- Python 3
- Python Essentials Template
- Git & GitHub
- Heroku



## Credits 

### Content 

- All code written by me, except standard Python documentation references.  
- Logic inspired by classic calculator programs used in teaching Python fundamentals.

### Media








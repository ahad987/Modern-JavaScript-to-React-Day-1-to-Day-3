### Modern JavaScript to React (FrontEnd) for Django Framework (Day: 1 to 3)

Welcome to my learning journey! This repository documents my daily progress as I master modern frontend development—moving from core JavaScript fundamentals to React—specifically optimized for integration with the Django Web Framework (DRF).

* * *

### 📅 Phase 1: Modern JavaScript (Weeks 1-4)

### 🚀 Week 1: JavaScript Fundamentals

### 🔹 Day 1: Introduction to JavaScript & Setup

*   **Concepts Learned:** JS runtime engine, linking external scripts, browser console, and execution context.

### 🔹 Day 2: Operators with Variables, Data types, let vs const

*   **Concepts Learned:** Block scope vs function scope (`let` vs `const`), dynamic data types, Arithmetic, Comparison, and Logical (`&&`, `||`, `!`) operators.
*   **Project Built:** Grade Calculator
    *   *Input:* `85` ➔ *Output:* `A+`
*   **Assessment Challenge:** E-commerce Discount Calculator
    *   *Logic:* Calculates discount rates (0%, 10%, 20%) based on total purchase limits using comparison and logical operators.

### 🔹 Day 3: Conditional Statements

*   **Concepts Learned:** Flow control using `if`, `else`, `else if`, and multi-way branching using `switch` cases.
*   **Project Built:** Traffic Signal Simulator
    *   *Inputs:* `red`, `yellow`, `green` ➔ *Outputs:* `STOP`, `READY`, `GO`
*   **Assessment Challenge:** Movie Ticket Pricing System
    *   *Logic:* Nested validation checking passenger age groups combined with weekday/weekend scheduling filters.

* * *

### 🛠️ Code Repositories & Implementation

### 📊 Day 2 Project: Grade Calculator

javascript

    function calculateGrade(marks) {
        let grade = "";
        if (marks >= 80 && marks <= 100) {
            grade = "A+";
        } else if (marks >= 70 && marks < 80) {
            grade = "A";
        } else if (marks >= 60 && marks < 70) {
            grade = "A-";
        } else if (marks >= 50 && marks < 60) {
            grade = "B";
        } else if (marks >= 40 && marks < 50) {
            grade = "C";
        } else if (marks >= 33 && marks < 40) {
            grade = "D";
        } else if (marks >= 0 && marks < 33) {
            grade = "F (Fail)";
        } else {
            grade = "Invalid Marks!";
        }
        return `Output: ${grade}`;
    }
    console.log(calculateGrade(85)); // Output: A+
    

Use code with caution.

### 🚦 Day 3 Project: Traffic Signal Simulator

javascript

    function checkSignal(color) {
        let action = "";
        switch(color.toLowerCase()) {
            case "red":
                action = "STOP";
                break;
            case "yellow":
                action = "READY";
                break;
            case "green":
                action = "GO";
                break;
            default:
                action = "INVALID SIGNAL";
        }
        return action;
    }
    console.log(checkSignal("green")); // Output: GO
    

Use code with caution.

* * *

### 🎯 Active Challenges & Lab Assessments

### 🛒 Assessment 1: E-commerce Discount Calculator

*   **Objective:** Calculate final bill values after filtering purchases.
*   **Rules:**
    *   Purchase ≥ 5000 TK ➔ 20% Off
    *   Purchase 2000 TK to 4999 TK ➔ 10% Off
    *   Purchase < 2000 TK ➔ 0% Off

### 🎬 Assessment 2: Movie Ticket Pricing System

*   **Objective:** Dynamic pricing engine evaluating viewer age and calendar day.
*   **Rules:**
    *   Age < 12 ➔ 0 TK *(Child Free)*
    *   Age ≥ 60 ➔ 200 TK *(Senior Citizen)*
    *   Regular (Age 12-59) ➔ 500 TK *(Fri/Sat Weekend)* else 400 TK *(Weekdays)*

* * *

### 🎯 Learning Objectives

By completing the first three days of this phase, I have successfully mastered the following core engineering skills required to build reactive web frontends:

### ⚙️ JavaScript Core Mechanics

*   **Execution & Scope:** Understood how the V8 engine interprets code, utilizing block scope (`let`, `const`) to prevent variable leaking.
*   **Data Type Management:** Mastered dynamic typing and safe value assignment, ensuring stable state management for future API integrations.

### 🧮 Advanced Operations & Type Strictness

*   **Strict Comparison:** Implemented strict equality (`===`, `!==`) over loose equality (`==`) to eliminate silent type coercion bugs.
*   **Logical Composition:** Used short-circuit evaluation and logical chaining (`&&`, `||`, `!`) to handle complex frontend business rules.

### ⛓️ Control Flow & Architectural Branching

*   **Dynamic UI Conditionals:** Built conditional branching systems using `if/else` and `switch` statements to mutate user interfaces based on incoming application states.
*   **Scalable Code Structures:** Learned when to transition from nested `if` statements to flat, highly-readable `switch` blocks for maintainable clean code.

### 🐍 The Django Blueprint Connection

*   **State Alignment:** Preparing JavaScript logic patterns to map directly to Django backend logic structures.
*   **API Readiness:** Mastering frontend client-side validation loops to minimize unnecessary HTTP payload requests to **Django REST Framework (DRF)** endpoints.

* * *
## 👤 Contact

**Abdul Ahad Chowdhury**
- GitHub: [@ahad987](https://github.com/ahad987)
- Email: [ahad987@gmail.com](mailto:ahad987@gmail.com)
- **LinkedIn:** [Your Name / Profile](https://www.linkedin.com/in/ahad1987/)
- **Facebook:** [ahadc](https://facebook.com)
- **WhatsApp:** [Message on WhatsApp](https://wa.me)
- **Phone:** [+880 1812148778](tel:+8801812148778)
- Project: [https://github.com/ahad987/Modern-JavaScript-to-React-Day-1-to-Day-3](https://github.com/ahad987/Modern-JavaScript-to-React-Day-1-to-Day-3)

---
⭐ **Feel free to star this repository if you find my learning track useful!**
* * *
<div align="center">Made with ❤️ by Abdul Ahad Chowdhury</div>

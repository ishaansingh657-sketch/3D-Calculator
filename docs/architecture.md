# System Architecture

The 3D Scientific Calculator follows a simple full-stack architecture that separates the user interface, backend processing, calculation engine, database settings, and calculation history.

## Architecture Overview

```text
User
  │
  ▼
HTML / CSS / JavaScript
  │
  ▼
PHP Backend
  │
  ├──────────────► MySQL
  │                │
  │                └── Calculator Settings
  │
  ▼
Python Calculation Engine
  │
  ├── Performs calculations
  ├── Handles mathematical functions
  └── Records successful calculations
          │
          ▼
       CSV File
```

## Components

### 1. Frontend

The frontend provides the calculator interface and user interaction.

Technologies:

- HTML
- CSS
- JavaScript

The JavaScript handles button interactions, builds the expression, sends calculation requests to the PHP backend, and displays the returned result.

### 2. PHP Backend

The PHP backend acts as the connection layer between the frontend and the calculation engine.

Main responsibilities:

- Receive calculation requests from JavaScript
- Retrieve calculator settings from MySQL
- Pass calculation data to the Python engine
- Process the Python response
- Return the result to the frontend

Main file:

```text
backend/calculate.php
```

### 3. Python Calculation Engine

Python performs the actual mathematical calculations.

Main responsibilities:

- Arithmetic calculations
- Scientific calculations
- Degree and radian angle handling
- Input validation
- Error handling
- Calculation history logging

Main file:

```text
python/calculator.py
```

### 4. MySQL Database

MySQL stores the calculator configuration settings.

The project uses the following table:

```text
calculator_settings
```

The settings include:

- Decimal precision
- Angle mode
- Theme

Database setup is provided in:

```text
database/calculator_db.sql
```

### 5. CSV Calculation History

Successful calculations are recorded in:

```text
data/calculation_history.csv
```

The CSV file stores calculation information such as:

- Date and time
- First value
- Operator
- Second value
- Result

The generated calculation history is excluded from Git using `.gitignore`.

## Request Flow

A typical calculation follows this sequence:

1. The user enters values and selects an operation.
2. JavaScript collects the calculator input.
3. JavaScript sends the request to `calculate.php`.
4. PHP retrieves the relevant calculator settings from MySQL.
5. PHP passes the calculation request to the Python engine.
6. Python performs the calculation.
7. Python records a successful calculation in the CSV history file.
8. Python returns the calculation result.
9. PHP processes the response and returns JSON.
10. JavaScript displays the result in the calculator interface.

## Separation of Responsibilities

| Component  | Responsibility                             |
| ---------- | ------------------------------------------ |
| HTML       | Calculator structure                       |
| CSS        | User interface and visual design           |
| JavaScript | User interaction and frontend logic        |
| PHP        | Backend communication and request handling |
| Python     | Mathematical calculations and CSV logging  |
| MySQL      | Calculator configuration                   |
| CSV        | Calculation history                        |

## Project Structure

```text
3D-Calculator/
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
│
├── backend/
│   ├── calculate.php
│   └── db.php
│
├── python/
│   └── calculator.py
│
├── database/
│   └── calculator_db.sql
│
├── docs/
│   ├── architecture.md
│   ├── setup.md
│   └── Calculator.png
│
└── data/
    └── calculation_history.csv
```

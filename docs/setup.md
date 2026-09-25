# Setup & Installation

This guide explains how to set up and run the 3D Scientific Calculator locally.

## Prerequisites

Install the following:

- PHP 7.4 or later
- MySQL 8.x or compatible MariaDB
- Python 3.x
- Git
- A modern web browser

## 1. Clone the Repository

Clone the repository using Git:

```bash
git clone https://github.com/ishaansingh657-sketch/3D-Calculator.git
cd 3D-Calculator
```

## 2. Configure Environment Variables

The project includes:

```text
.env.example
```

It contains:

```env
DB_PASSWORD=your_mysql_password
PYTHON_EXECUTABLE=python
```

Set these variables in your operating system or server environment.

Do not commit real passwords, API keys, or other secrets to GitHub.

## 3. Set Up the Database

The database schema is available at:

```text
database/calculator_db.sql
```

Run this SQL file using MySQL or a database management tool such as phpMyAdmin.

The script creates:

```text
Database: calculator_db
Table: calculator_settings
```

The default settings are:

```text
Decimal Places: 10
Angle Mode: DEG
Theme: 3D Glass
```

## 4. Configure the Database Connection

The PHP database connection is located at:

```text
backend/db.php
```

The project reads the database password from:

```text
DB_PASSWORD
```

Make sure:

- MySQL is running.
- The database `calculator_db` exists.
- The `calculator_settings` table exists.
- The database credentials match your local environment.

## 5. Configure Python

The calculation engine is located at:

```text
python/calculator.py
```

The PHP backend uses the environment variable:

```text
PYTHON_EXECUTABLE
```

For a standard Python installation:

```env
PYTHON_EXECUTABLE=python
```

Verify Python is available from your terminal:

```bash
python --version
```

## 6. Verify PHP

Verify that PHP is available:

```bash
php --version
```

The PHP installation must be able to use the `mysqli` extension because the project uses MySQL through PHP `mysqli`.

## 7. Start the Application

From the project root, start PHP's built-in development server:

```powershell
php -S localhost:8000
```

Then open:

```text
http://localhost:8000/frontend/
```

## 8. Test the Calculator

Test basic arithmetic:

```text
7 + 3
```

Expected result:

```text
10
```

Test a scientific function:

```text
sin(90)
```

With the default `DEG` angle mode, the expected result is:

```text
1
```

Test square root:

```text
√25
```

Expected result:

```text
5
```

Test square:

```text
5²
```

Expected result:

```text
25
```

## 9. Verify Calculation History

After a successful calculation, the Python calculation engine automatically creates or updates:

```text
data/calculation_history.csv
```

The file contains calculation history such as:

- Date and time
- First number
- Operator
- Second number
- Result

The generated CSV file is excluded from Git.

## 10. Troubleshooting

### PHP command is not recognized

If this command fails:

```bash
php --version
```

make sure PHP is installed and its executable is available through the system PATH.

### Python command is not recognized

If this command fails:

```bash
python --version
```

make sure Python is installed and available through the system PATH.

You can also set `PYTHON_EXECUTABLE` to the appropriate Python executable configured for your system.

### Database connection fails

Check:

- MySQL is running.
- The database exists.
- The `calculator_settings` table exists.
- `DB_PASSWORD` is configured correctly.
- The connection settings in `backend/db.php` match your local MySQL configuration.

### Calculator does not return a result

Check:

- PHP's development server is running.
- The frontend is opened through the PHP server rather than directly as a file.
- Python is available to PHP.
- The database connection works.
- The browser console does not report JavaScript errors.

## Project Entry Point

The main frontend file is:

```text
frontend/index.html
```

The application is normally accessed through:

```text
http://localhost:8000/frontend/
```

## Important Security Note

Never commit the following to the public repository:

- Real database passwords
- `.env` files containing secrets
- Private credentials
- Generated calculation history containing private information

Use `.env.example` as the public configuration template.

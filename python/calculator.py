import math
import sys
import json
import csv
import os
from datetime import datetime


def save_to_csv(num1, operator, num2, result):

    project_root = os.path.dirname(
        os.path.dirname(os.path.abspath(__file__))
    )

    csv_file = os.path.join(
        project_root,
        "data",
        "calculation_history.csv"
    )

    file_exists = os.path.exists(csv_file)

    with open(csv_file, "a", newline="", encoding="utf-8") as file:

        fieldnames = [
            "Date & Time",
            "First Number",
            "Operator",
            "Second Number",
            "Result"
        ]

        writer = csv.DictWriter(
            file,
            fieldnames=fieldnames
        )

        if not file_exists:
            writer.writeheader()

        writer.writerow({
            "Date & Time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "First Number": num1,
            "Operator": operator,
            "Second Number": "" if num2 is None else num2,
            "Result": result
        })
def calculate(num1, operator, num2=None, angle_mode="DEG"):

    try:

        # Two-number operations

        if operator == "+":
            result = num1 + num2

        elif operator == "-":
            result = num1 - num2

        elif operator == "*":
            result = num1 * num2

        elif operator == "/":

            if num2 == 0:
                return "Error: Cannot divide by zero"

            result = num1 / num2

        elif operator == "%":

            if num2 is None:
                return "Error: Second number required"

            result = (num1 * num2) / 100

        elif operator == "^":

            result = num1 ** num2

        # One-number percentage

        elif operator == "percent":

            result = num1 / 100

        # Square root

        elif operator == "sqrt":

            if num1 < 0:
                return "Error: Cannot find a square root of a negative number"

            result = math.sqrt(num1)

        # Square

        elif operator == "square":

            result = num1 ** 2

        # Sine

        elif operator == "sin":

            if angle_mode == "DEG":
                angle = math.radians(num1)
            else:
                angle = num1

            result = round(math.sin(angle), 10)

        # Cosine

        elif operator == "cos":

            if angle_mode == "DEG":
                angle = math.radians(num1)
            else:
                angle = num1

            result = round(math.cos(angle), 10)

        # Tangent

        elif operator == "tan":

            if angle_mode == "DEG":
                angle = math.radians(num1)
            else:
                angle = num1

            result = round(math.tan(angle), 10)

        # Log base 10

        elif operator == "log":

            if num1 <= 0:
                return "Error: Logarithm is only defined for positive numbers"

            result = round(math.log10(num1), 10)

        # Natural logarithm

        elif operator == "ln":

            if num1 <= 0:
                return "Error: Natural logarithm is only defined for positive numbers"

            result = round(math.log(num1), 10)

        else:

            return "Error: Invalid operator"

        return result

    except (TypeError, ValueError, OverflowError):

        return "Error: Invalid number"


def main():

    # Check whether enough arguments were provided

    if len(sys.argv) < 3:

        print(json.dumps({
            "result": "Error: Missing input"
        }))

        return

    try:

        # First number

        num1 = float(sys.argv[1])

        # Operator

        operator = sys.argv[2]

        # Second number

        num2 = None

        if len(sys.argv) >= 4 and sys.argv[3] != "":
            num2 = float(sys.argv[3])

        # Angle mode

        angle_mode = "DEG"

        if len(sys.argv) >= 5 and sys.argv[4] != "":
            angle_mode = sys.argv[4].upper()

        # Perform calculation

        result = calculate(
            num1,
            operator,
            num2,
            angle_mode
        )

        # Save successful calculations to CSV

        if not isinstance(result, str) or not result.startswith("Error"):

            save_to_csv(
                num1,
                operator,
                num2,
                result
            )

        # Return result in JSON format

        print(json.dumps({
            "result": result
        }))

    except ValueError:

        print(json.dumps({
            "result": "Error: Invalid number"
        }))


if __name__ == "__main__":
    main()
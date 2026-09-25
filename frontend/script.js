const expression = document.getElementById("expression");
const result = document.getElementById("result");

let firstNumber = "";
let operator = "";


function addToDisplay(value) {

    result.textContent += value;

}


function clearDisplay() {

    expression.textContent = "";
    result.textContent = "";

    firstNumber = "";
    operator = "";

}


function setOperator(value) {

    firstNumber = result.textContent;
    operator = value;

    expression.textContent = firstNumber + " " + value;

    result.textContent = "";

}


async function calculateResult() {

    const secondNumber = result.textContent;

    if (firstNumber === "" || operator === "" || secondNumber === "") {
        result.textContent = "Error";
        return;
    }

    expression.textContent =
        firstNumber + " " + operator + " " + secondNumber;

    result.textContent = "Calculating...";

    try {

        const response = await fetch("../backend/calculate.php", {

            method: "POST",

            headers: {
                "Content-Type": "application/x-www-form-urlencoded"
            },

            body: new URLSearchParams({
                num1: firstNumber,
                operator: operator,
                num2: secondNumber
            })

        });


        if (!response.ok) {
            throw new Error("Server error");
        }


        const data = await response.json();

        result.textContent = data.result;


        // Keep the result available for the next calculation
        firstNumber = data.result;
        operator = "";
        // Apply them recieved from MySQL
        if (data.theme)
        {
            document.body.setAttribute("data-theme",data.theme);
        }

    }

    catch (error) {

        result.textContent = "Error";

        console.error(error);

    }

}


async function scientificFunction(operation) {

    const number = result.textContent;

    if (number === "") {
        result.textContent = "Error";
        return;
    }

    try {

        const response = await fetch("../backend/calculate.php", {
            method: "POST",

            headers: {
                "Content-Type": "application/x-www-form-urlencoded"
            },

            body: new URLSearchParams({
                num1: number,
                operator: operation
            })

        });


        if (!response.ok) {
            throw new Error("Server error");
        }


        const data = await response.json();

        result.textContent = data.result;

    }

    catch (error) {

        result.textContent = "Error";

        console.error(error);

    }

}
/* Simple Equation */
#include <iostream>
using namespace std;

int eval(int num1, int num2, int op) {
	switch (op) {
	case 0:
		return num1 + num2;
	case 1:
		return num1 - num2;
	case 2:
		return num1 * num2;
	case 3:
		if (num2 == 0) {
			throw runtime_error("Divided by zero");
		}
		return num1 / num2;
	case 4:
		return num1 % num2;
	}
	throw runtime_error("Unknown operator");
}

int eval(int num1, int num2, int num3, int op1, int op2) {
	// Precedence: "*/%" > "+-"
	if (op2 > 1 && op1 <= 1) {
		return eval(num1, eval(num2, num3, op2), op1);
	}
	else {
		return eval(eval(num1, num2, op1), num3, op2);
	}
}

char opToChar(int op) {
	switch (op) {
	case 0:
		return '+';
	case 1:
		return '-';
	case 2:
		return '*';
	case 3:
		return '/';
	case 4:
		return '%';
	}
	throw runtime_error("Unknown operator");
}

int main()
{
	int num1, num2, num3;
	cin >> num1 >> num2 >> num3;
	for (int s = 0; s < 25; s++) {
		try {
			int op1 = s / 5;
			int op2 = s % 5;
			if (eval(num1, num2, num3, op1, op2) == 0) {
				cout << num1 << opToChar(op1) << num2 << opToChar(op2) << num3 << "=0" << endl;
			}
		}
		catch (runtime_error ignored) {
		}
	}
	return 0;
}

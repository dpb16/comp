#include <iostream>
using namespace std;

// Recursive Fibonacci function
int fibonacciRecursive(int n) {
    if (n <= 1){
		return n;
	}
    return fibonacciRecursive(n - 1) + fibonacciRecursive(n - 2);
}

// Iterative Fibonacci function
int fibonacciIterative(int n) {
    if (n <= 1){
		return n;
	}
    int prev2 = 0, prev1 = 1, current;
    for (int i = 2; i <= n; ++i)
	 {
        current = prev1 + prev2;
        prev2 = prev1;
        prev1 = current;
    }
    return current;
}

int main() {
    int n, choice;
    cout << "Enter Fibonacci position: ";
    cin >> n;

    cout << "Choose method (1 - Recursive, 2 - Iterative): ";
    cin >> choice;

    switch (choice) {
        case 1:
            cout << "Fibonacci (Recursive): " << fibonacciRecursive(n) << endl;
            break;
        case 2:
            cout << "Fibonacci (Iterative): " << fibonacciIterative(n) << endl;
            break;
        default:
            cout << "Invalid choice!" << endl;
    }

    return 0;
}


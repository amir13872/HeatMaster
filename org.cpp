#include <iostream>
#include <cmath>
#include <string>
#include <Windows.h>

using namespace std;

class HeatCalculator {
public:
    double calculate_c(double Q, double m, double delta_T) {
        return Q / (m * delta_T);
    }

    double calculate_Q(double c, double m, double delta_T) {
        return c * m * delta_T;
    }

    double calculate_m(double Q, double c, double delta_T) {
        return Q / (c * delta_T);
    }

    double calculate_delta_T(double Q, double c, double m) {
        return Q / (c * m);
    }

    double calculate_T2(double Q, double m, double c, double T1) {
        return (Q / (c * m)) + T1;
    }

    void run() {
        while (true) {
            system("cls");
            system("color 0b");
            cout << "\nIn the name of God, the Most Gracious, the Most Merciful\n";
            cout << "I, Amir Mahdi Zare, a 10th grade math student at Dr. Mehdi Torkzadeh High School,\n";
            cout << "am honored to present this program for calculating heat, heat capacity, and specific heat\n";
            cout << "based on the heat formula from Chapter 4 of 10th grade physics.\n";
            cout << "Instructor: Mr. Hassanzadeh Moghadam\n";
            cout << "Programmer: Amir Mahdi Zare\n\n";

            cout << "For calculating specific heat capacity (c) : c\n";
            cout << "For calculating heat (Q) : q\n";
            cout << "For calculating mass (m) : m\n";
            cout << "For calculating temperature difference (ΔT) : t\n";
            cout << "For calculating second temperature (T2) : t2\n";
            cout << "For exit : exit\n";

            string choice;
            cout << "Enter your choice: ";
            cin >> choice;

            if (choice == "exit") {
                cout << "Goodbye!\n";
                break;
            }

            else if (choice == "c") {
                double Q, m, delta_T;
                cout << "Enter heat (Q) in joules: ";
                cin >> Q;
                cout << "Enter mass (m) in kilograms: ";
                cin >> m;
                cout << "Enter temperature difference (ΔT) in degrees Celsius: ";
                cin >> delta_T;

                double c = calculate_c(Q, m, delta_T);
                cout << "Specific heat capacity (c) is: " << c << " joules per kilogram per degree Celsius\n";
            }

            else if (choice == "q") {
                double c, m, delta_T;
                cout << "Enter specific heat capacity (c) in joules per kilogram per degree Celsius: ";
                cin >> c;
                cout << "Enter mass (m) in kilograms: ";
                cin >> m;
                cout << "Enter temperature difference (ΔT) in degrees Celsius: ";
                cin >> delta_T;

                double Q = calculate_Q(c, m, delta_T);
                cout << "Heat (Q) is: " << Q << " joules\n";
            }

            else if (choice == "m") {
                double Q, c, delta_T;
                cout << "Enter heat (Q) in joules: ";
                cin >> Q;
                cout << "Enter specific heat capacity (c) in joules per kilogram per degree Celsius: ";
                cin >> c;
                cout << "Enter temperature difference (ΔT) in degrees Celsius: ";
                cin >> delta_T;

                double m = calculate_m(Q, c, delta_T);
                cout << "Mass (m) is: " << m << " kilograms\n";
            }

            else if (choice == "t") {
                double Q, c, m;
                cout << "Enter heat (Q) in joules: ";
                cin >> Q;
                cout << "Enter specific heat capacity (c) in joules per kilogram per degree Celsius: ";
                cin >> c;
                cout << "Enter mass (m) in kilograms: ";
                cin >> m;

                double delta_T = calculate_delta_T(Q, c, m);
                cout << "Temperature difference (ΔT) is: " << delta_T << " degrees Celsius\n";
            }

            else if (choice == "t2") {
                double Q, c, m, T1;
                cout << "Enter heat (Q) in joules: ";
                cin >> Q;
                cout << "Enter specific heat capacity (c) in joules per kilogram per degree Celsius: ";
                cin >> c;
                cout << "Enter mass ( m) in kilograms: ";
                cin >> m;
                cout << "Enter initial temperature (T1) in degrees Celsius: ";
                cin >> T1;

                double T2 = calculate_T2(Q, m, c, T1);
                cout << "Second temperature (T2) is: " << T2 << " degrees Celsius\n";
            }

            else {
                cout << "Invalid input! Please enter 'c', 'q', 'm', 't', 't2', or 'exit'.\n";
            }
        }
    }
};

int main() {
    HeatCalculator calculator;
    calculator.run();
    return 0;
}

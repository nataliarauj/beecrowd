#include <iostream>

using namespace std;

int torre_hanoi(int n, char origem, char destino, char auxiliar) {
    if (n == 1) {
        return 1;
    }

    int movimentos = torre_hanoi(n - 1, origem, auxiliar, destino);
    movimentos += 1;
    movimentos += torre_hanoi(n - 1, auxiliar, destino, origem);
    return movimentos;
}

int main() {
    int teste = 1;
    while (true) {
        int n;
        cin >> n;
        if (n == 0) {
            break;
        }

        int total_movimentos = torre_hanoi(n, 'A', 'C', 'B');

        cout << "Teste " << teste << endl;
        cout << total_movimentos << endl;
        cout << endl;
        
        teste++;
    }

    return 0;
}
#include <iostream>

int main() {
    int a, n;
    std::cin >> a >> n;

    while (n <= 0) {
        std::cin >> n; 
    }

    int soma = 0;
    for (int i = 0; i < n; ++i) {
        soma += a;
        ++a;
    }

    std::cout << soma << std::endl;
    return 0;
}
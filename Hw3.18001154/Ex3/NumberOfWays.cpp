#include <iostream>
#include <conio.h>
using namespace std;

void input(int &m, int &n)
{
    cout << "Nhap so phan thuong m =  ";
    cin >> m;
    cout << "Nhap so học sinh n =  ";
    cin >> n;
}

int part(int m, int n)
{
    if (m == 0)
        return 1;
    else if (n == 0)
        return 0;
    else if (m == 1 || n == 1)
        return 1;
    else if (m < n)
        return part(m, m);
    else
        return part(m, n - 1) + part(m - n, n);
}
void output(int m, int n)
{
    cout << m << " phan thuong, " << n << " sinh vien se co " << part(m, n) << " cach chia";
}

int main()
{
    int m, n;
    input(m, n);
    output(m, n);
    getch();
    return 0;
}
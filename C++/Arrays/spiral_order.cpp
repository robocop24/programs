#include <iostream>
using namespace std;

int main()
{
    /* m-rows n-columns T-TopMost B-BottomMost L-Leftmost R-RightMost */
    int m, n, T, B, L, R;

    cin >> m >> n;
    T = 0, B = m - 1, L = 0, R = n - 1;

    int arr[m][n];

    for (int i = 0; i < m; i++)
    {
        for (int j = 0; j < n; j++)
        {
            int value;
            cin >> value;
            arr[i][j] = value;
        }
    }

    for (int i = 0; i < m; i++)
    {
        for (int j = 0; j < n; j++)
        {
            cout << arr[i][j] << " ";
        }
        cout << "\n";
    }

    cout << "\n";

    int dir = 0;
    while (T <= B && L <= R)
    {

        // dir -> 0 ,move left to right
        if (dir == 0)
        {

            for (int i = L; i <= R; i++)
            {
                cout << arr[T][i] << " ";
            }
            T++;
        }
        // dir -> 1 ,move top to bottom
        else if (dir == 1)
        {
            for (int i = T; i <= B; i++)
            {
                cout << arr[i][R] << " ";
            }
            R--;
        }
        // dir -> 2 ,move right to left
        else if (dir == 2)
        {
            for (int i = R; i >= L; i--)
            {
                cout << arr[B][i] << " ";
            }
            B--;
        }
        // dir -> 3 ,move bottom to top
        else if (dir == 3)
        {
            for (int i = B; i >= T; i--)
            {
                cout << arr[i][L] << " ";
            }
            L++;
        }
        dir = (dir + 1) % 4;
    }
}
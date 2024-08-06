// searching for an element in usorted array
#include <iostream>

int linearSearch(int array[], int n, int val)
{
    for (int i = 0; i < n; i++)
    {
        if (array[i] == val)
            return i;
    }
    return -1;
}


int main()
{
    int array[] = {1, 2, 3, 4, 5};
    int length = sizeof(array) / sizeof(array[0]);
    int value = 5;
    std::cout << linearSearch(array, length, value);
}
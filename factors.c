#include <stdio.h>

int main()
{
    long long int num = 239809320265259;
    long int factor_one = 2;
    long int factor_two;

    while (num % factor_one)
    {
        if (factor_one <= num)
        {
            factor_one++;
        }
        else
        {
            return (-1);
        }
    }

    factor_two = num / factor_one;
    printf("%lld = %ld * %ld\n", num, factor_two, factor_one);
    return (0);
}

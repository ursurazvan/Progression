#include <stdio.h>
using namespace std;

int main(int p1, int p2, int p3, int u0, int n)
{
    long long res=u0;
    for(int i=1; i<=n; i++){
        res=(p1+res)+(i*p2*p3);
    }
    printf("%lld", res);
    return 0;
}


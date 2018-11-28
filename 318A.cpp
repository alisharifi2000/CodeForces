#include <iostream>
#include <cmath>
using namespace std;

int main()
{
    long long int n,k;
    cin>>n>>k;
    if(n%2==0)
    {
        if(k<=n/2)
        {
            cout<<(2*k)-1;
        }
        else
        {
            k=k-(n/2);
            cout<<2*k;
        }
    }
    else if(n%2!=0)
    {
        long long int m;
        m=floor(n/2);
        if(k<=m+1)
        {
            cout<<(2*k)-1;
        }
        else
        {
            k=k-(m+1);
            cout<<2*k;
        }
    }
    return 0;
}

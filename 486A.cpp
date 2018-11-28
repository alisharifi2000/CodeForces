#include <iostream>
#include <cmath>

using namespace std;

int main()
{
    long long int n;
    cin>>n;
    long long int r;
    long long int b;
    r= n/2;
    b= n%2;
    if(b==0)
    {
        cout<<r;
    }
    else if(b==1)
    {
        cout<<r-n;
    }

}

#include <iostream>

using namespace std;

int main()
{
    int num;
    int price;
    int money;
    int sum=0;
    cin>>price;
    cin>>money;
    cin>>num;
    sum = price*(num*(num+1))/2;
    if(sum<=money)
    {
        cout<<0;
    }
    else
    {
        cout<<sum-money;
    }
}

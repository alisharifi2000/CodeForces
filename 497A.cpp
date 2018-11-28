#include <iostream>

using namespace std;

int main()
{
    int n;
    cin>>n;
    int num[n][2];
    for(int i=0;i<n;i++)
    {
        for(int j=0;j<2;j++)
        {
            cin>>num[i][j];
        }
    }
    int counter=0;
    for(int i=0;i<n;i++)
    {
        if((num[i][1]-num[i][0])>=2)
        {
            counter++;
        }
    }
    cout<<counter;

}

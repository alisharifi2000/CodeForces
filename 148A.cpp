#include <iostream>

using namespace std;

int main()
{
    int k,l,m,b;
    int counter=0;
    cin>>k>>l>>m>>b;
    int n;
    cin>>n;
    int num[n];
    for(int i=0;i<n;i++)
    {
        num[i]=(i+1);
    }
    for(int i=l-1;i<n;i=i+l)
    {
        num[i]=0;
    }
    for(int i=m-1;i<n;i=i+m)
    {
        num[i]=0;
    }
    for(int i=k-1;i<n;i=i+k)
    {
        num[i]=0;
    }
    for(int i=b-1;i<n;i=i+b)
    {
        num[i]=0;
    }
    for(int i=0;i<n;i++)
    {
        if(num[i]==0)
        {
            counter++;
        }
    }
    cout<<counter;
}

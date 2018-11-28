#include <iostream>

using namespace std;

int main()
{
    long long int min1,max1;
    int n;
    int counter=0;
    cin>>n;
    int mat[n];
    cin>>mat[0];
    min1=mat[0];
    max1=mat[0];
    for(int i=1;i<n;i++)
    {
        cin>>mat[i];
        if(mat[i]>max1)
        {
            max1=mat[i];
            counter++;
        }
        else if(mat[i]<min1)
        {
            min1=mat[i];
            counter++;
        }
    }
    cout<<counter;
    return 0;
}

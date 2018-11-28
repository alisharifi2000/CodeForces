#include <iostream>
#include <vector>
using namespace std;

int main()
{
    int n;
    int counter =0;
    cin>>n;
    int mat[n][2];
    for(int i=0; i<n;i++)
    {
        for(int j=0;j<2;j++)
        {
            cin>>mat[i][j];
        }
    }
    for(int i=0;i<n;i++)
    {
        for(int j=1;j<n;j++)
        {
            if(i+j<n)
            {
                if(mat[i][0]== mat[i+j][1])
               {
                counter++;
               }
            }
        }
    }
    for(int i=0;i<n;i++)
    {
        for(int j=1;j<n;j++)
        {
            if(i+j<n)
            {
                if(mat[i][1]== mat[i+j][0])
                {
                 counter++;
                }
            }
        }
    }
    cout<<counter;

}

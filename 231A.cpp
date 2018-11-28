#include <iostream>

using namespace std;
int main()
{
    int n, counter=0,sum=0;
    cin>>n;
    int mat[n][3];
    for(int i=0;i<n;i++)
    {
       for(int j=0;j<3;j++)
          {
          cin>>mat[i][j];
          }
    }
    for(int i=0;i<n;i++)
    {
       sum=mat[i][0]+mat[i][1]+mat[i][2];
       if(sum>=2)
       {
           counter++;
       }
       sum=0;
    }
cout<<counter;
return 0;
}

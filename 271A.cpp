#include <iostream>

using namespace std;

int main()
{
    int n,r1,r2,r3,r4;
    cin>>n;
    n++;
    int flag =0;
   while(flag !=1)
 {
      r1=n/1000;
      r2=(n-(r1*1000))/100;
      r3=(n-(1000*r1+100*r2))/10;
      r4=(n%10);
      if(r1==r2)
     {
          n=n+1;
     }
     else if(r1==r3)
     {
         n=n+1;
     }
     else if(r1==r4)
     {
         n=n+1;
     }
     else if(r2==r3)
     {
         n=n+1;
     }
     else if(r2==r4)
     {
         n=n+1;
     }
     else if(r3==r4)
     {
         n=n+1;
     }
      else
     {
          flag= 1;
     }
 }
    cout<<n;
    return 0;
}

#include <iostream>

using namespace std;

int main()
{
   long long n;
   cin>>n;
   long long c =0;
   long long int n1=0;
   long long int n2=0;
   long long int n3=0;
   long long int n4=0;
   int num[n];
   for(long long int i=0;i<n;i++)
   {
       cin>>num[i];
       if(num[i]==1)
       {
           n1++;
       }
       else if(num[i]==2)
       {
           n2++;
       }
       else if(num[i]==3)
       {
           n3++;
       }
       else if(num[i]==4)
       {
           n4++;
       }
   }
   c=c+n4;
   n4=0;
   if(n==n1&&(n1%4!=0))
   {
       c=c+(n1/4)+1;
       n1=0;
   }
   else if(n==n1&n1%4==0)
   {
       c=c+(n1/4);
       n1=0;
   }

   if(n3>n1)
   {
       c=c+n3;
       n1=0;
       n3=0;
   }
   else if(n1>n3)
   {
       c=c+n3;
       n1=n1-n3;
       n3=0;
   }
   else if(n1==n3)
   {
       c=c+n3;
       n1=0;
       n3=0;
   }
   if(n2%2==0)
   {
       c=c+(n2/2);
       n2=0;
   }
   else if(n2%2!=0)
   {
       c=c+(n2/2);
       n2=1;
       if(n1<=2)
       {
           c++;
           n2=0;
           n1=0;
       }
       else if(n1<=6&&n1>=3)
       {
           c=c+2;
           n1=0;
           n2=0;
       }
       else if(n1>6)
       {
           c++;
           n2=0;
           n1=n1-2;
           if(n1%4==0)
           {
               c=c+(n1/4);
               n1=0;
           }
           else if(n1%4!=0)
           {
               c=c+(n1/4)+1;
               n1=0;
           }
       }
   }
   if(n1>0)
   {
       if(n1%4!=0)
       {
           c=c+(n1/4)+1;
           n1=0;
       }
       else if (n1%4==0)
       {
           c=c+(n1/4);
           n1=0;
       }
   }
   cout<<c;
}

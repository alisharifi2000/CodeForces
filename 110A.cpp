#include <iostream>
#include <string>
using namespace std;
int main()
{
   string num;
   cin>>num;
   long long int counter4=0;
   long long int counter7=0;
   for(long long int i=0;i<=num.size();i++)
   {
       if((num[i]=='4'))
       {
           counter4++;
       }
       else if((num[i]=='7'))
       {
           counter7++;
       }
   }
   if((counter4+counter7)==num.size()&&counter4!=0 && counter7!=0)
   {
       if(counter4+counter7==7||counter4+counter7==4)
       {
       cout<<"YES";
       }
       else 
       {
           cout<<"NO";
       }
   }
   else if(counter4+counter7==7||counter4+counter7==4)
   {
       cout<<"YES";
   }
   else
   {
       cout<<"NO";
   }
}

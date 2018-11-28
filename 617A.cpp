#include <iostream>

using namespace std;

int main()
{
   int n;
   cin>>n;
   int counter=0;
   int i=5;

   while(n>0 && i>0)
   {
       counter =n/i+counter;
       n=n%i;
       i--;
   }
   cout<<counter;

}

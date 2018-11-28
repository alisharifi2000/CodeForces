#include <iostream>

using namespace std;

int main()
{
   int n;
   cin>>n;
   int counter =0;
   while(n>=(counter*(counter+1))/2)
   {
     n=n-(counter*(counter+1))/2;
     counter++;
   }
   cout<<counter-1;


}

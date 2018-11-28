#include <iostream>
#include <cmath>
#include <algorithm>
using namespace std;

int main()
{
   int n1,n2,n3;
   cin>>n1>>n2>>n3;
   int d1,d2,d3;
   int m;
   d1=abs(n1-n2);
   d2=abs(n2-n3);
   d3=abs(n3-n1);
   m=(max(max(d1,d2),d3));
   cout<<d1+d2+d3-m;
}

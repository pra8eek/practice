#include<iostream>
using namespace std;
void bin(int n)
{
  if( n==0 || n==1 )
    cout<<n;
  else
  {
    bin(n/2);
    cout<<n%2;
  }
}

int main()
{
  int a=5, b=9;
  bin(5);
  cout<<"\n";
  bin(b);
  return 0;
}

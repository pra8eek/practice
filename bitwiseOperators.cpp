#include<bits/stdc++.h>
using namespace std;
void bin(int n) //to convert decimal to binary
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
  int x=13;
  cout<<x<<" in binary is : ";
  bin(x);
  cout<<endl;
  cout<<x<<" multiplied by 4 is "<<(x<<2)<<endl;
  cout<<x<<" divided by 2 is "<<(x>>1)<<endl;
  return 0;
}

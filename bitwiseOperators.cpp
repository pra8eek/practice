// The things we can do with binary operators :
// Multiply/Divide by 2
// Finding even/odd
// Finding 1's and 2's compliment
// Finding if the number is a power of 2

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
  int x=15;

  cout<<x<<" in binary is : ";
  bin(x);
  cout<<endl;

  cout<<x<<" multiplied by 4 is "<<(x<<2)<<endl;
  cout<<x<<" divided by 2 is "<<(x>>1)<<endl;

  ( x & 1 )? cout<<x<<" is odd\n" : cout<<x<<" is even\n";

  cout<<"1's complement of "<<x<<" is "<<(~x)<<endl;
  cout<<"2's complement of "<<x<<" is "<<(~x + 1)<<endl;

  (!(x & (x - 1))) ? cout<<x<<" is a power of 2\n" : cout<<x<<" is NOT a power of 2\n";
  return 0;
}

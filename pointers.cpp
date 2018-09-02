#include<bits/stdc++.h>
using namespace std;
int main()
{
  int *p;
  p = new int(10);
  cout<<"Value = "<<*p<<", Address = "<<p<<endl;
  delete p;

  //Array as pointer
  int arr[5]={1,2,3,4,5};
  int *ptr;
  ptr = new int;
  ptr = arr ;
  cout<<"Array traversing through pointer : ";
  cout<<ptr[0]<<" "<<ptr[1]<<" "<<ptr[2]<<" "<<ptr[3]<<" "<<ptr[4]<<endl;
  return 0;
}

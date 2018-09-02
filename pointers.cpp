#include<bits/stdc++.h>
using namespace std;

void increment(void* ptr , int size)
{
  if( size == sizeof(char))
  {
    char *ch;
    ch = (char*) ptr ;
    (*ch)++;
  }
  else if( size == sizeof(int))
  {
    int *n;
    n = (int*) ptr ;
    (*n)++;
  }
}

int main()
{
  int* p;
  p = new int(10);
  cout<<"Value = "<<*p<<", Address = "<<p<<endl;
  delete p;

  //Array as pointer
  int arr[5]={1,2,3,4,5};
  p = new int;
  p = arr ;
  cout<<"Array traversing through pointer : ";
  cout<<p[0]<<" "<<p[1]<<" "<<p[2]<<" "<<p[3]<<" "<<p[4]<<endl;

  //for 2D array : arr[i][j] = *(*(arr + i) + j)

/**int num[2][3] = {{1,2,3},{7,8,9}};
  int** ptr;
  ptr  = num ;
  for(int i=0;i<2;i++)
    for(int j=0;j<3;j++)
      cout<<*(*(ptr +i)+j)<<" ";
  cout<<endl;*/

  //illustration of void pointer
  int a = 10;
  char c = 'x';
  cout<<"BEFORE : int is "<<a<<" and char is "<<c<<endl;
  increment(&a,sizeof(a));
  increment(&c,sizeof(c));
  cout<<"AFTER : int is "<<a<<" and char is "<<c<<endl;

  //pointers to pointers
  int n = 3 ;
  int* q;
  int** r;
  q = &n;
  r = &q;
  cout<<"n = "<<n<<endl;
  cout<<"*q = "<<*q<<", &q = "<<&q<<endl;
  cout<<"**r = "<<**r<<", &r = "<<&r<<endl;
  return 0;
}

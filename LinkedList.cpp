#include<iostream>
#define endl "\n"
using namespace std;
class Node
{
    public :
        int val;
        Node* next;
        Node()
        {
            val = 0;
            next = NULL;
        }
        Node(int v) 
        { 
            val = v;
            next = NULL;
        }
};

class LinkedList
{
    Node top;
    Node temp;
    public :
        void insert( int n )
        {
            // std :: cout<<"Insert function invoked";
            // if(top.next == NULL)
            // {
            //     // std::cout<<"If me to aa gaya";
            //     top.val = n;
            //     top.next = &temp;
            // }
            // else
            // {
            //     // std::cout<<"else me aa gaya";
            //     temp.val = n;
            //     // temp.next = &temp;
            //     temp.next=NULL;

            // }  

            Node n=top;
            // cout<<n.next;       
        }
        void show()
        {
            if( top.next == NULL )
                std :: cout<<"List is empty"<<endl;
            else
            {
                Node n = top;
                while( n.next != NULL )
                {
                    std :: cout<<n.val<<" ";
                    n = *n.next;
                }
            }
        }
};

int main()
{
    LinkedList l;
    l.show();
    // std::cout<<"Show tak ho gaya"<<endl;
    l.insert(5);
    l.insert(10);
    l.insert(15);
    // std::cout<<"Insert bhi ho gaya badka ji"<<endl;
    // l.show();
    return 0;
}
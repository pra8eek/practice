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
            std :: cout<<n<<" inserted"<<endl;
            if(top.next == NULL)
            {
                top.val = n;
                top.next = &temp;
                int x;
            }
            else
            {
                Node temp(n);
                temp.next = top.next;
                top.next = & temp;
            }
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
                    std :: cout<<n.val;
                    n = *n.next;
                }
            }
        }
        Node* deleteNode(Node *head, int i) {
        if(i == 0)
        {
            Node* temp = head;
            head = head->next;
            delete temp;
            return head;
        }
        int k = 0;
        Node* temp = head;
        while(k < i-1 && temp->next != NULL)
        {
            k++;
            temp = temp->next;
        }
        if(temp == NULL)
        {
            return head;
        }
        Node* to_be_deleted = temp->next;
        temp->next = to_be_deleted->next;
        delete to_be_deleted;
        return head;

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
    l.show();
    return 0;
}

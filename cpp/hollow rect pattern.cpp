#include<iostream>
using namespace std;
int main()
{
    cout<<"Enter the length and breadth of the rect\n";
    int l,b;
    cin>>l>>b;
    for(int i = 0; i<l; i++)
    {
        for(int j = 0; j<b; j++)
        {
            if(i==0 || i==l-1 || j==0 || j==b-1) 
                cout<<"*";
            else
                cout<<" ";
        }
        cout<<"\n";
    }
}
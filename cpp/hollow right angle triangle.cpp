#include<iostream>
using namespace std;
int main()
{
    cout<<"Enter the height of the triangle\n";
    int l;
    cin>>l;
    for(int i = 0; i<l; i++)
    {
        for(int j = 0; j<=i; j++)
        {
            if(j==0||j==i||i==l-1)
            cout<<"*";
            else
            cout<<" ";
        }
        cout<<"\n";
    }
}
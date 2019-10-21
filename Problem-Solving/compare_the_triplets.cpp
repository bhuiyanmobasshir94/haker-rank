#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    
    int a[3];
    int b[3];
    
    int alice =0;
    int bob =0;
    
    for(int i=0;i<3;i++)
        {
        cin>>a[i];
    }
        for(int i=0;i<3;i++)
        {
        cin>>b[i];
    }
        for(int i=0;i<3;i++)
        {
           if(a[i] > b[i]) alice +=1;
           else if(a[i] < b[i]) bob +=1;
           else { alice +=0; bob +=0;}
        }
     cout << alice<< " " << bob;
    
    return 0;
}

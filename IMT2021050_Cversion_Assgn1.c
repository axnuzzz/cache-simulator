#include<stdio.h>
#include<stdlib.h>

int Addition(int a,int b,int c,int d,int e,int f,int g,int h,int i,int j,int k,int l,int m,int n,int o){

    int p = (a+b+c+d+e+f+g+h+i+j+k+l+m+n+o);
    return p;
}
int Subtraction(int a,int b,int c,int d,int e,int f,int g,int h,int i,int j,int k,int l,int m,int n,int o){

    int p = (a-b-c-d-e-f-g-h-i-j-k-l-m-n-o);
    return p;
}
int Average(int a,int b,int c,int d,int e,int f,int g,int h,int i,int j){
    int p = (a+b+c+d+e+f+g+h+i+j)/10 ;
    return p;
}

int main(){

    int x;

    printf("Select 1 for addition, 2 for subtraction and 3 for average of 10 numbers");
    scanf("%d",&x);

    int a,b,c,d,e,f,g,h,i,j,k,l,m,n,o;

    if (x==1)
    {
        scanf("%d",&a);
        scanf("%d",&b);
        scanf("%d",&c);
        scanf("%d",&d);
        scanf("%d",&e);
        scanf("%d",&f);
        scanf("%d",&g);
        scanf("%d",&h);
        scanf("%d",&i);
        scanf("%d",&j);
        scanf("%d",&k);
        scanf("%d",&l);
        scanf("%d",&m);
        scanf("%d",&n);
        scanf("%d",&o);

        printf("%d", Addition(a,b,c,d,e,f,g,h,i,j,k,l,m,n,o));
    }
    else if (x==2)
    {
        scanf("%d",&a);
        scanf("%d",&b);
        scanf("%d",&c);
        scanf("%d",&d);
        scanf("%d",&e);
        scanf("%d",&f);
        scanf("%d",&g);
        scanf("%d",&h);
        scanf("%d",&i);
        scanf("%d",&j);
        scanf("%d",&k);
        scanf("%d",&l);
        scanf("%d",&m);
        scanf("%d",&n);
        scanf("%d",&o);

        printf("%d", Subtraction(a,b,c,d,e,f,g,h,i,j,k,l,m,n,o));
    }else if (x==3)
    {
        scanf("%d",&a);
        scanf("%d",&b);
        scanf("%d",&c);
        scanf("%d",&d);
        scanf("%d",&e);
        scanf("%d",&f);
        scanf("%d",&g);
        scanf("%d",&h);
        scanf("%d",&i);
        scanf("%d",&j);

        printf("%d", Average(a,b,c,d,e,f,g,h,i,j));
    }
    
    return 0;
}
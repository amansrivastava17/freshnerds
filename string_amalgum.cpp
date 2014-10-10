#include<iostream>
#include<string>
#include<stdio.h>
#include<stdlib.h>
using namespace std;

//nlogn complexity to find amalgum words in two string

//structure to store sum product and no of character for each word
struct arr
{
    int arrsum;
    unsigned long long int arrpro;
    int arrchar;
};
template<class t1>void merge1(t1 *arr, int l, int m, int r);
template<class t1>void merge_sort(t1 *arr, int l, int r);
int main()
{
    struct arr s1[20];
    struct arr s2[20];
    int s=0;
    int a[]={1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26};   //value assign to each alphabets
    char string1[100];
    char string2[100];
    for(s=0;s<20;s++)
    {
        s1[s].arrsum=0;
        s2[s].arrsum=0;
        s1[s].arrpro=1;
        s2[s].arrpro=1;
        s1[s].arrchar=0;
        s2[s].arrchar=0;

    }

    int i=0,k=0,l=0,j=0,m=0,word_count_amalgum=0;
    cout<<"\nEnter string1 :";
    cin.getline(string1,100);
    cout<<"\nEnter string2 :";
    cin.getline(string2,100);
    //cout<<string1<<"  "<<string2;
    while(string1[i]!='\0')
    {
        if(string1[i]==' ')
            k++;
        else
        {
        s1[k].arrsum=s1[k].arrsum+a[string1[i]-'a'];
        s1[k].arrpro=s1[k].arrpro*a[string1[i]-'a'];
        s1[k].arrchar++;
        }
        i++;
    }
    i=0;
    while(string2[i]!='\0')
    {
        if(string2[i]==' ')
            l++;
        else
        {
            s2[l].arrsum=s2[l].arrsum+a[string2[i]-'a'];
            s2[l].arrpro=s2[l].arrpro*a[string2[i]-'a'];
            s2[l].arrchar++;
        }
        i++;
    }
    i=0;
    j=0;

    merge_sort(s1,0,k);
    merge_sort(s2,0,l);

    //calculate similar sum (amalgum words) in both structure array
    if(k==l)
    {
        while(i<=k&&j<=l)
        {

            if(s1[i].arrsum==s2[j].arrsum&&s1[i].arrpro==s2[j].arrpro&&s1[i].arrchar==s2[j].arrchar)
            {

                word_count_amalgum++;
                i++;
                j++;
            }
            else if(s1[i].arrsum>s2[j].arrsum)
                j++;
            else
                i++;
        }
    }
    if(word_count_amalgum==k+1)
        cout<<"strings are amalgum";
    else
        cout<<"Strings are not amalgum";
return 0;
}
template<class t1>void merge1(t1 *s, int l, int m, int r)
{
    int i, j, k;
    int n1 = m - l + 1;
    int n2 =  r - m;

    struct arr L[n1], R[n2];

    for(i = 0; i < n1; i++)
        L[i] = s[l+i];
    for(j = 0; j < n2; j++)
        R[j] = s[m+1+j];

    i = 0;
    j = 0;
    k = l;
    while (i < n1 && j < n2)
    {
        if (L[i].arrsum <= R[j].arrsum)
        {
            s[k] = L[i];
            i++;
        }
        else
        {
            s[k] = R[j];
            j++;
        }
        k++;
    }

    while (i < n1)
    {
        s[k] = L[i];
        i++;
        k++;
    }
    while (j < n2)
    {
        s[k]= R[j];
        j++;
        k++;
    }
}
template<class t1>void merge_sort(t1* s, int l, int r)
{
    if (l < r)
    {
        int m = l+(r-l)/2;
        merge_sort(s, l, m);
        merge_sort(s, m+1, r);
        merge1(s, l, m, r);
    }
}

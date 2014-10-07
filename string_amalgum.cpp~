#include<iostream>
#include<stdio.h>u
#include<string.h>
using namespace std;
//nlogn complexity to find amalgum words in two string
void merge1(int arr[], int l, int m, int r);
void merge_sort(int arr[], int l, int r);
int main()
{
    int a[]={1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26};   //value assign to each alphabets
    char string1[100];
    char string2[100];
    int arr1[20]={0};                                                                 //array to store sum of each word of string1
    int arr2[20]={0};                                                                 //array to store sum of each word of string2
    int i=0,k=0,l=0,j=0,word_count_amalgum=0;
    cout<<"\nEnter string1 :";
    gets(string1);
    cout<<"\nEnter string2 :";
    gets(string2);
    //calculate sum of each word in arr1(string1)
    while(string1[i]!='\0')
    {
        if(string1[i]==' ')
            k++;
        else
        arr1[k]=arr1[k]+a[string1[i]-'a'];
        i++;

    }
    i=0;
    //calculate sum of each word in arr2(string2)
    while(string2[i]!='\0')
    {
        if(string2[i]==' ')
            l++;
        else
        arr2[l]=arr2[l]+a[string2[i]-'a'];
        i++;

    }
    //cout<<"**"<<arr1[1]<<"**"<<arr2[0]<<"**";
    i=0;
    //sort both arrays
    merge_sort(arr1,0,k);
    merge_sort(arr2,0,l);
    //calculate similar sum (amalgum words) in both array
    while(i<=k&&j<=l)
    {
        if(arr1[i]==arr2[j])
        {
            word_count_amalgum++;
            i++;
            j++;
        }
        else if(arr1[i]>arr2[j])
            j++;
        else
            i++;
    }
    cout<<"\nNumber of amalgum words are : "<<word_count_amalgum;
return 0;
}
void merge1(int arr[], int l, int m, int r)
{
    int i, j, k;
    int n1 = m - l + 1;
    int n2 =  r - m;

    int L[n1], R[n2];

    for(i = 0; i < n1; i++)
        L[i] = arr[l + i];
    for(j = 0; j < n2; j++)
        R[j] = arr[m + 1+ j];

    i = 0;
    j = 0;
    k = l;
    while (i < n1 && j < n2)
    {
        if (L[i] <= R[j])
        {
            arr[k] = L[i];
            i++;
        }
        else
        {
            arr[k] = R[j];
            j++;
        }
        k++;
    }

    while (i < n1)
    {
        arr[k] = L[i];
        i++;
        k++;
    }
    while (j < n2)
    {
        arr[k] = R[j];
        j++;
        k++;
    }
}
void merge_sort(int arr[], int l, int r)
{
    if (l < r)
    {
        int m = l+(r-l)/2;
        merge_sort(arr, l, m);
        merge_sort(arr, m+1, r);
        merge1(arr, l, m, r);
    }
}


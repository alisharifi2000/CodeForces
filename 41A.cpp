#include <iostream>
#include <string>
using namespace std;

int main()
{
    string word;
    string word1;
    char temp;
    cin>>word;
    int i = word.size()-1;
    int j=0;
    while(i>j)
    {
        temp = word [i];
        word [i] = word [j];
        word [j] = temp;
        i--;
        j++;
    }
    int counter=0;
    cin>>word1;
    int num = word.size();
    int num1 = word1.size();
    if(num != num1)
    {
        cout<<"NO";
    }
    else
    {
        for(int l=0;l<num;l++)
        {
            if(word1[l]==word[l])
            {
                counter++;
            }
        }
        if(counter== num)
        {
         cout<<"YES";
        }
        else
        {
        cout<<"NO";
        }
    }

}

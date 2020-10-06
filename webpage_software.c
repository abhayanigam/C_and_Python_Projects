#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int main()
{
    //to open a any website.
    /*char site[]= "explorer https://";
    char url[30];
    printf("Enter website url :");
    scanf("%s",url);
    strcat(site,url);
    system(site);*/

    //to open this website online.
    //system("explorer https://www.youtube.com");
    
    //to open any software.
    char soft[] = "cmd /c";
    char name[30];
    printf("Enter software name :");
    scanf("%s",name);
    strcat(soft,name);
    system(soft);
}
//Simple assistant NAMETINA BY: Abhaya Nigam.

#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define RESET               "\033[0m"
#define BOLDYELLOW          "\033[1m\033[33m"
#define BOLDRED             "\033[1m\033[31m"
#define BOLD_ITALIC         "\e[3m\e[1m"
#define STYLE_UNDERLINE     "\033[4m"
#define BOLDWHITE           "\033[1m\033[37m"
#define BOLDGREEN           "\033[1m\033[32m" 
#define BOLDBLUE            "\033[1m\033[34m" 

char sign(char name[15]);
char enteries(char ent[5]);

void fordelay(int j)
{
    int i, k;
    for (i = 0; i < j; i++)
        k = i;
}

int main()
{
    printf("\t\t\t\xB2\xB2\xB2" BOLDRED" Nametina your"RESET BOLDWHITE" smart"RESET BOLDGREEN" typing assistant. "RESET "\xB2\xB2\xB2\xB2\n");

    char hello[10], name[15], ans[3], ent[5];
start:
    printf("Say Hello to start: ");
    scanf("%s", hello);
    puts((strcmp(hello, "hello") == 0) ? "Hey !! there\n" : "i can't understand what you say\n");
    if (strcmp(hello, "hello") != 0)
    {
        goto start;
    }
    sign(name);
run:
    printf("To seaarch web page type " BOLDYELLOW "(web)" RESET " and for software type " BOLDRED "(soft)" RESET"\n:-");
    scanf("%s", ent);
    enteries(ent);

    printf("\n");
    printf(STYLE_UNDERLINE BOLD_ITALIC "\tWant's to search again ?\n" RESET);
    printf("Then enter yes for search again & no for exit :");
    scanf("%s", ans);
    puts((strcmp(ans, "yes") == 0) ? " " : BOLDBLUE "\nExiting the program .............\n"RESET);
    if ((strcmp(ans, "yes") == 0))
    {
        goto run;
    }
    else
    {
        exit(0);
    }
    return 0;
}

char sign(char name[15])
{
    printf("So, for better understanding please tell me your name : ");
    scanf("%s", name);
    printf("\n");
    printf("hey !!"BOLDYELLOW" %s" RESET " nice to meet you.\n", name);

    system("pause");
    system("cls"); 

    printf("\n\nLOADING");
        for (int i = 0; i <= 5; i++)
        {
            fordelay(1000000000);
            printf(".");
        }

    printf("\n");

    printf("So, My name is Nametina your smart typing assistant\nI can only open web pages and softwares for you.\n");
    printf("\n");
    printf(BOLDYELLOW "%s" RESET " sir if you wants to open web pages or softwares just write here.\n",name);
}

char enteries(char use[5])
{
    char url[30], softname[30];
    char site[] = "explorer https://";
    char soft[] = "cmd /c";
    if (strcmp(use, "web") == 0)
    {
        printf(BOLD_ITALIC "Search a " BOLDYELLOW "Webpage" RESET ": " RESET "");
        scanf("%s", url);
        strcat(site, url);
        system(site);
    }
    else
    {
        printf(BOLD_ITALIC "Search a " BOLDRED "Software" RESET ": " RESET);
        scanf("%s", softname);
        strcat(soft, softname);
        system(soft);
    }
}
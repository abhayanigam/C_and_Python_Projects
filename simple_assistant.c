//Simple assistant.
#include <stdio.h>
#include <stdlib.h>
char sign(char name[15]);
char enteries(char ent[5]);
int main()
{
    char hello[10], name[15], ans[3], ent[5];
start:
    printf("Say Hello to start:");
    scanf("%s", hello);
    puts((strcmp(hello, "hello") == 0) ? "Hey !! there\n" : "i can't understand what you say\n");
    if (strcmp(hello, "hello") != 0)
    {
        goto start;
    }
    sing(name);
run:
    printf("for webpage search type (web) and for software type (soft) :");
    scanf("%s", ent);
    enteries(ent);

    printf("\n");
    printf("Wanted search again \n");
    printf("then enter yes for search again & no for exit :");
    scanf("%s", ans);
    puts((strcmp(ans, "yes") == 0) ? " " : "Exiting the program .............\n");
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
    printf("So, for better understanding please tell me your name :");
    scanf("%[^\n]%*c", name);
    printf("\n");
    printf("hey !! %s nice to meet you.\n", name);
    printf("So, My name is Nametina the smart type assistant\nI can open any web page and software for you.\n");
    printf("\n");
    printf("if you want to open just write the website name a or software name.\n");
}
char enteries(char use[5])
{
    char url[30], softname[30];
    char site[] = "explorer https://";
    char soft[] = "cmd /c";
    if (strcmp(use, "web") == 0)
    {
        printf("Search a Webpage:");
        scanf("%s", url);
        strcat(site, url);
        system(site);
    }
    else
    {
        printf("Search Software:");
        scanf("%s", softname);
        strcat(soft, softname);
        system(soft);
    }
}
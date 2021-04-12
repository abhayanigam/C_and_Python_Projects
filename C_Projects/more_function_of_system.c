#include <stdio.h>
#include <stdlib.h>

/*
    Summary to change color:-
        0 = Black       8 = Gray
        1 = Blue        9 = Light Blue
        2 = Green       A = Light Green
        3 = Aqua        B = Light Aqua
        4 = Red         C = Light Red
        5 = Purple      D = Light Purple
        6 = Yellow      E = Light Yellow
        7 = White       F = Bright White
*/

void fordelay(int j)
{
    int i, k;
    for (i = 0; i < j; i++)
        k = i;
}

int main()
{
    int i;

    printf("\t\t\t\xB2\xB2\xB2 Program to change colour & loading screen  \xB2\xB2\xB2\xB2");

    system("color 6");      // To change color refer summary at the top.

    printf("\n\n\n\t\xB2\xB2\xB2\xB2\xB2\xB2\xB2 Now screen going to clear and then shows the loading screen \xB2\xB2\xB2\xB2\xB2\xB2\xB2");
    
    printf("\n");
    system("pause");        //--> Press any key to continue.

    system("cls");          // To clear screen.

    printf("\n\nMaking the loading screen!\nLOADING");
        for (i = 0; i <= 10; i++)
        {
            fordelay(1000000000);
            printf(".");
        }

    printf("\n");
    system("date");         // Show the current date and change the date and month.

    return 0;
}
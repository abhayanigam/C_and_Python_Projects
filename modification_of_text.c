#include <stdio.h>

#define RESET       "\033[0m"
#define BLACK       "\033[30m"             /* Black */
#define RED         "\033[31m"             /* Red */
#define GREEN       "\033[32m"             /* Green */
#define YELLOW      "\033[33m"             /* Yellow */
#define BLUE        "\033[34m"             /* Blue */
#define MAGENTA     "\033[35m"             /* Magenta */
#define CYAN        "\033[36m"             /* Cyan */
#define WHITE       "\033[37m"             /* White */
#define BOLDBLACK   "\033[1m\033[30m"      /* Bold Black */
#define BOLDRED     "\033[1m\033[31m"      /* Bold Red */
#define BOLDGREEN   "\033[1m\033[32m"      /* Bold Green */
#define BOLDYELLOW  "\033[1m\033[33m"      /* Bold Yellow */
#define BOLDBLUE    "\033[1m\033[34m"      /* Bold Blue */
#define BOLDMAGENTA "\033[1m\033[35m"      /* Bold Magenta */
#define BOLDCYAN    "\033[1m\033[36m"      /* Bold Cyan */
#define BOLDWHITE   "\033[1m\033[37m"      /* Bold White */

#define STYLE_UNDERLINE    	"\033[4m"
#define STYLE_NO_UNDERLINE 	"\033[24m"
#define STYLE_BOLD         	"\033[1m"
#define BOLD      		   	"\e[1m"
#define ITALIC      	   	"\e[3m"
#define BOLD_ITALIC        	"\e[3m\e[1m"

int main()
{
    printf ("\033[33;1m The Long way to change color and boldnes \033[0m\n");

    printf( BOLDWHITE "The short way using macros." RESET );

	printf(STYLE_UNDERLINE "Use this macro to underline\n");

	printf(STYLE_NO_UNDERLINE "Use this macro for No underline\n");

	printf(STYLE_BOLD "1st method Use this macro to Bold\n");

	printf(BOLD "2nd method Use this macro to Bold\n");

	printf(ITALIC "Use this macro to italic a text\n");

	printf(BOLD_ITALIC "Use this macro for Bold italic text\n");

    return 0;
}
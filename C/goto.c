#include <stdio.h>
void main()
{
label1:
    printf("in label\n");
    goto end;
printf("Killer");
goto label1;
end:
    printf("Ending");
}

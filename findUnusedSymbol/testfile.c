#include <stdio.h>

int a = 1;
int b = 2;

void fund()
{
}

void func()
{
}

static void funb()
{
    printf("hello world! %d\r\n", a);
}

void funa()
{
    funb();
}

int main()
{
    funa();
}

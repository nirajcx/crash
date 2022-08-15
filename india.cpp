#include<iostream.h>
#include<conio.h>
#include<graphics.h>
#include<math.h>
#include<stdio.h>
#include<dos.h>
#include<time.h>
void main()
{
 clrscr();
 int gm, gd=DETECT;
 int r,i,a,b,x,y;
 float PI=3.14
 ;
 initgraph(&gd,&gm,"c:\\TURBOC3\\BGI");

 setcolor(LIGHTRED);                     //for orange part
 rectangle(100,100,400,150);
 setfillstyle(SOLID_FILL,LIGHTRED);
 floodfill(101,101,LIGHTRED);
 delay(400);
 setcolor(WHITE);                        //for white part
 rectangle(100,150,400,200);
 setfillstyle(SOLID_FILL, WHITE);
 floodfill(101,151,WHITE);
 delay(400);
 setcolor(GREEN);                        //for green part
 rectangle(100,200,400,250);
 setfillstyle(SOLID_FILL,GREEN);
 floodfill(101,201,GREEN);
 delay(300);
 a=250, b=175,r=24;                     //for ashok chakra
 setcolor(BLUE);
 circle(a,b,r);
 a=250,b=175,r=24;
 setcolor(BLUE);
 circle(a,b,r);
 for(i=0;i<=360;i=i+15)
 {
  x=r*cos(i*PI/180);
  y=r*sin(i*PI/180);
  line(a,b,a+x,b-y);
  delay(100);
  }
  delay(300);
  setcolor(LIGHTRED);
  settextstyle(TRIPLEX_FONT,HORIZ_DIR,4);
  outtextxy(100,270,"HAPPY");
  delay(300);
   setcolor(WHITE);
  settextstyle(TRIPLEX_FONT,HORIZ_DIR,4);
  outtextxy(160,320,"INDEPENDANCE");
   delay(300);
   setcolor(GREEN);
  settextstyle(TRIPLEX_FONT,HORIZ_DIR,4);
  outtextxy(350,370,"DAY");
  delay(200);
  getch();
  }



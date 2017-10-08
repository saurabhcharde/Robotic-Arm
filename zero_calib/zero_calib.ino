#include<Servo.h>
Servo servo1,servo1,servo1;

void setup() {
  // put your setup code here, to run once:

  pinMode(12,OUTPUT);
  //pinMode(13,OUTPUT);
  servo1.attach(12);
  //servo2.attach(13);
}

void loop() {
  // put your main code here, to run repeatedly:
  servo1.write(0);
  //servo2.write(0);
}

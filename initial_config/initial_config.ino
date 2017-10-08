#include<Servo.h>

int base=9,shoulder=10,elbow=11,wrist=12,gripper=13;
Servo servo1,servo2,servo3,servo4,servo5;

void setup() {
  // put your setup code here, to run once:
  pinMode(base,OUTPUT);
  pinMode(shoulder,OUTPUT);
  pinMode(elbow,OUTPUT);
  pinMode(wrist,OUTPUT);
  pinMode(gripper,OUTPUT);  
  servo1.attach(base);
  servo2.attach(shoulder);
  servo3.attach(elbow);
  servo4.attach(wrist);
  servo5.attach(gripper);
}

void loop() {
  // put your main code here, to run repeatedly:
  servo1.write(90);
  delay(1000);
  servo2.write(10);
  delay(1000);
  servo3.write(10);
  delay(1000);
  servo4.write(112);
  delay(1000);
  servo5.write(180);
  delay(1000);
}

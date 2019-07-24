//RX
#include <SPI.h>
#include "nRF24L01.h"
#include "RF24.h"
#include <Servo.h>

int packet[10];
int sayi;
int mp = 6;
const int lp = 8;
const uint64_t pipes[2] = { 0xF0F0F0F0E1LL, 0xF0F0F0F0D2LL };
typedef enum { role_ping_out = 1, role_pong_back } role_e;

RF24 radio(9,10);
role_e role = role_pong_back;
Servo servo; 

void setup(void)
{
  
  Serial.begin(115200);
  radio.begin();
  role = role_pong_back;
  radio.openWritingPipe(pipes[1]);
  radio.openReadingPipe(1,pipes[0]);
  radio.setDataRate(RF24_1MBPS);
  radio.setPALevel(RF24_PA_MAX);
  radio.startListening();  
  servo.attach(7);
  pinMode(lp, OUTPUT);
  pinMode(mp, OUTPUT);
}







void loop() 
{
  
  if (radio.available())
{ 
  bool done = false;
  while (!done)
{ 
  done = radio.read( &packet, sizeof(packet) );
  servo.write(packet[1]);
  digitalWrite(lp,packet[0]);
  delay(1);
  digitalWrite(lp,0);
  delay(1);
  Serial.print("packet receive(content) : ");
  Serial.print(packet[0]);
  Serial.print("-");
  Serial.print(packet[1]);
  Serial.print("-");
  Serial.print(packet[2]);
  Serial.print("-");
  Serial.print(packet[3]);
  Serial.print("-");
  Serial.print(packet[4]);
  Serial.print("-");
  Serial.print(packet[5]);
  Serial.print("-");
  Serial.print(packet[6]);
  Serial.print("-");
  Serial.print(packet[7]);
  Serial.print("-");
  Serial.print(packet[8]);
  Serial.print("-");
  Serial.println(packet[9]);
}
}
}

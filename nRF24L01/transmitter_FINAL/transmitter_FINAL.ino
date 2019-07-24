//TX
#include <SPI.h>
#include "nRF24L01.h"
#include "RF24.h"
#define controller_pin A0
int packet[10];
const int bt = 8;
const uint64_t pipes[2] = { 0xF0F0F0F0E1LL, 0xF0F0F0F0D2LL };
typedef enum { role_ping_out = 1, role_pong_back } role_e;
role_e role = role_pong_back;
RF24 radio(9, 10);


void setup(void)
{
  Serial.begin(115200);
  radio.begin();
  role = role_ping_out;
  radio.openWritingPipe(pipes[0]);
  radio.openReadingPipe(1, pipes[1]);
  radio.setDataRate(RF24_1MBPS);
  radio.setPALevel(RF24_PA_MAX);
  radio.stopListening();
  pinMode(bt, INPUT);
}







void loop(void)

{
  packet[0] = 1;
  packet[1] = analogRead(controller_pin);
  packet[1] = map(packet[1], 0, 1023, 0, 180);
  packet[2] = packet[1];
  packet[3] = packet[1];
  packet[4] = packet[1];
  packet[5] = packet[1];
  packet[6] = packet[1];
  packet[7] = packet[1];
  packet[8] = packet[1];
  packet[9] = packet[1];
  bool ok = radio.write( &packet, sizeof(packet) );
  Serial.print("packet send(content) : ");
  Serial.print(packet[0]);
  Serial.print("-");
  Serial.println(packet[1]);
  delay(10);
}

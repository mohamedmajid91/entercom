#include <SPI.h>
#include "nRF24L01.h"
#include "RF24.h"
#include "printf.h"
int packet[2];
//
// Hardware configuration
//

// Set up nRF24L01 radio on SPI bus plus pins 9 & 10 

RF24 radio(9,10);

//
// Topology
//

// Radio pipe addresses for the 2 nodes to communicate.
const uint64_t pipes[2] = { 0xF0F0F0F0E1LL, 0xF0F0F0F0D2LL };

//
// Role management
//
// Set up role.  This sketch uses the same software for all the nodes
// in this system.  Doing so greatly simplifies testing.  
//

// The various roles supported by this sketch
typedef enum { role_ping_out = 1, role_pong_back } role_e;

// The debug-friendly names of those roles
const char* role_friendly_name[] = { "invalid", "Ping out", "Pong back"};

// The role of the current running sketch
role_e role = role_pong_back;

void setup(void)
{
  //
  // Print preamble
  //

  Serial.begin(115200);
  printf_begin();
  printf("ROLE: %s\n\r",role_friendly_name[role]);

  //
  // Setup and configure rf radio
  //

  radio.begin();

  // optionally, increase the delay between retries & # of retries
  radio.setRetries(15,15);

  // optionally, reduce the payload size.  seems to
  // improve reliability
  //radio.setPayloadSize(8);

  //
  // Open pipes to other nodes for communication
  //

  // This simple sketch opens two pipes for these two nodes to communicate
  // back and forth.
  // Open 'our' pipe for writing
  // Open the 'other' pipe for reading, in position #1 (we can have up to 5 pipes open for reading)

  //if ( role == role_ping_out )
  {
    //radio.openWritingPipe(pipes[0]);
    //radio.openReadingPipe(1,pipes[1]);
  }
  //else
  {
    //radio.openWritingPipe(pipes[1]);
    //radio.openReadingPipe(1,pipes[0]);
  }

  //
  // Start listening
  //

  radio.startListening();

  //
  // Dump the configuration of the rf unit for debugging
  //

  radio.printDetails();
  role = role_pong_back;
  radio.openWritingPipe(pipes[1]);
  radio.openReadingPipe(1,pipes[0]);

}

void loop() {
  // put your main code here, to run repeatedly:





    
    // if there is data ready
    if ( radio.available() )
    {
      // Dump the payloads until we've gotten everything
      //unsigned long packet;
      bool done = false;
      while (!done)
      {
        // Fetch the payload, and see if this was the last one.
        done = radio.read( &packet, sizeof(packet) );
        Serial.print("packet receive(content) : ");
        Serial.println(packet[0]);
        // Spew it
        //printf("\nGot payload %lu...",packet);

  // Delay just a little bit to let the other unit
  // make the transition to receiver
  delay(20);
      }
      /*
      // First, stop listening so we can talk
      radio.stopListening();

      // Send the final one back.
      radio.write( &got_time, sizeof(unsigned long) );
      printf("Sent response.\n\r");

      // Now, resume listening so we catch the next packets.
      radio.startListening(); */
    }








}

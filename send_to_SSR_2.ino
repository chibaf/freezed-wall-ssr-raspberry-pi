#include <avr/io.h>
#define PWMPin 9

unsigned int frq = 16; // frequency
float duty = 0.5; // duty ratio

byte incomingByte; // for incoming serial data
int dec;

void setup() {
  Serial.begin(9600);
  pinMode(PWMPin, OUTPUT);
}

void loop() {
  // seting mode
  TCCR1A = 0b00100001;
  TCCR1B = 0b00010010;
  OCR1A = (unsigned int)(1000000 / frq);  // top value
  
  if (Serial.available() > 0) {
    // read the incoming byte:
    incomingByte = Serial.read();

    dec = (int)incomingByte;
    duty = (float)dec/255.0;
    OCR1B = (unsigned int)(1000000 / frq * duty); // duty ratio

    Serial.println(duty);
    // write number to SSR via pwm 9:
    //analogWrite(9, dec);
  }
}

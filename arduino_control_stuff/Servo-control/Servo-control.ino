#include <Servo.h>

Servo myservo;  // create Servo object to control a servo
// twelve Servo objects can be created on most boards

int pos = 0;    // variable to store the servo position

int piSignalPin = 3;

void setup() {
  Serial.begin(9600);
  pinMode(piSignalPin, INPUT);
  myservo.attach(2);  // attaches the servo on pin 9 to the Servo object
}

void loop() {
  int piSignal = digitalRead(piSignalPin);

  if (piSignal == HIGH) {
      for (pos = 0; pos <= 130; pos += 1) { // goes from 0 degrees to 180 degrees
        // in steps of 1 degree
        myservo.write(pos);              // tell servo to go to position in variable 'pos'
        delay(8);                       // waits 15 ms for the servo to reach the position
      }
      for (pos = 130; pos >= 0; pos -= 1) { // goes from 180 degrees to 0 degrees
        myservo.write(pos);              // tell servo to go to position in variable 'pos'
        delay(8);                       // waits 15 ms for the servo to reach the position
      }
  } else {
    Serial.println("Not rotating");
  }

  delay(100);
}

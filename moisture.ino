byte incoming = 0;

void setup() {
  Serial.begin(9600);

}

void loop() {
  if (Serial.available() > 0) {
    incoming = Serial.read() - 'O';
    //Serial.println("Got");
    Serial.println(analogRead(incoming));
  }
}

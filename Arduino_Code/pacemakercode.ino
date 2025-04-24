const int ledPin = 9;
const int buttonPin = 7; // Use this if you're simulating with a button
const int potPin = A0;   // Use this if you're simulating with a potentiometer

int heartRate = 0;
int minHeartRate = 60;
int maxHeartRate = 100;

void setup() {
  pinMode(ledPin, OUTPUT);
  pinMode(buttonPin, INPUT);
  Serial.begin(9600); // Communication with Raspberry Pi
}

void loop() {
  // Simulate heart rate with button (press to increase rate)
  if (digitalRead(buttonPin) == HIGH) {
    heartRate += 1;
  }

  // Simulate heart rate with potentiometer (read analog value)
  heartRate = analogRead(potPin) / 10; // Scaling down analog value to heart rate range

  // Regulate heart rate based on programmed limits
  if (heartRate < minHeartRate || heartRate > maxHeartRate) {
    digitalWrite(ledPin, HIGH); // Pacemaker active (LED on)
  } else {
    digitalWrite(ledPin, LOW); // Normal heart rate (LED off)
  }

  // Send heart rate data to Raspberry Pi
  Serial.println(heartRate);
  delay(1000);
}
// Define variables
int data;
int LEDPin = 10;

void setup() 
{ 
  pinMode(LEDPin, OUTPUT);
  Serial.begin(9600);  
//  Initially setting LED to low
//  digitalWrite(LEDPin, LOW);
}
 
void loop() 
{
  // see if there is any incoming serial data
  while (Serial.available())
  {
    data = Serial.read();
   }
   if (data == '1')
  digitalWrite (LEDPin, HIGH);

  else if (data == '0')
  digitalWrite (LEDPin, LOW);
}

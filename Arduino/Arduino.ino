#define ledR 6
#define ledG 5
#define ledB 3

int valR,valG,valB;
char rx[6];
char charR[3];
char charG[3];
char charB[3];

int i=0;

void setup() {                
  pinMode(ledR, OUTPUT);
  pinMode(ledG, OUTPUT);  
  pinMode(ledB, OUTPUT);  
  
  Serial.begin(115200);
  
  
  
}

// the loop routine runs over and over again forever:
void loop() 
{
  if (Serial.available() > 0) 
  {
    rx[i] = (char)Serial.read();
    i++;      
  }
  
  
if (strcmp(rx, "START!") == 0) 
{
  Serial.println("ACK");
}
  
  
  if(i == 6)
  {
    
    charR[0] = rx[0];
    charR[1] = rx[1];
    charG[0] = rx[2];
    charG[1] = rx[3];
    charB[0] = rx[4];
    charB[1] = rx[5];
    valB = (int)strtol(charB,NULL,16);
    valG = (int)strtol(charG,NULL,16);
    valR = (int)strtol(charR,NULL,16);
   
    i = 0; 
  }
  
  
  analogWrite(ledR,255-valR);
  analogWrite(ledG,255-valG);
  analogWrite(ledB,255-valB);
}

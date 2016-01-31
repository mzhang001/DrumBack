#define LIKE 0  //A0 PORT
#define UNLIKE 1  //A1 PORT
#define THRESHOLD 200

int val_like = 0;
int val_unlike = 0;

void setup()
{
  Serial.begin(9600);
}

void loop()
{
  val_like = analogRead(LIKE);  //READ FROM PORT
  val_unlike = analogRead(UNLIKE);  //READ FROM PORT
  bool flag = false;
  if(val_like > THRESHOLD) { 
    Serial.println("LIKE");
    flag = true;
  }
  if(val_unlike > THRESHOLD) {
    Serial.println("UNLIKE");
    flag = true;
  }
  if(flag) {
    delay(100);
    flag = false;
  }
}

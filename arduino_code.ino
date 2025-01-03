
#include "I2Cdev.h" 
#include "MPU6050.h" 
MPU6050 sensor; 

int ivme_x, ivme_y, ivme_z, gyro_x, gyro_y, gyro_z; 
const int ayakkabi_sensor_pin = A1;
int ayakkabi_value = 0;
bool temas, tus;

void setup() {
  Serial.begin(9600);     
  sensor.initialize();   
  pinMode(ayakkabi_sensor_pin, INPUT);
  tus = false;
}
  
void loop() {
  sensor.getMotion6(&ivme_x, &ivme_y, &ivme_z, &gyro_x, &gyro_y, &gyro_z); 
  ayakkabi_value = analogRead(ayakkabi_sensor_pin);

  if (ayakkabi_value < 15)
  {
    temas = true;
    tus = false;
  }
  else
  {
    temas = false;
  }

  if (temas == false && tus == false)
  {
    Serial.println(000);
    tus = true;
  }
  else
  {
    Serial.println(ivme_x);
  }
  
  delay(200);    
}

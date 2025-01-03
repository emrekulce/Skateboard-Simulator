#include "I2Cdev.h"
#include "MPU6050.h"

MPU6050 sensor;

int ivme_x, ivme_y, ivme_z, gyro_x, gyro_y, gyro_z;

const int threshold = 2000; 
const int ayakkabi_sensor_pin = A1;
int ayakkabi_value = 0;
bool temas, tus;

void setup()
{
  Serial.begin(9600);
  pinMode(ayakkabi_sensor_pin, INPUT);
  tus = false;
  sensor.initialize();
  if (sensor.testConnection()) {
    Serial.println("MPU6050 sensörü başarıyla bağlandı!");
  } else {
    Serial.println("MPU6050 bağlantı hatası!");
  }
}

void loop() 
{
  sensor.getMotion6(&ivme_x, &ivme_y, &ivme_z, &gyro_x, &gyro_y, &gyro_z);
  ayakkabi_value = analogRead(ayakkabi_sensor_pin);

  if (ivme_x > threshold) {
    Serial.println("sag");
  } 
  else if (ivme_x < -threshold) {
    Serial.println("sol");
  } 
  else {
  }
  }

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
    Serial.println("ileri");
    tus = true;
  }

  delay(100);
}

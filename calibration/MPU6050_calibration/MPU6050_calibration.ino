#include "I2Cdev.h"
#include "MPU6050.h"

#if I2CDEV_IMPLEMENTATION == I2CDEV_ARDUINO_WIRE
    #include "Wire.h"
#endif

MPU6050 accelgyro;

int16_t ax, ay, az;
int16_t gx, gy, gz;

void setup() {
    #if I2CDEV_IMPLEMENTATION == I2CDEV_ARDUINO_WIRE
        Wire.begin();
    #elif I2CDEV_IMPLEMENTATION == I2CDEV_BUILTIN_FASTWIRE
        Fastwire::setup(400, true);
    #endif

    Serial.begin(38400);

    // initialize device
    Serial.println("Initializing I2C devices...");
    accelgyro.initialize();

    // verify connection
    Serial.println("Testing device connections...");
    Serial.println(accelgyro.testConnection() ? "MPU6050 connection successful" : "MPU6050 connection failed");
}

int cnt = 0, t = 0;
double ave_ax = 0.0, ave_ay = 0.0, ave_az = 0.0;
double ave_gx = 0.0, ave_gy = 0.0, ave_gz = 0.0;

void loop() {
    // read raw measurements from device
    accelgyro.getMotion6(&ax, &ay, &az, &gx, &gy, &gz);

    t += 1;
    if (t > 500) {
        cnt += 1;
        // calculate average value to eliminate noises
        ave_ax = (double(cnt - 1) * ave_ax + ax) / double(cnt);
        ave_ay = (double(cnt - 1) * ave_ay + ay) / double(cnt);
        ave_az = (double(cnt - 1) * ave_az + az) / double(cnt);
        ave_gx = (double(cnt - 1) * ave_gx + gx) / double(cnt);
        ave_gy = (double(cnt - 1) * ave_gy + gy) / double(cnt);
        ave_gz = (double(cnt - 1) * ave_gz + gz) / double(cnt);

        Serial.print("a/g:\t");
        Serial.print(ave_ax); Serial.print("\t");
        Serial.print(ave_ay); Serial.print("\t");
        Serial.print(ave_az); Serial.print("\t");
        Serial.print(ave_gx); Serial.print("\t");
        Serial.print(ave_gy); Serial.print("\t");
        Serial.println(ave_gz);
    }
}

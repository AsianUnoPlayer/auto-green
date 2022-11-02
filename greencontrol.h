#ifndef GREENCONTROL_H
#define GREENCONTROL_H

//all the components for light
#define MOIST_SENSOR 1
#define TEMP_SENSOR 2 //technically temperature & humidity sensor
#define UV_LIGHT 3

//all the components for water
#define WATER_PUMP 4
#include <iostream>

//all the extra stuff
#define RGB_LIGHT 5

class plant
{
    plant(String name, int water, double plantMin, double plantMax);
    
    int indicate_water_lvl();
    void set_water(int waterLevel);

    double get_temp();
    void temp_adjust(double minTemp, double maxTemp);

    String name;
    double waterNeeds;
    double minTemp;
    double maxTemp;
}

#endif
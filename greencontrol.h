#ifndef GREENCONTROL_H
#define GREENCONTROL_H

//all the components for light
#define MOIST_SENSOR 
#define TEMP_SENSOR //technically temperature & humidity sensor
#define UV_LIGHT 

//all the components for water
#define WATER_PUMP
#include <iostream>

class plant
{
    plant(String name, double water, double plantMin, double plantMax);
    
    void get_moist();
    void get_temp();
    void set_temp();

    void indicate_water();

    String name;
    double waterNeeds;
    double minTemp;
    double maxTemp;
}

#endif
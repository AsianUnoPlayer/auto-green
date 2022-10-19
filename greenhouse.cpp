#include <iostream>
#include "greencontrol.h"
using namespace std;

plant::plant(String name, double water, double plantMin, double plantMax)
{
    name = name;
    waterNeeds = water;
    minTemp = plantMin;
    maxTemp = plantMax;
}

void plant::get_moist()
{
    //idk something
}
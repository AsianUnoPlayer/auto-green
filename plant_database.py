#Something with GrowStuff API https://www.growstuff.org/
#Or maybe the USDA API https://plants.usda.gov/

#Replace this with some API in the future or just hardcore the data right now
plant_database = ["basil", "rosemary", "catnip"]

class PlantData:
    def __init__(self, plant_name, plant_height, plant_width, plant_spacing, plant_water, plant_mintemp, plant_maxtemp, plant_minSoil, plant_maxSoil):
        self.name = plant_name
        self.height = plant_height #Max Height in inches
        self.width = plant_width #Max Width in inches
        self.spacing = plant_spacing #Average Spacing in inches
        self.water = plant_water #in fahrenheit
        self.minTemp = plant_mintemp #in fahrenheit
        self.maxTemp = plant_maxtemp #in fahrenheit
        self.minSoilph = plant_minSoil #in pH
        self.maxSoilph = plant_maxSoil #in pH

basil = PlantData("Basil", 3.0, 16.0, 6.0, "moderate", 70.0, 85.0, 6.0, 7.5)
rosemary = PlantData("Rosemary", 3.0, 16.0, 2.5, "drought-tolerant", 55.0, 80.0, 6.0, 7.0)
catnip = PlantData("Catnip", 3.0, 3.0, 21.0, "average", 55.0, 85.0, 6.0, 7.0)
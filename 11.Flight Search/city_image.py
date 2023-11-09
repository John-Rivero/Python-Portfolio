from PyQt6.QtGui import QPixmap

#IMAGE paths
city_image_paths = {
    
    "ATL" : "11.Flight Search\image\Atlanta.jpg",
    "DFW" : "11.Flight Search\image\DFW.jpg",
    "DEN" : "11.Flight Search\image\Denver.jpg",
    "ORD" : "11.Flight Search\image\Chicago.jpg",
    "LAX" : "11.Flight Search\image\LA.jpg",
    "JFK" : "11.Flight Search/image/New York.jpg",
    "LAS" : "11.Flight Search\image\Las Vegas.jpg",
    "MCO" : "11.Flight Search\image\Orlando.jpg",
    "MIA" : "11.Flight Search\image\Miami.jpg",
    "CLT" : "11.Flight Search\image\Charlotte.jpg",
    "SEA" : "11.Flight Search\image\Seattle.jpg",
    "PHX" : "11.Flight Search\image\Phoenix.jpg",
    "EWR" : "11.Flight Search/image/Newark.jpg",
    "SFO" : "11.Flight Search\image\San Francisco.jpg",
    "IAH" : "11.Flight Search\image\Houston.jpg",
    "BOS" : "11.Flight Search\image\Boston.jpg",
    "FLL" : "11.Flight Search\image\Fort Lauderdale.jpg",
    "MSP" : "11.Flight Search\image\Minneapolis.jpg",
    "LGA" : "11.Flight Search/image/New York City.jpg",
    "DTW" : "11.Flight Search\image\Detroit.jpg",
    "PHL" : "11.Flight Search\image\Philadelphia.jpg",
    "SLC" : "11.Flight Search\image\Salt Lake City.jpg",
    "DCA" : "11.Flight Search\image\WashingtonDC.jpg",
    "SAN" : "11.Flight Search\image\San Diego.jpg",
    "BWI" : "11.Flight Search\image\Baltimore.jpg",
    "TPA" : "11.Flight Search\image\Tampa.jpg",
    "AUS" : "11.Flight Search\image\Austin.jpg",
    "IAD" : "11.Flight Search\image\WashingtonDC2.jpg",
    "BNA" : "11.Flight Search/image/Nashville.jpg",
    "MDW" : "11.Flight Search\image\Chicago2.jpg"

}

#LocationTo image selector
def image_city_Clicked(self,index):
    
    selected_city = self.locationTo.currentText()
    selected_city2 = selected_city[-4:-1]
    #print(selected_city2)
    
    if selected_city2 in city_image_paths:
        city = city_image_paths[selected_city2]
        pixmap = QPixmap(city)
        
        self.cityImage.setPixmap(pixmap)
        
    else:
        print("error")

    
    


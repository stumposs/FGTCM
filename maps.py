'''
This module includes objects and methods relevant to google map quest 
'''

class Icon:
    #'''Get/make marker icons at http://mapki.com/index.php?title=Icon_Image_Sets'''
    def __init__(self,id='icon'):
        self.id = id
        #self.image = ""     #uses default Google Maps icon
        self.shadow = ""

        self.image = ""
        self.iconSize = (12, 20)    # these settings match above icons
        self.shadowSize = (22, 20)
        self.iconAnchor = (6, 20)
        self.infoWindowAnchor = (5, 1)

class Map:
    def __init__(self,id="map",pointlist=None):
        global coordiante1
        global coordinate2
        self.id       = id    # div id        
        #self.width    = "500px"  # map div width
        #self.height   = "300px"  # map div height
        self.center   = (coordinate1,coordinate2)     # center map latitude coordinate
        self.zoom        = "1"   # zoom level
        self.navcontrols  =   True   # show google map navigation controls
        self.mapcontrols  =   True   # show toogle map type (sat/map/hybrid) controls
        if pointlist == None:
            self.points = []   # empty point list
        else:
            self.points = pointlist   # supplied point list
    
    def __str__(self):
        return self.id
        
    
    def setpoint(self, point):
        """ Add a point (lat,long,html,icon) """
        self.points.append(point)

class PyMap:
    def GoogleMapPy(self):
        """ Returns complete javacript for rendering map """
        self.js = """<script src="https://maps.googleapis.com/maps/api/js?v=3.exp&sensor=false"></script>
		<script>
		var map;
		var marker;
		var center;
		var poly;
		var infowindow;
		var image;
		var markers = [];
		function initialize() {
			center = new google.maps.LatLng(0.0,0.0);
			var mapOptions = {zoom: 1,center: center};
			image = {
				url: 'PlaneImage.png',
				// This marker is 20 pixels wide by 32 pixels tall.
				size: new google.maps.Size(1000, 1000),
				// The origin for this image is 0,0.
				origin: new google.maps.Point(0,0),
				// The anchor for this image is the base of the flagpole at 0,32.
				anchor: new google.maps.Point(10, 10)
			};
			map = new google.maps.Map(document.getElementById('map-canvas'),mapOptions);
			marker = new google.maps.Marker({position: center, map: map,icon: image, animation: google.maps.Animation.DROP});
			var polyOptions = {
			strokeColor: '#FF00FF',
			strokeOpacity: 1.0,
			strokeWeight: 3
			};
			poly = new google.maps.Polyline(polyOptions);
			poly.setMap(map);
			
			//var contentString = ['coordinates','Latitude: ' + marker.getPosition().lat(), 'Longitude: '+marker.getPosition().lng()].join('<br>');
			
			function createInfoWindowContent(){
				return[
					'Coordinates:',
					'Latitude: ' + marker.getPosition().lat(),
					'Longitude: ' + marker.getPosition().lng()
				].join('<br>');
			}
			infowindow = new google.maps.InfoWindow();
			
			google.maps.event.addListener(marker, 'click', function() {
				infowindow.setContent(createInfoWindowContent());
				infowindow.open(map,marker);
			});
			
			google.maps.event.addListener(map,'click',function(event) {
				addMarker(event.latLng);
			});
			


		}

		function moveMarker(position, map, marker) {
			//infowindow.close();
			var path = poly.getPath();
			path.push(position);
			marker.setPosition(position);
			map.panTo(position);
			//infowindow.setContent(createInfoWindowContent());
			//infowindow.open(map,marker);
		}
		
		function addMarker(location) {
			var marker2 = new google.maps.Marker({
				position: location,
				map: map,
				title: "my title",
				icon: image
			});
			map.panTo(location);
			//markers.push(marker2);
		}

		google.maps.event.addDomListener(window, 'load', initialize);

		</script>
		"""
        return self.js 
        
    def showhtml(self):
        """returns a complete html page with a map"""
        self.html = """
		<!DOCTYPE html>
<html>
  <head>
    <title>Accessing arguments in UI events</title>
    <meta name="viewport" content="initial-scale=1.0, user-scalable=no">
    <meta charset="utf-8">
    <style>
      html, body, #map-canvas {
        height: 100%%;
        margin: 0px;
        padding: 0px
      }
    </style>
    %s
  </head>
  <body>
    <div id="map-canvas"></div>
  </body>
</html>
		""" % self.GoogleMapPy()
        return self.html
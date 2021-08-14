# Geo Location Polygon API

## API Documentation

URL/  : Endpoint: /Providers

      : GET, POST
      
      : Description: Create a Provider.
      
      : URL: http://localhost:8000/providers

URL/  : Endpoint: /Providers/1

      : GET, DELETE, PUT
      
      : Description: A Provider's Details. Update, Delete Provider.
      
      : URL: http://localhost:8000/providers/1

URL/  : Endpoint: /Providers/1/Polygons

      : GET, POST
      
      : Description: A Provider's Service Areas. Create new Service Area.
      
      : URL: http://localhost:8000/providers/1/polygons

URL/  : Endpoint: /Providers/1/Polygons/1

      : GET, DELETE, PUT
      
      : Description: A Service Area's Polygon Details. Update, Delete Service Area.
      
      : URL: http://localhost:8000/providers/1/polygons/1

URL/  : Endpoint: /Providers/1/Polygons/1/Polygon

      : GET, POST,
      
      : Description: A Service Area's Polygon 'Lats' and 'Lngs'. Add New Polygon Coordinates.
      
      : URL: http://localhost:8000/providers/1/polygons/1/polygon

URL/  : Endpoint: /Providers/1/Polygons/1/Polygon/1

      : GET, DELETE, PUT
      
      : Description: A Polygon's 'lat' and 'lng' coordinates. Update, Delete a Polygon.
      
      : URL: http://localhost:8000/providers/1/polygons/1/polygon/1

URL/  : Endpoint: /Users/

      : Description: Create a new User.
      
      : URL: http://localhost:8000/users/

URL/  : Endpoint: /Login/

      : Description: Login to platform.
      
      : URL: http://localhost:8000/login/

URL/  : Endpoint: /Services/?lat=&lng=

      : Description: List all 'service areas' within parameters 'lat' and 'lng'.
      
      : URL: http://localhost:8000/services?lat=&lng=



## This Project solves the following task

A transportation company is expanding internationally, and they have a scaling problem, many transportation suppliers they would like to integrate cannot give concrete zipcodes, cities, etc that they serve. 

To combat this, they would like to be able to define custom polygons as their "service area" and would like for the owners of these shuttle companies to be able to define and alter their polygons whenever they want, eliminating the need for company employees to do this boring grunt work.

They would like you to build a JSON REST API to help them solve this problem. 
Your project should have API endpoints to create, update, delete, and retrieve information about service area providers. Batch operations are not necessary except for get. 

A provider should contain the following information:

- Name

- Email

- Phone Number

- Language

- Currency

Once a provider is created they should be able to start defining service areas. 
These service areas will be geojson polygons and should be stored in the database in a way that they can be retrieved and queried upon easily. 

There should be endpoints to create, update, delete, and get a polygon. Batch operations are not necessary except for get. 
A polygon should contain a name and price as well as the geojson information.

You should create an API endpoint to query this data. 
It should take a lat/lng pair as arguments and return a list of all polygons that include the given lat/lng. It should also return the name of the polygon, provider's name, and price should be returned for each polygon. This operation should be FAST. 
The company has thousands of providers and hundreds of thousands of service areas.

All of this should be built in python/django. 
Use any extra libraries you think will help, choose whatever database you think is best fit for the task, and use caching as you see fit. 

Once you finish, write up some API docs (again using any tool you see fit) and make sure your code is well tested. 

Ensure that your code is clean, follows standard pep8 style (though you can use 120 characters per line) and has comments where appropriate.


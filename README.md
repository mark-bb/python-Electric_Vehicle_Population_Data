# Electric Vehicle Population dataset analysis with a python program
The comma-separated values (CSV) file [Electric_Vehicle_Population_Data.csv](https://data.wa.gov/api/views/f6w7-q2d2/rows.csv?accessType=DOWNLOAD) is used as a dataset for analysis with a python program Electric_Vehicle_Population_Data.py.

The program consists of a number of functions:
- get_vehicles: reads the CSV file passed as a parameter and returns a dictionary with keys as column names (from the 1-st row) and values as list of column values
- get_most_popular_makes: gets the dictionary returned by the 1-st function and returns a sorted list of tuples in the form of (Make_name, Number_of_owners)
- get_most_popular_models: gets the vehicles dictionary returned by the 1-st function and returns a sorted list of tuples in the form of ((Make_name, Model_name), Number_of_owners)
- get_vehicles_by_year: gets the vehicles dictionary returned by the 1-st function, a year number and returns a number of vehicles made in this year
- get_vehicle_types_by_year: gets the dictionary returned by the 1-st function and returns a sorted list of tuples in the form of (year, (number_of_BEVs, number_of_PHEVs))

 The main part of the program calls sequentially:
 - get_vehicles to get a dictionary from the file
 - get_most_popular_makes and prints first N (specified as a variable value) tuples returned
 - get_most_popular_models and prints first N (specified as a variable value) tuples returned
 - get_vehicles_by_year with a year number of interest
 - get_vehicle_types_by_year and prints the result

import csv

def get_vehicles(file_name):
    '''
    Reads the csv file and returns dictionary with:
    - keys as column names (from the 1-st row)
    - values as list of column values
    Parameters:
    - file_name: input data set file name
    Returns: dictionary
    '''

    vehicles = {} # dictionary initialization
    f = open(file=file_name, mode="r")
    line_no = 0
    lines = csv.reader(f, delimiter=',', quotechar='"')
    for line in lines:
        # The "line" variable is a list of tokens got from a line of file
        line_no += 1
        if line_no == 1:
            '''
            We read the 1-st line of the file.
            Initialize the vehicles dictionary with:
            token (a column name) as a key and empty list as value
            '''
            #print ("length: {}".format(len(tok)))
            for idx in range(len(line)):
                vehicles[line[idx]] = list()
            
            # save the list of headers
            # we will use it later to store the data properly
            headers = line 
            #print (headers)
            #print ("Attributes number: {}".format(len(headers)))
        else:
            # Save data to the dictionary using headers.
            for idx in range(len(line)):
                vehicles[headers[idx]].append(line[idx])
            #print (vehicles)
            '''
            # Just for test: to stop after a number of lines
            if line_no == 1001:
                break
            '''
    f.close()
    return vehicles

def get_most_popular_makes(vehicles):
    '''
    Gets vehicles dictionary and returns a sorted list 
    (most Number_of_owners first):
    of tuples: (Make_name, Number_of_owners)
    Parameters:
    - vehicles: dictionary with vehicles
    Returns: sorted list
    '''

    # Dictionary {Make: number_of_owners}
    item_count = {}
    # print(vehicles['Make'])
    for val in vehicles['Make']:
        item_count[val] = (0 if not item_count.get(val) else item_count[val]) + 1
    #print(item_count)

    # Sort dictionary in the reverse order by values and return the result
    return sorted(item_count.items(), key=lambda x:x[1], reverse=True)

def get_most_popular_models(vehicles):
    '''
    Gets vehicles dictionary and returns a sorted list 
    (most Number_of_owners first):
    of tuples: ((Make_name, Model_name), Number_of_owners)
    Parameters:
    - vehicles: dictionary with vehicles
    Returns: sorted list
    '''

    # Dictionary {(Make, Model): number_of_owners}
    item_count = {}
    # Model consists of pair values: Make and Model
    # We iterate by indexes of one of them (Make)
    # to get the corresponding index of Model
    for idx in range(len(vehicles['Make'])):
        # print ("{}, {}".format(vehicles['Make'][idx], vehicles['Model'][idx]))
        # val is tuple (Make, Model) here
        val = (vehicles['Make'][idx], vehicles['Model'][idx])
        item_count[val] = (0 if not item_count.get(val) else item_count[val]) + 1
    #print (item_count)

    # Sort dictionary in the reverse order by values and return the result
    return sorted(item_count.items(), key=lambda x:x[1], reverse=True)

def get_vehicles_by_year(vehicles, year):
    '''
    Gets vehicles dictionary, year number and returns
    a number of vehicles made in this year
    Parameters:
    - vehicles: dictionary with vehicles
    - year: a year number
    Returns: number of vehicles made
    '''

    count = 0
    for yr in vehicles['Model Year']:
        if yr == year:
            count += 1
    return count

def get_vehicle_types_by_year(vehicles):
    '''
    Gets vehicles dictionary and returns a sorted list 
    (most Number_of_owners first):
    of tuples: (year, (number_of_BEVs, number_of_PHEVs))
    Parameters:
    - vehicles: dictionary with vehicles
    Returns: sorted list of tuples
    '''

    # Dictionary {year: (BEVs, PHEVs)}
    item_count = {}
    # Model consists of pair values: Make and Model
    # We iterate by indexes of one of them (Make)
    # to get the corresponding index of Model
    for idx in range(len(vehicles['Model Year'])):
        # val is tuple (Make, Model) here
        year = vehicles['Model Year'][idx]
        type = vehicles['Electric Vehicle Type'][idx]
        #print("Year: {}, type: {}".format(year, type))
        is_bev = 0 if type.find('(BEV)') == -1 else 1
        is_phev = 0 if type.find('(PHEV)') == -1 else 1
        if not item_count.get(year):
            # initialize the dictionary for this year
            item_count[year] = (is_bev, is_phev)
        else:
            # increment the tuple values for this year
            item_count[year] = (item_count[year][0] + is_bev, item_count[year][1] + is_phev)

    #return sorted list of tuples by year
    return sorted(item_count.items())

#
# Main
#

# Get dictionary vehicles
vehicles = get_vehicles(file_name="Electric_Vehicle_Population_Data.csv")
#print(vehicles)

items_to_print = 3

# Print not more than first items_to_print Models
items = get_most_popular_makes(vehicles)
print ("\nThe most {} popular Marks:".format(items_to_print))
for idx in range (min(items_to_print, len(items))):
    print (items[idx])

# Print not more than first items_to_print Models
items = get_most_popular_models(vehicles)
print ("\nThe most {} popular Models:".format(items_to_print))
for idx in range (min(items_to_print, len(items))):
    print (items[idx])

# Print the number of vehicles made in the year specified
year = "2016"
print("\nThe number of vehicles made in {}: {}".format(year, get_vehicles_by_year(vehicles, year)))

print ("\nTypes by year:")
items = get_vehicle_types_by_year(vehicles)
#print (items)
for item in items:
    print ("Year {}: BEVs = {}, PEVs = {}".format(item[0], item[1][0], item[1][1]))

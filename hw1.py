##function to delete row with humd = -99.000 or -999.000
def delete_row(data):
    count = 0
    data_list = data #copy data to a new list
    while(count<len(data)):
        for datas in data_list: #iterate
            if datas.get('HUMD') == '-99.000' or datas.get('HUMD') == '-999.000':
                data_list.remove(datas) #delete unwanted datas
        count +=1
    return data_list #return modified list


#function to return sum for each station id.
def sum(data_list, station_id):
    data_dic = dict() #declaration of new data dictionary
    for id in station_id:
        data_dic[id] = 0 #set all data value to zero

    for datas in data_list:
        for key, value in datas.items():
            if value in station_id:
                data_dic[value] += float(datas.get('HUMD'))

    return sorted(data_dic.items()) #return the sorted data

#function to save the list to output
def save_list(data_dic):
    data_list = []
    saved_list = []
    count = 0
    for key, value in data_dic:
        if value == 0: #if HUMD's value is zero, output None
            data_list.append(key)
            data_list.append('None')
        else:
            data_list.append(key)
            data_list.append(value)

    while(count<len(data_list)):
        saved_list.append(data_list[count:count+2])
        count +=2

    return saved_list


#  csv -- fileIO operation
import csv #import csv library

cwb_filename = '106061181.csv'#read the file
#cwb_filename = 'sample_input.csv'#read the sample input file
data = []
header = []
target_data =[]
with open(cwb_filename) as csvfile:
   mycsv = csv.DictReader(csvfile)
   header = mycsv.fieldnames
   for row in mycsv:
      data.append(row)

#=======================================

station_id = ['C0A880', 'C0F9A0', 'C0G640', 'C0R190', 'C0X260'] #list declaration id needed
for id in station_id:
    target_data += list(filter(lambda item: item['station_id'] == id , data))#retrieve data point for ids

#compute and print data
print(save_list(sum(delete_row(target_data), station_id)))

import requests
import sys
import json
def update_csv_with_zip_code(csvfilename):
    rownum = 0
    import csv
    all_lines = []
    with open(csvfilename) as f, open(csvfilename + ".out.csv", "w") as g:
        reader = csv.reader(f)
        writer = csv.writer(g)
        for row in reader:
            if rownum == 0:
                rownum += 1
                pass
            else:
                lat = row[24]
                lon = row[25]
                rownum += 1
                line = row
                line.append(get_zip_for_point(lat, lon))
                all_lines.append(line)
                
        for line in all_lines:
            writer.writerow(line)

def get_zip_for_point(lattitude, longitude):
    link = 'https://reverse.geocoder.api.here.com/6.2/reversegeocode.json?prox='+lattitude+"%2C"+longitude+'%2C250&mode=retrieveAddresses&maxresults=1&gen=9&app_code=R16AjGFBYKOLX8ax5T6-yg&app_id=L6XIaPrZvRPC5uP8HQpS'
    x = requests.get(link)
    jsonData = json.loads(x.text)
    return jsonData['Response']['View'][0]['Result'][0]['Location']['Address']['PostalCode']
    

if __name__ == '__main__':
	filename = sys.argv[1]
	print("Processing filename", filename)
	update_csv_with_zip_code(filename)
	


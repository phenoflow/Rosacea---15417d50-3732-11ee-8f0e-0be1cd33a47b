# Kuan V, Denaxas S, Gonzalez-Izquierdo A, Direk K, Bhatti O, Husain S, Sutaria S, Hingorani M, Nitsch D, Parisinos C, Lumbers T, Mathur R, Sofat R, Casas JP, Wong I, Hemingway H, Hingorani A, 2023.

import sys, csv, re

codes = [{"code":"F4C3100","system":"readv2"},{"code":"M153.00","system":"readv2"},{"code":"M153000","system":"readv2"},{"code":"M153100","system":"readv2"},{"code":"M153200","system":"readv2"},{"code":"M153300","system":"readv2"},{"code":"M153400","system":"readv2"},{"code":"M153z00","system":"readv2"},{"code":"Myu6900","system":"readv2"},{"code":"1518.0","system":"med"},{"code":"16014.0","system":"med"},{"code":"30398.0","system":"med"},{"code":"3582.0","system":"med"},{"code":"36835.0","system":"med"},{"code":"50603.0","system":"med"},{"code":"53876.0","system":"med"},{"code":"64861.0","system":"med"},{"code":"970.0","system":"med"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('rosacea-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["rosacea---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["rosacea---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["rosacea---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)

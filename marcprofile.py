import sys
import os
import csv
from pymarc import MARCReader
import json


def main():
    ingest_file = "augaspace.mrc"
    field_counts = {}
    with open(ingest_file,'rb') as fh:
        reader= MARCReader(fh)
        for record in reader:
            field_counter = 0
            while field_counter < 1000:
                field_tag = str(field_counter).zfill(3)
                field = record.get_fields(field_tag)
                if len(field) > 0:
                    if field_tag in field_counts:
                        field_counts[field_tag] = int(field_counts[field_tag]) + 1
                    else:
                        field_counts[field_tag] = 1
                field_counter = field_counter + 1
            
    
    with open("field_counts.csv","w") as f:
        w = csv.writer(f)
        w.writerows(field_counts.items())




if __name__ == "__main__":
    main()



""" StackBehavior - Tags Merge Topic Based
This module is for merging tags count(s) files into one file.
"""
import csv
import os

input_folder = './dataset/data/tag_counts/topic_based_year'
output_file = './dataset/data/tag_counts/tags_count_topic_based_merged_year.csv'

def readBatch():
    """ Read all files in '/dataset/data/tag_counts/topic_based' """
    for subdir, _, files in os.walk(input_folder):
        for file in files:
            path = os.path.join(subdir, file)
            with open(path, encoding="utf8") as csvfile:
                readCSV = csv.reader(csvfile, delimiter=',')
                next(readCSV, None) #Skip header
                for row in readCSV:
                    write_file(row)

def write_file(row):
    """ Write data from csv reader """
    with open(output_file, 'a', encoding="utf8", newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(row)
    csvfile.close()

readBatch()

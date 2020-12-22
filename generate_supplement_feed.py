"""generate_supplement_feed.
Simple CLI for supplement feed generation.
If there is any question, please reach to @yunruoliang
 
Usage:
 generate_supplement_feed.py [--result-filepath=<str>] [--supplement-feed-filepath=<str>] [--custom-label=<str>] [--custom-label-number=<str>]
 generate_supplement_feed.py (-h | --help)
 
Options:
 -h --help                             Show this screen.
 --result-filepath=<str>               Specify client reviewed result filepath
 --supplement-feed-filepath=<str>      Specify generated supplement feed filepath.
 --custom-label=<str>                  Specify the value of cusotm label, ex: gps-sta-client1-20200305
 --custom-label-number=<str>           Specify the name of custom label. [default: custom label 4]
 
"""
 
### python3 generate_supplement_feed.py --result-filepath="client_reviewed_result.csv" --supplement-feed-filepath="generated_supplement_feed.csv" --custom-label="gps-sta" --custom-label-number="custom label 4"
 
from docopt import docopt
from os import listdir
from os.path import isfile, join
import os
import pandas
import csv
import pdb
 
def generateSupplementFeed(result_filepath, supplement_feed_filepath, custom_label, custom_label_number):
 result = pandas.read_csv(result_filepath, header=0, encoding="utf-8")
 
 ids = result['Id']
 new_titles = result['New_title']
 Approveds = result['Approved']
 #subAccountIds = result['subAccountId']
 
 
 with open(supplement_feed_filepath, mode='a') as supplement_feed_file:
   nlp_writer = csv.writer(supplement_feed_file)
   nlp_writer.writerow(['id', 'title', custom_label_number, 'subAccountId'])
   supplement_feed_file.flush()
 
   for index, id in enumerate(ids):
     if Approveds[index] == True:
       #nlp_writer.writerow([ids[index], new_titles[index], custom_label, subAccountIds[index]])
       nlp_writer.writerow([ids[index], new_titles[index], custom_label])
       supplement_feed_file.flush()
 
def main():
   # get all input parameters
   arguments = docopt(__doc__)
   result_filepath = arguments['--result-filepath']
   supplement_feed_filepath = arguments['--supplement-feed-filepath']
   custom_label = arguments['--custom-label']
   custom_label_number = arguments['--custom-label-number']
   generateSupplementFeed(result_filepath, supplement_feed_filepath, custom_label, custom_label_number)
  
 
if __name__ == '__main__':
   main()

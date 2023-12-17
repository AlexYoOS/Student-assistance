#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_pet_labels.py
#                                                                             
# PROGRAMMER: 
# DATE CREATED:                                  
# REVISED DATE: 

##
# Imports python modules
from os import listdir

# TODO OVERALL: Define get_pet_labels function below please be certain to replace None
#       in the return statement with results_dic dictionary that you create 
#       with this function
# 
def get_pet_labels(image_dir):
    """
    Creates a dictionary of pet labels (results_dic) based upon the filenames 
    of the image files. These pet image labels are used to check the accuracy 
    of the labels that are returned by the classifier function, since the 
    filenames of the images contain the true identity of the pet in the image.
    Be sure to format the pet labels so that they are in all lower case letters
    and with leading and trailing whitespace characters stripped from them.
    (ex. filename = 'Boston_terrier_02259.jpg' Pet label = 'boston terrier')
    Parameters:
     image_dir - The (full) path to the folder of images that are to be
                 classified by the classifier function (string)
    Returns:
      results_dic - Dictionary with 'key' as image filename and 'value' as a 
      List. The list contains for following item:
         index 0 = pet image label (string)
    """

    # TODO: Step 1: Create list of files in directory using os.listdir() functionality -
    # how how listdir is already imported for you in line 20 above.
    # STORE THE LIST OF FILES IN THE VARIABLE NAME"in_files"
  
    # TODO: Step 2: Create empty dictionary for the results (pet labels, etc.)

    # Processes through each file in the directory, extracting only the words
    # of the file that contain the pet image label, furhter note use of range function below:
    # Using the range function in iteration is done to effectively save memory, as when processing each item
    # we do not load the full list into working memory as we would do when iterating 
    # over the full data container when writing: "for i n in_files: ..."
    for idx in range(0, len(in_files), 1):
       
       # : PLEASE DO NOT MISS TO IMPLEMENT THIS STEP! This step skips file if it starts with . (like .DS_Store of Mac OSX) because it 
       # isn't an pet image file
       if in_files[idx][0] != ".":
           # the following code that extracts the pet label from each item, must be placed inside this indentation!
           # Hence at precisely this indenation - 4 whitespaces / 1 tab inside the if-statement you must continue writing this funcion,
           # have a look at the hints file for a few further insights!

    return None

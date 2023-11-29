## convert all text to lowercase

with open('normalized/text_files/written-sources.txt', 'r') as data_file:
     
    # open output.txt file in append mode
    with open('normalized/written-sources-lowercase.txt', 'a') as output_file:
         
        # read data.txt file, convert case, 
        # and write to output.txt file
        output_file.write(data_file.read().lower())
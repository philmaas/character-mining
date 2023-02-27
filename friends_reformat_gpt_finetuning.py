import csv





with open('tsv/friends_transcripts.tsv', 'r') as input_file:
        reader = csv.DictReader(input_file, delimiter='\t')   
        with open('tsv/friends.csv', 'r') as second_input_file:
            reader2 = csv.DictReader(second_input_file, delimiter=',')

            # with open('output_file.tsv', 'w') as output_file:
            #     writer = csv.writer(output_file, delimiter='\t')

            #     # Write the header line
            #     writer.writerow(['season_id', 'episode_id', 'scene_id', 'speaker', 'transcript', 'episode_title'])

            for row in reader: 
                #print(row['season_id'])
                #for row2 in reader2:
                #     season = "s"+row2['Season'] 
                #     #format season string to with 2 digits
                #     if(len(season) == 2):
                #         season = "s0"+row2['Season']


                #     episode = "e"+ row2['Episode']
                #     if(len(episode) == 2):
                #         episode = "e0"+row2['Episode']

                #     # print(season)
                #     # print(episode)      
                #     #if(row['season_id'] == "s01" and row['episode_id'] == "e01"):
                new_line = row2['Title'] +  row2['Summary'] +  row['season_id'].capitalize() + row['episode_id'].capitalize()+ row['scene_id'].capitalize()+  row['speaker'].split(' ')[0]+": " + row['transcript']           
                print(new_line)
                        #writer.writerow(new_line)
                
                    



# Open the input file for reading
    # with open('tsv/friends_transcripts.tsv', 'r') as input_file:
    #     reader = csv.DictReader(input_file, delimiter='\t')
    #     # Open the output file for writing

    #     # with open('tsv/friends_kaggle_mainData.tsv', 'r') as second_input_file:
    #     #     reader2 = csv.DictReader(second_input_file, delimiter='\t')
    #         # with open('output_file.tsv', 'w') as output_file:
    #         #     writer = csv.writer(output_file, delimiter='\t')
                
    #         #     # Write the header line
    #             #writer.writerow(['season_id', 'episode_id', 'scene_id', 'speaker', 'transcript'])
    #             # Iterate through the rows in the input file
    #     for row in reader:
    #         #Split speaker into first name and last name
    #         #Capitalize first letter of first name
    #         #row['speaker'] = row['speaker'].split(' ')[0].capitalize()
    #         #row['scene_id'].capitalize()
    #         # Combine the specified columns into a new line
        
    #         if(row['season_id'] == season):
    #             new_line = row2['Title'] + ""+ row['season_id'].capitalize() +"\n"+ row['episode_id'].capitalize()+ "\n"+ row['scene_id'].capitalize()+  "\n"+ row['speaker'].split(' ')[0]+": " + row['transcript']           
    #             print(new_line)
        
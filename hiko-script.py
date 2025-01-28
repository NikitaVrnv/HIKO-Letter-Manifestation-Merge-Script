#!/usr/bin/env python3
import csv
import json

# Dictionary for converting ms_manifestation to preservation
manifestation_to_preservation = {
    'E': 'extract',
    'S': 'copy',
    'D': 'draft',
    'ALS': 'original',
    'O': 'other',
    'P': 'printed'
}

# Valid combinations between manifestation and preservation
valid_combinations = {
    'E': ['extract'],
    'S': ['copy'],
    'D': ['draft'],
    'ALS': ['original'],
    'O': ['other'],
    'P': ['printed']
}

# Reading the source CSV file
with open('input.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    
    # Creating a list to store new data
    new_data = []
    
    for row in reader:
        # Checking if the 'copies' field exists and is not empty
        if not row.get('copies'):
            print(f"Skipping row with empty 'copies' field: {row}")
            continue
        
        try:
            # Trying to load JSON from the 'copies' field
            copies = json.loads(row['copies'])
        except json.JSONDecodeError as e:
            # Logging the error and skipping the row
            print(f"Invalid JSON in 'copies' field: {row['copies']}. Error: {e}")
            continue
        
        new_copies = []
        
        for copy in copies:
            ms_manifestation = copy.get('ms_manifestation')
            preservation = copy.get('preservation')
            
            # Logic for combining values
            if ms_manifestation and preservation:
                # Both fields are filled: checking their validity
                if preservation in valid_combinations.get(ms_manifestation, []):
                    # Valid combination: keeping preservation
                    final_preservation = preservation
                else:
                    # Invalid combination: using value from manifestation
                    final_preservation = manifestation_to_preservation.get(ms_manifestation, preservation)
            elif ms_manifestation:
                # Only manifestation is filled: using its value
                final_preservation = manifestation_to_preservation.get(ms_manifestation, None)
            elif preservation:
                # Only preservation is filled: keeping it
                final_preservation = preservation
            else:
                # Both fields are empty: leaving as null
                final_preservation = None
            
            # Creating a new record without ms_manifestation
            new_copy = {
                'type': copy.get('type'),
                'preservation': final_preservation,
                'copy': copy.get('copy'),
                'manifestation_notes': copy.get('manifestation_notes'),
                'l_number': copy.get('l_number'),
                'repository': copy.get('repository'),
                'archive': copy.get('archive'),
                'collection': copy.get('collection'),
                'signature': copy.get('signature'),
                'location_note': copy.get('location_note')
            }
            new_copies.append(new_copy)
        
        # Converting back to JSON
        new_copies_json = json.dumps(new_copies)
        
        # Adding the new row to the result
        new_row = {
            'id': row['id'],
            'uuid': row['uuid'],
            'copies': new_copies_json
        }
        new_data.append(new_row)

# Writing the new CSV file
with open('output.csv', 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['id', 'uuid', 'copies']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
    writer.writeheader()
    writer.writerows(new_data)

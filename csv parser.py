
with open('Voorraad_woningen_en_niet_woningen_09012020_161347.csv') as infile:
    with open('Voorraad_woningen_en_niet_woningen.csv', 'w') as outfile:
        for line in infile:
            fields = line.split(';')
            outfile.write(','.join(fields))
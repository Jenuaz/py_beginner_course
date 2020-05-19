import json #this thing allow to work with JSON file
with open('inputfile.json', 'r') as input: #to get data we use open which name is inputfile and read mode
#by using (with) statement the file handle automatically be closed when the code ritch the exit block
#while we have file open all we need to do is use json.load to load data from our input file into python
    obj = json.load(input) #File will be loaded to obj we can work with
    print('Hello, ' + obj['name'])
    with open('output.txt','w') as output: 
        output.write(obj['name'] + "'s Hobbies:\n")
        for hobby in obj['hobbies']:
            output.write(hobby + "\n")

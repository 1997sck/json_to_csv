import json

if __name__ == '__main__':
    try:
        with open('input.json.py', 'r') as f:
            data = json.loads(f.read())

        output = ','.join([*data[0]])    # data[0] meanse first row
        for obj in data:                 # for loop to take all data
            output += f'\n{obj["Name"]},{obj["age"]},{obj["birthyear"]}'   # once value entering for these name , age, birth year it will come to next line to enter different value

        with open('output.csv', 'w') as f:
            f.write(output)
    except Exception as ex:
        print(f'Error: {str(ex)}')




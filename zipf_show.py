import json
import operator

def print_result(limit=25):
    with open("db.json", 'r') as file:
        data = json.loads(file.read())
        data["last_link_ending"] = 0
        sorted_data = sorted(data.items(), key=operator.itemgetter(1), reverse=True)
        for x in range(limit):
            key = sorted_data[x][0]
            value = sorted_data[x][1]
            print(key + ": ", str(value))

input_text = " "

while input_text != "":
    input_text = input("Command: ")
    if input_text == "show":
        printlimit = int(input("Enter limit: "))
        if printlimit == "":
            print_result()
        else:
            print_result(limit=printlimit)
    elif input_text == "exit":
        exit()

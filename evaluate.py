import re
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

def load(filename): #process input and output files
    with open(filename, 'r',encoding='utf-8') as file:
        data_array = file.readlines()
    datastr = "".join(data_array)

    punctuation = r'[，。！？「」：（）\n . o u t p u t i n : 》《 , 1 2 3 4 5 6 7 8 9 0 、O — ! …  "]'
    
    clean = re.sub(punctuation, '', datastr)#remove all punctuation
    characters = list(clean) #split into characters

    #now put markers around every character that is between markers
    inside_markers = False
    ind = 0
    for char in characters:
        if char == "@": #if @ - inside markers
           # print(char== "@")
            inside_markers = True
        elif char =="#": #if # - outside markers
            #print(char, "outside")
            inside_markers = False
        elif inside_markers: # if inside markers - reformat char
           # print(char == "#")
           # print(char, "inside")
            characters[ind] = "@@" + char + "##"
        else:
            pass

        ind+=1

    result = []
    for char in characters:
        if char != "@" and char != "#" and char != "@@@##": #strip of remaining outside markers and mistakes
            result.append(char)

    return (result)


def calculate_metrics(truths, predictions):
    accuracy = accuracy_score(truths, predictions)
    precision = precision_score(truths, predictions, average='macro', zero_division = 0)
    recall = recall_score(truths, predictions, average='macro', zero_division = 0)
    f1 = f1_score(truths, predictions, average='macro', zero_division = 0)
    return [accuracy, precision, recall, f1]

if __name__ == "__main__":

    predictions = "output.csv"  
    truths = "eval.txt"

    predictions = load(predictions) #process
    truths = load(truths)

    ind = 0 #how far until first different char

    for x in range(len(predictions)):
        if(truths[x].strip("@#") == predictions[x].strip("@#")):
            ind +=1
        else:
            break

    #only get matching - will change this
    predictions = predictions[:ind]
    truths = truths[:ind]

    evaluation_results = calculate_metrics(truths, predictions)
    print("Accuracy: ", evaluation_results[0],"\nPrecision: ", evaluation_results[1], "\nRecall: ", evaluation_results[2], "\nF1 Score: ", evaluation_results[3])

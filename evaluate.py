import re
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import difflib


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
            inside_markers = True
        elif char =="#": #if # - outside markers
            inside_markers = False
        elif inside_markers: # if inside markers - reformat char
            characters[ind] = "@@" + char + "##"
        else:
            pass

        ind+=1

    result = []
    for char in characters:
        if char != "@" and char != "#" and char != "@@@##": #strip of remaining outside markers and mistakes
            result.append(char)

    return result


def align_sequences(true, pred):
    sequence = difflib.SequenceMatcher(None, true, pred)
    #result of this:
    #(tag, i1, i2, j1, j2)

    #'replace' a[i1:i2] should be replaced by b[j1:j2].
    #'delete' a[i1:i2] should be deleted. Note that j1 == j2 in this case.
    #'insert' b[j1:j2] should be inserted at a[i1:i1]. Note that i1 == i2 in this case.
    #'equal' a[i1:i2] == b[j1:j2] (the sub-sequences are equal).

    #print(sm.get_opcodes())

    aligned_true = []
    aligned_pred = []

    for opcode, i1, i2, j1, j2 in sequence.get_opcodes():
        if opcode == 'equal': #add to both
            #print("T", (true[i1]),pred[j1])
            aligned_true.extend(true[i1:i2])
            aligned_pred.extend(pred[j1:j2])

        elif opcode == 'replace': #if difference in length of replace - add '-', else add chars to both
            max_len = max(i2 - i1, j2 - j1)
            ref_segment = list(true[i1:i2]) + ['-'] * (max_len - (i2 - i1))
            pred_segment = list(pred[j1:j2]) + ['-'] * (max_len - (j2 - j1))
            
            aligned_true.extend(ref_segment)
            # print("A:", aligned_true)
            aligned_pred.extend(pred_segment)
            # print("P:", aligned_pred)
            
        elif opcode == 'delete': #add as many '-'s as there are deleted characters
            aligned_true.extend(true[i1:i2])
            aligned_pred.extend(['-'] * (i2 - i1))

        elif opcode == 'insert': #add as many '-'s as there are inserted characters
            aligned_true.extend(['-'] * (j2 - j1))
            aligned_pred.extend(pred[j1:j2])

    return aligned_true, aligned_pred



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
    predictions, truths = align_sequences(truths, predictions) #get alignments

    evaluation_results = calculate_metrics(predictions, truths) #get metrics
    
    print("Accuracy: ", evaluation_results[0],"\nPrecision: ", evaluation_results[1], "\nRecall: ", evaluation_results[2], "\nF1 Score: ", evaluation_results[3])


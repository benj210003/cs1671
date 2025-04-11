import json

def read_data():
    with open('data/eval.txt', 'r', encoding='utf-8') as file:
        lines = file.readlines()
        return lines

def process(s):
    s = s.replace("@", "")
    s = s.replace("#", "")
    s = s.replace("\n", "")
    
    return s

if __name__ == "__main__":
    with open('fine_tuning_data.jsonl', mode='w', newline='', encoding='utf-8') as outfile:
        data = read_data()
        
        for row in data:
            prompt = process(row)
            response = row.replace("\n", "")
            
            fine_tuning_data = {
                "prompt": prompt,
                "completion": response
            }
            
            # Write this dictionary as a JSON object to the output file (JSON Lines format)
            json.dump(fine_tuning_data, outfile, ensure_ascii=False)
            outfile.write('\n')  # Ensure each entry is on a new line

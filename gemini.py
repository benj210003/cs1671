import time
from google import genai
import csv

def process(content):
    processed = []

    for s in content:
        s = s.replace("@", "")
        s = s.replace("#", "")
        s = s.replace("\n", "")
        processed.append(s)

    return processed

def read_data():
    with open('data/eval.txt', 'r', encoding='utf-8') as file:
        lines = file.readlines()
        return process(lines)

def n_shot(processed_data, prompt):
    MODEL = "gemini-2.0-flash"
    API_KEY = "AIzaSyCWETZzhoU_0ayN0AWnkj93QlQltxreolE"
    client = genai.Client(api_key=API_KEY)

    responses = []
    max_retries = 5
    retry_delay = 2

    for line in processed_data:
        retries = 0
        while retries < max_retries:
            try:
                print("Sending prompt")
                response = client.models.generate_content(
                    model=MODEL,
                    contents=prompt + line
                )
                print("Response succesfull")
                responses.append(response.text)
                break
            except Exception as e:
                if '429' in str(e):  # Check if error is related to resource exhausted (429)
                    print(f"Rate limit exceeded. Retrying in {retry_delay} seconds...")
                    time.sleep(retry_delay)
                    retry_delay *= 2  # Double the delay each time
                    retries += 1
                else:
                    print(f"An unexpected error occurred: {e}")
                    break

    return responses

if __name__ == "__main__":
    API_KEY = "AIzaSyCWETZzhoU_0ayN0AWnkj93QlQltxreolE"
    processed_data = (read_data())

    prompt_cn = "你是一位優秀的中文及臺語語言學家。"
    prompt_en = "You are an excellent linguist in Mandarin Chinese and Taiwanese Hokkien."

    prompt_zs_cn = prompt_cn + "你的任務是標記給定臺語句子中參雜的中文普通話。"
    prompt_fs_cn = prompt_zs_cn + """以下是一些範例。

    輸入：請上門的客人試食
    輸出：請上門的@@客##@@人##試食

    輸入：𪜶想欲的不巧一个公道佮尊嚴
    輸出：𪜶想欲的@@不##@@巧##一个公道佮尊嚴

    輸入：伊的修養真好，攏袂佮人冤家。
    輸出：伊的@@修##@@養##真好，攏袂佮人冤家。
    """

    prompt_zs_en = prompt_en + " Your task is to label the characters that are in Mandarin Chinese in the given Taiwanese-Hokkien sentence."
    prompt_fs_en = prompt_zs_en + """ Below are some examples.

    input: 請上門的客人試食
    output: 請上門的@@客##@@人##試食

    input: 𪜶想欲的不巧一个公道佮尊嚴
    output: 𪜶想欲的@@不##@@巧##一个公道佮尊嚴

    input: 伊的修養真好，攏袂佮人冤家。
    output: 伊的@@修##@@養##真好，攏袂佮人冤家。
    """

    responses = n_shot(processed_data, prompt_fs_en)
    file_path = 'prompt_fs_en.csv'

    with open(file_path, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(responses)
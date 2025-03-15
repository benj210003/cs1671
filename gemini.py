from google import genai

model = "gemini-2.0-flash"

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

input = '加 上 肉 仁 卵_@ 白 質 含_@ 量_@ 懸_@'

client = genai.Client(api_key="AIzaSyCWETZzhoU_0ayN0AWnkj93QlQltxreolE")
response = client.models.generate_content(
    model=model, 
    contents=prompt_fs_en + input
)
print(response.text)
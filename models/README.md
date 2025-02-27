# Models

## Token-Level Language Identification

> For more information, please see [Taiwanese Hokkien (Taigi) LLMs](https://github.com/lbh0830/TW-Hokkien-LLM?tab=readme-ov-file)

<style>
    .heatMap {
        width: 70%;
        text-align: center;
    }
    .heatMap th {
        background: DimGrey;
        word-wrap: break-word;
        text-align: center;
    }
    .heatMap tr:nth-child(5) { background: DarkGreen; }
    .heatMap tr:nth-child(6) { background: DarkGreen; }
</style>

<div class="heatMap">


| Name | Description | Type | Link |
| :--- | :---| :--- | :--- |
| Taigi-Llama-2-7B | Continued pre-training of a traditional Chinese Llama2 model using a Hokkien corpus. | 🦙 Base Model | [🤗 Bohanlu/Taigi-Llama-2-7B](https://huggingface.co/Bohanlu/Taigi-Llama-2-7B) |
| Taigi-Llama-2-13B | Continued pre-training of a traditional Chinese Llama2 model using a Hokkien corpus. | 🦙 Base Model | [🤗 Bohanlu/Taigi-Llama-2-13B](https://huggingface.co/Bohanlu/Taigi-Llama-2-13B) | 
| Taigi-Llama-2-Translator-7B | Fine-tuning Taigi-Llama-2 with parallel data in Taiwanese Hokkien, Mandarin Chinese, and English. | 🔁 Translation Model | [🤗 Bohanlu/Taigi-Llama-2-Translator-7B](https://huggingface.co/Bohanlu/Taigi-Llama-2-Translator-7B) |
| Taigi-Llama-2-Translator-13B | Fine-tuning Taigi-Llama-2 with parallel data in Taiwanese Hokkien, Mandarin Chinese, and English. | 🔁 Translation Model | [🤗 Bohanlu/Taigi-Llama-2-Translator-13B](https://huggingface.co/Bohanlu/Taigi-Llama-2-Translator-13B) |
| Taigi-Llama-2-Translator-7B + CM datasets | Fine-tuning Taigi-Llama-2-Translator-7B with parallel code-mixed data in Taiwanese Hokkien (matrix) and Mandarin Chinese (embedding). | 🆕 Our Model | |
| Taigi-Llama-2-Translator-13B + CM datasets | Fine-tuning Taigi-Llama-2-Translator-13B with parallel code-mixed data in Taiwanese Hokkien (matrix) and Mandarin Chinese (embedding). | 🆕 Our Model | |
</div class="heatMap">

## Other Potentially Useful Models

- [Taigi-Llama-2-Chat-7B](https://huggingface.co/Bohanlu/Taigi-Llama-2-Chat-7B): Fine-tuning Taigi-Llama-2 with Taiwanese Hokkien Hanzi instruction fine-tuning datasets.	

- [Taigi-Llama-2-Chat-13B](https://huggingface.co/Bohanlu/Taigi-Llama-2-Chat-13B): Fine-tuning Taigi-Llama-2 with Taiwanese Hokkien Hanzi instruction fine-tuning datasets.	
# Datasets

## Token-Level Language Identification

[Taiwanese-Hokkien_Mandarin_CM_Dataset](https://github.com/alznn/taiwanese-hokkien_mandarin_cm_dataset?tab=readme-ov-file)

- **Matrix language**: Taiwanese Hokkien

- **Embedding language**: Mandarin

- Taiwanese Han characters are tagged with `_@` at the end; Mandarin Han characters are not tagged.
    - *Note that there is a large overlap between Taiwanese Han characters and Mandarin Han characters, the dataset is created only for the task of machine translation, not token-level language identification*


## Other Potentially Useful Datasets

[Taiwanese Corpora](https://github.com/i3thuan5/tai5-uan5_gian5-gi2_hok8-bu7/wiki/Taiwanese-Corpus%E8%AA%9E%E6%96%99): largest corpora of different Taiwanese languages and dialects in various formats from various sources, including but not limited to dictionaries, religious texts, new reports, lyrics, textbooks.

- Contains iCorpus

[iCorpus](https://github.com/Taiwanese-Corpus/icorpus_ka1_han3-ji7?tab=readme-ov-file): sentences from various Taiwanese news reports from 2008 to 2014.

- Mandarin is automatically translated from Hokkien and manually corroborated

- Sentences are segemented into words and punctuations via an algorithm. There are inconsistencies between Mandarin and Hokkien. Some sentences failed to be segmented.

- Contains some English words (primarily names of people and places) and weird special characters


[iCorpus-100](https://huggingface.co/datasets/Bohanlu/iCorpus-100)

- A subset of 100 sentences from iCorpus that doesn't contain English words, weird special characters

- Not segmented

- Used for evaluating machine translation of [Hokkien LLMs](https://arxiv.org/pdf/2403.12024)

[TAIDE-14-Tasks-Hokkien](https://huggingface.co/datasets/Bohanlu/TAIDE-14-tasks-Hokkien) 

- Used for evaluating text generation tasks of [Hokkien LLMs](https://arxiv.org/pdf/2403.12024)

[Taiwanese Corpus](https://github.com/Taiwanese-Corpus): various collection of Taiwanese Hokkien corpus, including dictionary and bible translation.
# Token-Level Language Identificaiton in Taiwanse-Hokkien and Mandarin Chinese Code-Mixed Literature

## Why Is It Important?

Taiwanese Hokkien is dying language, it's becoming more like a dialect instead of a language because of its dwindling use of a formal writing system.
- Baby boomers: knows 95% of the language
- Gen X: knows 70-80% of the language
- Gen Z: less than a quarter can speak Hokkien well
- Can be used as a feature to more accurately translate code-mixed Mandarin-Hokkien sentences
- Can be used to automatically annotate code-mixed Mandarin-Hokkien speech data

There are only like 7 nlp papers on the hokkien language, and out of those 7, only 3 have some sort of release models or datasets but none has a code base.

NLP tools typically struggle to process code-switched data and so linguists are commonly forced to annotate such data manually.

Can be used in education and facilitate Mandarin readers to read Taiwanese literature

## Challenges

- Limited resources on code-mixed data

- Large overlap between the use of Han characters in Taiwanese Hokkien and Mandarin Chinese, a rule-based swap does not work well because of low resource on dictionary pairs and segmentation of words could be different in Hokkien and Mandarin.

## Evaluation

Code-mixed sentences from 80s Taiwanese literature where the matrix language is Mandarin Chinese and embedding language is Taiwanese Hokkien.
- How many of the words out of all are correctly tagged? But could be tricky because of there's a chance of generating different segmentation

Maybe we can compare the accuracies between code-mixed data where the matrix and embedding langauges are swapped

## Potential Helpful Heuristics

- Part of speech tagging. Because the majority of the code-switched words are nouns and place names

- Named entity tagging?
In Writeup.md, explain how Laplace smoothing works in general and how it is implemented in the EditDistance.py file. Why is Laplace smoothing needed in order to make the prob method work? In other words, the prob method wouldn’t work properly without smoothing – why?

1. Laplace smoothing adds a small value to the probability of all events to ensure that no event has a probability of 0 just because it never occurred in the sample. In the EditDistance.py file it is used when we say "counts[a][b] += .1" for all a and b in the alphabet. This is necessary in order to make the prob method work because all misspellings are technically likely, even if they are improbable. In addition, since we are using logs we cannot have a probability of 0 because we can not take the log of 0.

Describe the command-line interface for EditDistance.py. What command should you run to generate a model from /data/spelling/wikipedia_misspellings.txt and save it to ed.pkl?

2. There are two arguments inputed, an optional file source that you read misspellings from, and a required file store that you write the default dict of default dicts (prob) to.
      python3 EditDistance.py -s ed.pkl --source /data/spelling/wikipedia_misspellings.txt

This lab’s starter code also includes a file called LanguageModel.py that defines an n-gram language model. Read through the code for the LanguageModel class, then answer the following questions:

3. Unigrams and bigrams are supported by the given LanguageModel class.

4. The given LanguageModel class deals with the problem of 0-counts by using Laplace smoothing with a value called alpha, whose default is set to 0.1. This value is added to numerator and multiplied by the length of the vocabulary in the denominator to ensure that no probability is ever 0 (just really really small).

5. The “__contains__()” method of the LanguageModel class returns true if a word is contained in the vocabulary of the LanguageModel class.

6. The get_chunks method limits the amount of memory Spacy uses while loading a very large document by allowing the user to specify a chunk_size (default = 100,000). Get_chunks then reads in that many lines of the file at a time, processes those lines, and then moves on to the next chunk. When it reaches the end of the file and therefore does not have chunk-size many lines, we break out of the get_chunks method.

7. The command -line interface for LanguageModel.py takes in 4 arguments. First, a required file '--store' to write the dictionary of probabilities to. Then, an optional float "--alpha" that is default set to 0.1, this value specifies the amount that we are using to Laplace Smooth. Then, an optional int "--vocab" with a default value of 40,000. This is used to add the '--vocab' most common words in the vocabulary of the language model. Then there "source" which points to one or many files that we use to build the LanguageModel.

python3 LanguageModel.py --store lm.pkl --alpha 0.1 --vocab 40000 /data/gutenberg/*.txt

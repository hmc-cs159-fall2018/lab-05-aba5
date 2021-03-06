1. Laplace smoothing adds a small value to the probability of all events to ensure that no event has a probability of 0 just because it never occurred in the sample. In the EditDistance.py file it is used when we say "counts[a][b] += .1" for all a and b in the alphabet. This is necessary in order to make the prob method work because all misspellings are technically likely, even if they are improbable. In addition, since we are using logs we cannot have a probability of 0 because we can not take the log of 0.

2. There are two arguments inputed, an required file source that you read misspellings from, and a required file store that you write the default dict of default dicts (prob) to.
      python3 EditDistance.py -s ed.pkl --source /data/spelling/wikipedia_misspellings.txt

3. Unigrams and bigrams are supported by the given LanguageModel class.

4. The given LanguageModel class deals with the problem of 0-counts by using Laplace smoothing with a value called alpha, whose default is set to 0.1. This value is added to numerator and multiplied by the length of the vocabulary in the denominator to ensure that no probability is ever 0 (just really really small).

5. The “__contains__()” method of the LanguageModel class returns true if a word is contained in the vocabulary of the LanguageModel class.

6. The get_chunks method limits the amount of memory Spacy uses while loading a very large document by allowing the user to specify a chunk_size (default = 100,000). Get_chunks then reads in that many lines of the file at a time, processes those lines, and then moves on to the next chunk. When it reaches the end of the file and therefore does not have chunk-size many lines, we break out of the get_chunks method.

7. The command -line interface for LanguageModel.py takes in 4 arguments. First, a required file '--store' to write the dictionary of probabilities to. Then, an optional float "--alpha" that is default set to 0.1, this value specifies the amount that we are using to Laplace Smooth. Then, an optional int "--vocab" with a default value of 40,000. This is used to add the '--vocab' most common words in the vocabulary of the language model. Then there is "source" which points to one or many files that we use to build the LanguageModel.

python3 LanguageModel.py --store lm.pkl --alpha 0.1 --vocab 40000 /data/gutenberg/*.txt
**

6., 7., 8. Autocorrect.py failed after about an hour, and gave us the error message "Problem with ~ and ~". We checked multiple times that we had the most recent edits to the starter code, but we were unable to find the source of this error. We worked for more than 8 hours, and we didn't feel that we would be able to progress any more to find our mistake. Also, we all don't have any more time to work on this lab, since we all have other things that would start to pile up, and we are deciding to proioritize sleep. We will make sure to get started on the next lab a little earlier. Thanks for understanding!

11. Our approach is to modify the align function in EditDistance. When we calculate the cost of going from the intended word to the observed word, we will check to see if there are two consecutive tuples of the form (x, y), (y, x). In this case, we know there is a transposition. A transposition is more likely than the substitution of two random letter. We will account for this difference by decreasing the edit distance cost by subtracting the average of the probabilities of (x, y) and (y, x).

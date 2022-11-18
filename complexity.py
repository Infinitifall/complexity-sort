import re

def complexity_sort(sentences_array):
    words_count = dict()
    sentences_words = dict()

    # populate words_count with global count of words
    # and sentences_words with words from each sentence
    for sentence in sentences_array:
        words = list()
        temp_words = re.findall(r'[a-zA-Z]+',sentence)
        for word in temp_words:
            words.append(word.lower())
        
        sentences_words[sentence] = words

        for word in words:
            if word in words_count:
                words_count[word] += 1
            else:
                words_count[word] = 1

    # create complexity value for each word
    words_complexity = dict()
    max_word_count = max(words_count.values())
    for word in words_count.keys():
        words_complexity[word] = max_word_count / words_count[word]
    
    # populate sentences_complexity
    sentences_complexity = list()
    for sentence in sentences_array:
        words = sentences_words[sentence]
        number_of_words = len(words)
        
        temp_list = [sentence, 0]

        # add up the complexity of each word
        for word in words:
            temp_list[1] += words_complexity[word]
        
        if number_of_words not in [0, 1]:
            temp_list[1] /= number_of_words ** (1 - 2/3)  # normalize by length powered to 1 - delta

        sentences_complexity.append(temp_list)
    
    # finally, sort sentences by their complexity in desc order
    return sorted(sentences_complexity, key=lambda x: -x[1])


if __name__ == "__main__":
    import sys
    
    my_sentences = sys.stdin.readlines()
    sorted_sentences = complexity_sort(my_sentences)

    for element in sorted_sentences:
        element[1] = round(element[1], 2)
        print(element)

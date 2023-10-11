#对 生字清单(写字表)每个字组词2个，优先使用词语表里的，然后用词语列表里的。
#列出词语表内未被使用de词语
print('======词语生成V1.0======')
print('本程序对生字清单(写字表)每个字组词2个，优先使用词语表里的，然后用词语列表里的，否则留空。')
#列出词语表内未被使用de词语')
# Create a dictionary to store words containing new words
new_words_word_dict = {}


# Define a function to find words containing new words
def find_words(new_word, word_list):
    # words_containing_new_word = []
    for word in word_list:
        if new_word in word:
            words_containing_new_word.append(word)
    return words_containing_new_word


# Input new words list
new_words_input = input("输入生字清单 用空格分开每个字，回车确定: ")
new_words_input = new_words_input.replace('\n', ' ')  # Replace newline characters with spaces
new_words_list = new_words_input.split()
# print('new_words_list写字表',new_words_list)
# Input vocabulary list
vocabulary_input = input("输入 词语表 ，用空格分开，回车确定: ")
vocabulary_input = vocabulary_input.replace('\n', ' ')  # Replace newline characters with spaces
vocabulary_list = vocabulary_input.split()
# print('vocabulary_list词语表',vocabulary_list)
# Input word list
word_input = input("输入备用词语列表，用空格分开，回车确定: ")
word_input = word_input.replace('\n', ' ')  # Replace newline characters with spaces
word_list = word_input.split()
# print('word_list词语列表',word_list)
# Iterate through the new words list and find two words containing each new word
for new_word in new_words_list:
    words_containing_new_word = []
    # First, search in the vocabulary list
    words_containing_new_word = find_words(new_word, vocabulary_list)
    # If not found in the vocabulary list, search in the word list
    # if not words_containing_new_word:
    words_containing_new_word = find_words(new_word, word_list)
    # If still not found, write as "Pending"
    if not words_containing_new_word:
        words_containing_new_word = ["Pending"]
    # Store the results in the dictionary
    # new_words_word_dict[new_word] = words_containing_new_word
    new_words_word_dict[new_word] = set(words_containing_new_word)  # Convert to set to remove duplicates
    # Remove matched words from vocabulary list and word list
    for matched_word in words_containing_new_word:
        if matched_word in vocabulary_list:
            vocabulary_list.remove(matched_word)
        if matched_word in word_list:
            word_list.remove(matched_word)
    # print('new_word', new_word)
    # print('word_list', word_list)
# Output the results
for new_word, word_lists in new_words_word_dict.items():
    result = f"{new_word}: {' '.join(word_lists)}"
    print(result)

# print(new_words_word_dict)

# Output the updated vocabulary list and word list
print("\nUpdated Vocabulary List词语表中剩余的词语:", ' '.join(vocabulary_list))
print("Updated Word List词语列表中剩余的词语:", ' '.join(word_list))

# Output the results to a text file
output_file_name = "new_words_output.txt"
with open(output_file_name, "w") as output_file:
    for new_word, word_set in new_words_word_dict.items():
        result = f"{new_word}: {' '.join(word_set)}\n"
        output_file.write(result)

# Output the updated vocabulary list and word list
with open(output_file_name, "a") as output_file:
    output_file.write("\nUpdated Vocabulary List: " + ' '.join(vocabulary_list) + "\n")
    output_file.write("Updated Word List: " + ' '.join(word_list))
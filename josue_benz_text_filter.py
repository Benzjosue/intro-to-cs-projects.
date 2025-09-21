'''
Program name: Text Filter
Author name: Huirong Chai
Description:  This program filters out banned words from a given sentence.

'''

banned_list = ['Turkey', 'Dog', 'Fox', 'Cat', 'Chicken']

def text_filter(message):
    # Parameter(s): message, a string representing the message to be filtered
    word_list = message.split()
    clean = ''
    for word in word_list:
        if word not in banned_list:
            clean += word + ' '
    return clean[:-1]

if __name__ == '__main__':
    user_message = input('>:')
    print('Input Message:', user_message)
    cleaned_message = text_filter(user_message)
    print('Output Message:', cleaned_message)
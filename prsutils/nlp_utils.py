""" nlp_utils.py
A collection of universally applicable util functions for the (pre-)processing
of input text (files).
"""

FOOTNOTE_CHARS = ['[', ']']
PUNCTUATION_CHARS = [',', '.', ':', '?', '!', '"', "'", ';']

class TextCleaner:
    """ Offers various functions to clean up text.
    """

    def __init__(self,
                 footnote_chars=FOOTNOTE_CHARS,
                 punctuation_chars=PUNCTUATION_CHARS):
        """
        :param footnote_chars: list of bad footnote chars
        """

        self.fn_chars = footnote_chars
        self.punct_chars = punctuation_chars


    def remove_footnote_numbers(self, input_text):
        """ Removes irregularly places numbers from strings, e.g. turns
        'They are only used in 1texts without a bibliography[2].' to
        'They are only used in texts without a bibliography.'

        :param input_text: the string containing footnotes
        :return: string with same text, but without footnote indicator numbers
        """

        # Remove numbers like 4 or numbers surrounded by brackets like [4] at
        # the beginning and end of words, however:
        # numbers surrounded by spaces are regular and should not be removed.

        # get individual words
        words = input_text.split(' ')

        # check each word for the stated criteria
        for i, word in enumerate(words):

            # is it a number? or is it something surrounded by brackets?
            if not is_number(word) and not (word[0]=='[' and word[-1]==']'):

                # does it start with a number or a footnote character?
                while is_number(words[i][0]) or words[i][0] in self.fn_chars:
                    words[i] = words[i][1:]

                # does it end with one?
                while is_number(words[i][-1]) or words[i][-1] in self.fn_chars:
                    words[i] = words[i][0:-1]

                # does it end with one followed by a punctuation character?
                if words[i][-1] in self.punct_chars:
                    while is_number(words[i][-2]) or words[i][-2] in self.fn_chars:
                        words[i] = words[i][0:-2] + words[i][-1]

        # recreate original string with cleaned words
        output_string = ' '.join(words)

        return output_string


# --------------------- helper functions -------------------------------------
def is_number(input_string):
    ''' Checks if the input string expresses a numerical number.
    c.f. https://www.pythoncentral.io/how-to-check-if-a-string-is-a-number-
    in-python-including-unicode/

    :param input_string: string - word which is potentially a number
    :return: boolean - True if input is number
    '''

    try:
        float(input_string)
        return True
    except ValueError:
        pass

    try:
        import unicodedata
        unicodedata.numeric(input_string)
        return True
    except (TypeError, ValueError):
        pass

    return False

if __name__ == '__main__':

    corrupted_string = "Die 1Kanzlerin hat2 beschlossen[3], zu [4]gehen und [3] einen [Denkzettel2] zu hinterlassen."
    cleaner = TextCleaner()
    clean_string = cleaner.remove_footnote_numbers(corrupted_string)

    print(corrupted_string)
    print(clean_string)


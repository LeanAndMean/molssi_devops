"""
string_util.py
A sample repository for the MolSSI Workshop at UF.

Misc. string processing functions.
"""


def title_case(sentence):
    """
    Convert a string to title case.

    Parameters
    ----------
    sentence : string
        String to be converted to a title.

    Returns
    -------
    title_case_sentence : string
        Input string as a title.
    
    Example
    -------
    >>> title_case('ThIS iS a StrInG to BE ConVerTed.')
        'This Is A String To Be Converted.'
    """
    # Check that input is string.
    if not isinstance(sentence, str):
        raise TypeError("Invalid input %s - Input must be type string" %(sentence))
    if len(sentence) == 0:
        return ''
    title_case_sentence = sentence[0].upper()
    for char_idx in range(1, len(sentence)):
        if title_case_sentence[-1] == ' ':
            title_case_sentence += sentence[char_idx].upper()
        else:
            title_case_sentence += sentence[char_idx].lower()
    return title_case_sentence

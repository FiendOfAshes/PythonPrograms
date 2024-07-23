def morse_coder(string):
    morse_dict = {'A': '. -', 'B': '- . . .', 'C': ' - . - .', 'D': ': - . .', 'E': '.',
                  'F': '. . - .', 'G': '- - .', 'H': '. . . .', 'I': '. .', 'J': '. - - -',
                  'K': '- . -', 'L': '. - . .', 'M': '- -', 'N': '- .', 'O': '- - -',
                  'P': '. - - .', 'Q': '- - . -', 'R': '. - .', 'S': '. . .', 'T': '-',
                  'U': '. . -', 'V': '. . . -', 'W': '. - -', 'X': '- . . -', 'Y': '- . - -', 'Z': '- - . .'}

    morse = ''

    for i in string:
        if i in morse_dict.keys():
            morse += morse_dict[i]
            morse += '  '
    return morse
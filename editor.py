formatters = 'plain bold italic header link inline-code new-line ordered-list unordered-list'.split()
parent_string = ''


def help_call():
    print('Available formatters: plain bold italic header link inline-code new-line ordered-list unordered-list'
          '\nSpecial commands: !help !done')


def done_call():
    with open('output.md', 'w') as f:
        f.write(parent_string)
    quit()


def header(level, text):
    hash_mark = '#'
    hash_mark *= int(level)
    if parent_string == '':
        add_to_parent(f'{hash_mark} {text}\n')
    else:
        add_to_parent(f'\n{hash_mark} {text}\n')
    print(parent_string)


def get_level():
    while True:
        user = input('Level: ')
        if 0 < int(user) <= 6:
            return user
        else:
            print('The level should be within the range of 1 to 6')


def get_text():
    return input('Text: ')


def get_label_url(pref):
    if pref == 'url':
        url = input('URL: ')
        return url
    elif pref == 'label':
        label = input('Label: ')
        return label


def new_line():
    add_to_parent('\n')
    print(parent_string)


def plain(text):
    add_to_parent(text)
    print(parent_string)


def inline_code(text):
    add_to_parent(f'`{text}`')
    print(parent_string)


def bold(text):
    add_to_parent(f'**{text}**')
    print(parent_string)


def italic(text):
    add_to_parent(f'*{text}*')
    print(parent_string)


def link(label, url):
    add_to_parent(f'[{label}]({url})')
    print(parent_string)


def add_to_parent(text):
    global parent_string
    parent_string += text


def ordered_unordered_list(ordered=False):
    while True:
        n_rows = int(input('Number of rows: '))
        if n_rows <= 0:
            print('The number of rows should be greater than zero')
        else:
            break
    rows = list()
    for i in range(1, n_rows + 1):
        rows.append(input(f'Row #{i}: '))
    for i in range(0, len(rows)):
        if ordered == True:
            add_to_parent(f'{i+1}. {rows[i]}\n')
        else:
            add_to_parent(f'* {rows[i]}\n')
    print(parent_string)


def main():
    while True:
        user_input = input('Choose a formatter: ')

        if user_input == '!help':
            help_call()
        elif user_input == '!done':
            done_call()
        elif user_input in formatters:
            if user_input == 'header':
                header(get_level(), get_text())
            elif user_input == 'plain':
                plain(get_text())
            elif user_input == 'inline-code':
                inline_code(get_text())
            elif user_input == 'bold':
                bold(get_text())
            elif user_input == 'italic':
                italic(get_text())
            elif user_input == 'new-line':
                new_line()
            elif user_input == 'link':
                link(get_label_url('label'), get_label_url('url'))
            elif user_input == 'ordered-list':
                ordered_unordered_list(ordered=True)
            elif user_input == 'unordered-list':
                ordered_unordered_list()

        else:
            print('Unknown formatting type or command')
            continue


main()

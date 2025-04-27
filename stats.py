
def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents

def get_num_words(text):
    num_words = len(text.split())
    return f"Found {num_words} total words"

def get_character_count(text):
    character_count = {}
    for c in list(text):
        if c.lower() in character_count:
            character_count[c.lower()] += 1
        else:
            character_count.update({c.lower():1})
    return character_count

def sort_character_count(character_count):
    sorted_characters = sorted(character_count.items(), key=lambda character: character[1], reverse=True)
    return dict(sorted_characters)


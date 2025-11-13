def get_word_count(text):
    count = len(text.split())
    return count

def get_char_count(text):
    counts = {}
    for char in text:
        char = char.lower()
        if not char.isalpha():
            continue
        if char not in counts:
            counts[char] = 0
        counts[char] += 1
    return counts

def get_num(item):
    return item['num']

def sorted_list(counts_dict):
    unsorted = []
    for k in counts_dict:
        unsorted.append({'char': k, 'num': counts_dict[k]})

    unsorted.sort(reverse=True, key = get_num)
    return unsorted






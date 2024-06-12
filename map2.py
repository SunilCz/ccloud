def mapper(input_data):
    word_counts = {}
    for word in input_data.split():
        word_counts[word] = word_counts.get(word, 0) + 1
    return word_counts

def reducer(mapped_data):
    reduced = {}
    for word_count in mapped_data:
        word, count = word_count
        reduced[word] = reduced.get(word, 0) + count
    return reduced

if __name__ == "__main__":
    input_data = "Deer Bear River Car Car River Deer Car Bear"
    
    mapped_data = mapper(input_data)
    reduced_data = reducer(mapped_data.items())
    
    for word, count in reduced_data.items():
        print(f"{word}: {count}")

words = ["apple", "banana", "cherry", "date", "elderberry", "fig"]
min_length=6

def length(w):
    return len(w) >= min_length

min=filter(length,words)
print(min)
min_list=list(min)
print(min_list)
from collections import Counter

while True:
    try:
        a = input().strip()
        b = input().strip()
    except EOFError:
        break

    ca = Counter(a)
    cb = Counter(b)

    common_counts = {ch: min(ca[ch], cb[ch]) for ch in set(a) & set(b)}
    result = ''.join(ch * common_counts[ch] for ch in sorted(common_counts.keys()))
    
    print(result)

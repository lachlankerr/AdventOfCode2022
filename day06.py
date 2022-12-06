def get_buffer():
    '''
        Reads the input directly from file, no processing required
    '''

    buffer = []
    with open('day06-input.txt') as f:
        buffer = f.read()
    return buffer

def solution(window_size):
    '''
        Finds the first index where the sliding window, of specified size, contains only unique characters
    '''

    buffer = get_buffer()
    chars = {}
    for i in range(len(buffer)):

        chars.setdefault(buffer[i], 0)
        chars[buffer[i]] += 1

        if sum(chars.values()) == window_size and len(chars.values()) == window_size:
            #print(chars)
            break
        
        if sum(chars.values()) == window_size:
            chars[buffer[i - window_size + 1]] -= 1
            if chars[buffer[i - window_size + 1]] == 0:
                del chars[buffer[i - window_size + 1]]
    
    return i + 1

def reddit_solution(w):
    '''
        https://www.reddit.com/r/adventofcode/comments/zdw0u6/2022_day_6_solutions/iz3m3pi/
    '''

    signal = get_buffer()
    for i in range(w, len(signal)):
        s = signal[i-w:i]
        if len(set(s)) == w:
            return i

if __name__ == "__main__":
    print(f"Day 6 part 1: {solution(4)}")
    print(f"Day 6 part 2: {solution(14)}")
    print(f"Day 6 part 1 (reddit): {reddit_solution(4)}")
    print(f"Day 6 part 2 (reddit): {reddit_solution(14)}")
"aaaabbcccccccddddgggggggggggg"

"4a2b7c4d12g"

#наша задача написать задачу которая на входе будет получать такую строку а на выходе (возвращать) вторую строку (4 символа а, потом2 символа b и тд)

def rle_encode(s):
    prev_char = s[0]
    print(prev_char)
    count = 0
    for cur_char in s:

        if prev_char != cur_char:
            print(count)
            print(cur_char)
            prev_char = cur_char
            count = 0
            count += 1
    print(count)
print(rle_encode("aaaabbcccccccddddgggggggggggg"))
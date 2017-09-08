
# code-katas

StringPyramid Best Practice solution1 

def watch_pyramid_from_the_side(characters):
    if not characters : return characters
    baseLen = len(characters)*2-1
    return '\n'.join( ' '*(i) + characters[i]*(baseLen-2*i) + ' '*(i) for i in range(len(characters)-1,-1,-1) )


def watch_pyramid_from_above(characters):
    if not characters : return characters
    baseLen = len(characters)*2-1
    return '\n'.join( characters[0:min(i,baseLen-1-i)] + characters[min(i,baseLen-1-i)]*(baseLen-2*min(i,baseLen-1-i)) + characters[0:min(i,baseLen-1-i)][::-1] for i in range(baseLen) )


def count_visible_characters_of_the_pyramid(characters):
    return -1 if not characters else (len(characters)*2-1)**2


def count_all_characters_of_the_pyramid(characters):
    return -1 if not characters else sum( (2*i+1)**2 for i in range(len(characters)) )


StringPyramid Best Practice solution2

def watch_pyramid_from_the_side(c, i=1, acc=[]):
    if c == None: return c
    if not c: return '\n'.join(acc)
    return watch_pyramid_from_the_side(c[:-1], i+2, [' '+l+' 'for l in acc]+[c[-1]*i])

def watch_pyramid_from_above(c, i=1, acc=[]):
    if c == None: return c
    if not c: return '\n'.join(acc)
    return watch_pyramid_from_above(c[:-1], i+2, [c[-1] * i] + [c[-1]+l+c[-1] for l in acc] + [c[-1] * i] * bool(acc))

def count_visible_characters_of_the_pyramid(c):
    return c and (2*len(c)-1)**2 or -1

def count_all_characters_of_the_pyramid(c):
    return c and (4*len(c)**3-len(c))//3 or -1


Kata6: Replace with Alphabet position
- Module: alphabet_position.py
- Tests: test_alphabet_position.py
- URL: https://www.codewars.com/kata/546f922b54af40e1e90001da

Kata6: Simple Encryption1, alternating split
- Module:  simple_encrypt1.py
- Tests:  test_simple_encrypt1.py.
- URL: https://www.codewars.com/kata/57814d79a56c88e3e0000786

Kata5: Extract domain name from a URL
- Module: domain_name.py
- Tests:  test_domain_name.py
- URL:  https://www.codewars.com/kata/514a024011ea4fb54200004b

Kata6: Vasya - Clerk
- Module:  vasya_clerk.py
- Tests:   test_vasya_clerk.py
- URL: https://www.codewars.com/kata/555615a77ebc7c2c8a0000b8


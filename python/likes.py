def likes(names):
    plural = True
    if len(names) < 2:
        plural = False
    
    if len(names) == 0:
        names.append("no one")
    elif len(names) == 2:
        names.insert(1," and ")
    elif len(names) == 3:
        names.insert(1,", ")
        names.insert(3," and ")
    elif len(names) >= 4:
        sum_people = len(names) - 2
        names.insert(1,", ")
        # 'invinsible' variable _
        for _ in range(sum_people):
            names.pop()
        names.append(f" and {sum_people} others")
        
    if plural:
        names.append(" like this")   
    else:
        names.append(" likes this")  

    print(''.join(names))
    return ''.join(names)

if __name__ == '__main__':
    assert likes([]) == 'no one likes this'
    assert likes(['Peter']) == 'Peter likes this'
    assert likes(['Jacob', 'Alex']) == 'Jacob and Alex like this'
    assert likes(['Max', 'John', 'Mark']) == 'Max, John and Mark like this'
    assert likes(['Alex', 'Jacob', 'Mark', 'Max']) == 'Alex, Jacob and 2 others like this'

"""
Best Kata:
def likes(names):
    n = len(names)
    return {
        0: 'no one likes this',
        1: '{} likes this', 
        2: '{} and {} like this', 
        3: '{}, {} and {} like this', 
        4: '{}, {} and {others} others like this'
    }[min(4, n)].format(*names[:3], others=n-2)
"""
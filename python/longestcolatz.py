number_chain_mapping = {1: 0}

highest = 1   # taking highest running chain_length into note
limit = 1000001
holy_grail = 1


def engine(base, chain_length=0):
    global highest
    global holy_grail
    if base in number_chain_mapping:
        return number_chain_mapping[base]
    else:
        if base % 2 == 0:
            chain_length = engine(base/2)
            meaning = 1 + chain_length
            if meaning > highest:
                highest = meaning
                holy_grail = base
            number_chain_mapping[base] = meaning
            return meaning
        else:
            next = 3 * base + 1
            chain_length = engine(next)
            meaning = 1 + chain_length
            if meaning > highest and base <= limit:
                highest = meaning
                holy_grail = base
            number_chain_mapping[base] = meaning
            return meaning


for number in range(1000001, 1, -1):
    if number in number_chain_mapping:
        pass
    else:
        engine(number)
print holy_grail

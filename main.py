def init_data(FILE): # "input.txt"
    with open(FILE, "r") as f:
        def clean_lines(f):
            return f.read().rstrip().split("\n")
        return [(name, lst) for name, *lst in
                 [line.split(" ") for line in clean_lines(f)]]

def partition(prefs):
    return (prefs[:len(prefs)//2], prefs[len(prefs)//2:])

def half_hash(pref_list):
    return {name:lst for name,lst in pref_list}

def gen_hash(hash1, hash2):
    return {**hash1, **hash2}

def prop(prefP, prefA, pairings,run):
    return (prefP, prefA, [*pairings, *[(p,a[0]) for p,a in prefP]], True)

def jilt(x,y,z,run):
    return (x+1, y+1, z+1, True)

def isComplete(x,y,z,run):
    return (x,y,z,True) if sum((x,y,z)) < 100 else (x,y,z,False)

def state_machine(x,y,z,run):
    x,y,z,run = isComplete(*jilt(*prop(x,y,z,run)))
    if not run:
        return "DONE"
    return state_machine(x,y,z,run)

STATE = init_data("input.txt")
proposers, acceptors = partition(STATE)

print(prop(proposers,acceptors,[],True)[2])




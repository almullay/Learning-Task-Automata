from sys import argv
import time
''' arg1: NFA / DFA file name, arg2: character to lump by'''

file = open(argv[1], 'r')
lines = file.readlines()
file.close()

states = int(lines[0].split()[0])

partition = list(range(states))

strings = lines[4::]

alphabet = list(set([i.split()[1] for i in strings]))
start = time.perf_counter()
lumped_flag = False
while not lumped_flag:
    lumped_flag = True
    for i in range(states):
        for a in alphabet:
            #print({int(k.split()[2]) for k in strings if k.split()[0]==str(i) and k.split()[1]==a})
            equivalence_Class = list({int(k.split()[2]) for k in strings if k.split()[0]==str(i) and k.split()[1]==a})
            if len(equivalence_Class) > 1:
                #print("lumping")
                lumped_flag = False
                m = min(equivalence_Class)
                for s in equivalence_Class:
                    partition[s] = m
    if lumped_flag:
        continue
    # TO-DO: add contradiction checking here: check if all equipartitions have same accept/reject values post-merge
    # if not, the lump_letter must be important to the DFA, because the ProdMDP states must have same accept/
    # reject value if the lump_letter label truly does not matter in the underlying DFA.
    
    next_strings = []
    for i in range(len(strings)):
        head, char, tail = strings[i].split()
        head = int(head)
        tail = int(tail)
        next_strings.append(str(partition[head]) +" "+ char +" "+ str(partition[tail]))
        # Debugging:
        # if partition[head] != partition[tail]:
        #     print(head, char, tail)
    strings = list(set(next_strings))

#print(strings)

f = open(argv[1] + "_cone_lumped", "w")
new_states = str(max(partition)+1) # plus 1 since state numbering starts at 0
accept_states = list(map(int, lines[2].split()[1::]))
new_accept_states = list(set([ str(partition[i]) for i in accept_states ]))
new_initial = str(partition[int(lines[3].split()[0])])
f.write(new_states+"\n")
f.write(lines[1])
f.write(str(len(new_accept_states)))
for i in new_accept_states:
    f.write(" "+i)
f.write("\n")
f.write(new_initial+"\n")
for i in strings:   
    f.write(i +"\n")
f.close()
print("time: ", time.perf_counter()-start)
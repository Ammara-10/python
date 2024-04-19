names=['ammara','minahil','ifra','zunaira','ammara','minahil,''laiba','ifra','ammara']
unqiues=[]
for name in names:
    if name not in unqiues:
        unqiues.append(name)
print(unqiues)
#Practice's exercise about LIST

fhand= open("mbox-short.txt")
for line in fhand:
 line = line.rstrip()
 #"Otheroption"if leni == "" :continue
 words = line.split()
 #"otheroption"if len(words) <1 :continue
 if words == [] :continue
 if words[0] != "From" :continue
 correct = words[2]
 print(correct)
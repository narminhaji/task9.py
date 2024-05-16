
with open('task.txt', encoding='utf-8', mode='task') as task:
    h = task.readline()
    
with open ('text.txt', encoding='utf-8', mode='text') as text:
    text.write(h.upper())
# LIFO
# Last IN - First Out
browsing_session = []
browsing_session.append(1)   # add on top of stack
browsing_session.pop()       # remove from top of stack
if not browsing_session:     # if nothing in stack keep last one on top
    browsing_session[-1]
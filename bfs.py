from collections import deque
from re import search
searchGraph = {}
searchGraph['You']=['Alice','Bob']
searchGraph['Alice']=['Jewel','Royston','Shawn']
searchGraph['Bob']=['Ross','Ted','Robin']
searchGraph['Jewel']=['Mariam']
searchGraph['Royston']=[]
searchGraph['Shawn']=[]
searchGraph['Ross']=[]
searchGraph['Ted']=[]
searchGraph['Robin']=[]
searchGraph['Mariam']=[]


def searchNameEndingWithM(name):
    search_queue = deque()
    search_queue+=searchGraph[name]
    searched=[]
    while search_queue:
        person = search_queue.popleft()
        if not person in searched:
            if ending_with_m(person):
                return person
            else:
                search_queue+=searchGraph[person]
                searched.append(person)
    return 'Could not find such a person'

def ending_with_m(person):
    return person[-1]=='m'


print(searchNameEndingWithM('You'))
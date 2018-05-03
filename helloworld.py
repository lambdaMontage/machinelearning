import test
import os

''' if os.path.exists('/Users/shihao/Desktop/python'):
    data = open('hello.txt')
    for each_line in data:
        if not each_line.find(':') == -1:
            try:
                (role,line) =  each_line.split(':',1)
                print(role,end='')
                print(' said: ' , end='')
                print(line,end='')
            except:
                pass

    data.close()
else:
    print('The data is missing!')
    #TODO  100页
each_line = "I tell you: , there's no such thing as  a flying circus."
print(each_line.find(':')) '''

# mins = [1,2,3]
# secs = [m * 60 for m in mins]
# print (secs)
#
# lower = ["I", "don't", "like", "spam"]
# upper = [s.upper() for s in lower]
# print(lower)


def sanitize(time_string):
    if '-' in time_string:
        splitter = '-'
    elif ':' in time_string:
        splitter = ':'
    else:
        return (time_string)
    (mins, secs) = time_string.split(splitter)
    return (mins + '.' + secs)


class AthleteList(list):
    def __init__(self,a_name,a_dob=None,a_times=[]):
        list.__init__([])
        self.name = a_name
        self.dob = a_dob
        self.extend(a_times)

    def top3(self):
        return (sorted(set([sanitize(t) for t in self]))[0:3])

def get_data(filename):
    try:
        with open(filename) as asd:
            data = asd.readline()
        templ = (data.strip().split(','))
        return (AthleteList(templ.pop(0), templ.pop(0), templ))
    except IOError as ioerr:
        print('file error: ' + str(ioerr))
        return (None)

james = get_data('/Users/shihao/Desktop/james2.txt')
juile = get_data('/Users/shihao/Desktop/julie2.txt')
mikey = get_data('/Users/shihao/Desktop/mikey2.txt')
sarah = get_data('/Users/shihao/Desktop/sarah2.txt')

print(james.name + "'s fastest times are: " + str(james.top3()))
print(juile.name + "'s fastest times are: " + str(juile.top3()))
print(mikey.name + "'s fastest times are: " + str(mikey.top3()))
print(sarah.name + "'s fastest times are: " + str(sarah.top3()))





class FMG:
    def write(msg):
        file = open('../tmp.txt', 'w')
        file.write(msg)

    def read():
        file = open('../tmp.txt', 'w')
        msg = file.readline()
        return msg

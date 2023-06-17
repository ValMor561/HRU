class HRU:

    def __init__(self):
        self.O = set()
        self.S = set()
        self.M = dict(dict())

    def create_object(self,object_name):
        if object_name not in self.O:
            self.O.add(object_name)
        else:
            print("This object is already exist")
            return 0
        for s in self.S:
            self.M[s][object_name] = set()
    
    def create_subject(self,subject_name):
        if subject_name not in self.S:
            self.S.add(subject_name)
            self.O.add(subject_name)
        else:
            print("This subject is already exist")
            return 0
        self.M[subject_name] = {}
        for o in self.O:
            self.M[subject_name][o] = set()

        for s in self.S:
            self.M[s][subject_name] = set()

    def add_right(self,right,subject,object):
        if right not in "rwx":
            print("wrong right")
            return 0
        elif right in self.M[subject][object]:
            print('This right is already exist')
            return 0
        else:
            self.M[subject][object].add(right)

    def delete_right(self,right,subject,object):
        if right not in self.M[subject][object]:
            print('This right does not exist')
            return 0
        else:
            self.M[subject][object].remove(right)

    def delete_subject(self,subject_name):
        self.S.remove(subject_name)
        self.O.remove(subject_name)
        del self.M[subject_name]

    def delete_object(self,object_name):
        self.O.remove(object_name)
        for s in self.S:
            del self.M[s][object_name]

    def can_read(self,subject,object):
        if "r" in self.M[subject][object]:
            return True
        else:
            return False

    def can_write(self,subject,object):
        if "w" in self.M[subject][object]:
            return True
        else:
            return False

    def can_execute(self,subject,object):
        if "e" in self.M[subject][object]:
            return True
        else:
            return False      


if __name__ == "__main__":
    hru = HRU()
    hru.create_subject("s1")
    hru.create_subject("s2")
    hru.create_object("o1")
    hru.create_object("o2")
    hru.add_right("r","s1","o1")
    hru.add_right("w","s1","o1")
    hru.add_right("w","s2","o1")
    print(hru.M)
    hru.delete_right("w","s1","o1")
    print(hru.M)
    hru.delete_subject("s2")
    print(hru.M)
    hru.delete_object("o2")
    print(hru.M)
    print(hru.can_read("s1","o1"))
    print(hru.can_write("s1","o1"))
    print(hru.can_execute("s1","o1"))
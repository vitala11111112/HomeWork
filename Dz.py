from random import*
class DZ():
    def strings(self,strings:list[str], nums:list[int])->list:
        origin = []
        for i in nums:
            origin.append(strings[i])
        return origin
    def strings2(self,list:list[int])->list:
        counter = 0
        even = []
        for i in range(len(list)):
            if list[i] % 2 == 0:
                even.append(list[i])
        shuffle(even)
        for i in range(len(list)):
            if list[i] % 2 == 0:
                list[i] = even[0]
                even.pop(0)
                    
        return list
if __name__ == "__main__":
    obj = DZ()
    print(obj.strings(["Mary", "Gary", "Harry"],[1, 2, 0]))
    print(obj.strings2( [10, 1, 4, 3, 8, 5]))
        
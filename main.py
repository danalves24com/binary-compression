class bitFlipEncode:
    def __init__(self, file):
        o = open(file, "r")
        o = o.read()
        #o = ' '.join(format(ord(x), 'b') for x in o)
        self.fileData = o.split(" ") 
        self.joined = "".join(self.fileData)  
        self.length = len(self.joined)   
    def analyze(self):
        self.incrementalIndexes = []
        for bitIndex in range(len(self.joined)):
            bit = self.joined[bitIndex]            
            if bit == "1":
                if len(self.incrementalIndexes) == 0:
                    self.incrementalIndexes.append(self.bitCheck(bitIndex))
                    #print(self.bitCheck(bitIndex))
                else:
                    self.incrementalIndexes.append(self.bitCheck(bitIndex - self.prevIndex))
                    #print(self.bitCheck(bitIndex - self.prevIndex))
            else:
                continue
            self.prevIndex = bitIndex

    def write(self):
        self.encodedMessage = "".join(self.incrementalIndexes)
        #print(self.incrementalIndexes)

    def bitCheck(self, bit):
        bit = str(bit)
        if len(bit) == 1:
            return bit
        elif len(bit) == 2:
            return "!"+bit
        elif len(bit) == 3:
            return "@"+bit
        elif len(bit) == 4:
            return "#"+bit
        else:
            return bit
        
class bitFlipDecode():
    def __init__(self, data):
        self.dataOutput = []
        index = 0
        for char in data:
            #print(char)
            if len(char) >= 1:
                char = char[0]
            index+=1
            if len(self.dataOutput) < 1:
                self.dataOutput.append(0+int(char))
            else:
                if char == "!":
                    char = f"{data[index+1]}{data[index+2]}"
                elif char == "@":
                    char = f"{data[index+1]}{data[index+2]}{data[index+3]}"                
                elif char == "#":
                    char = f"{data[index+1]}{data[index+2]}{data[index+3]}{data[index+4]}" 
                else:
                    char = char

                char = self.lastIndex+int(char)            
                self.dataOutput.append(char)
            
            self.lastIndex = int(char)
    def compile(self, length):
        canvas = []
        for b in range(length):
            canvas.append(int(0))
        for index in self.dataOutput:
            #print(index)    
            canvas[index] = 1

        self.compiled = canvas        
        indexF = 0
        res = []
        for bit in self.compiled:
            indexF+=1
            if indexF == 8:
                res.append(f"{bit} ")
                indexF = 0
            else:
                res.append(f"{bit}")
        self.compiled = "".join(res)







proc = bitFlipEncode("data")
proc.analyze()
proc.write()




enc = bitFlipDecode(proc.encodedMessage)
#print(proc.incrementalIndexes)
comp = open("compressed_data", "w")
comp.write(proc.encodedMessage)
comp.close()
#print(len(s))
#print(enc.dataOutput)
enc.compile(proc.length)
#print(enc.compiled)
f = open("processed output", "w")
f.write(enc.compiled)
f.close()
#print(len(proc.joined))
#print(proc.incrementalIndexes)

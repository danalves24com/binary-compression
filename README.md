# binary-compression
This compression works on the basis of analyzing all 1's and marking their location relative to the previous, by doing this I have achieved of an average lossless compression of 60%.
## Core Algorithms 
# 1
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
# 2
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
# 3
    def compile(self, length):
        canvas = []
        for b in range(length):
            canvas.append(int(0))
        for index in self.dataOutput:
            #print(index)    
            canvas[index] = 1

        self.compiled = canvas 

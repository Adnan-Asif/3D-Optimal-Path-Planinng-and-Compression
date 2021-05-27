class Point:

    def __init__(self, x: float = None, y: float = None, z: float =  None ) -> None:
        self.x = x
        self.y = y
        self.z = z


class Octree:

    max_depth = 10 

    def __init__(self, UpperX: float = None, UpperY: float = None, UpperZ: float = None, 
                LowerX: float = None, LowerY: float = None, LowerZ: float = None, lvl : int = -1) -> None:
        
        if (UpperX == None and UpperY == None and UpperZ == None and LowerX == None and LowerY == None and LowerZ == None):
            self.type = 'empty'
        elif (LowerX == None and LowerY == None and LowerZ == None):
            self.type = 'point'
            self.value = Point(UpperX, UpperY, UpperZ)
        else:
            self.type = 'region'
            self.value = None 

            self.LowerBound = Point(UpperX, UpperY, UpperZ)
            self.UpperBound = Point(LowerX, LowerY, LowerZ)

            #self.IsLeaf = True
            self.lvl = lvl+1 

            self.children = {
                'TopLeftFront' : None,
                'TopRightFront' : None, 
                'BottomRightFront' : None, 
                'BottomLeftFront' : None, 
                'TopLeftBack' : None, 
                'TopRightBack' : None, 
                'BottomRightBack' : None, 
                'BottomLeftBack' : None 
            }

            
            self.Center = Point((self.UpperBound.x + self.LowerBound.x)/2 , (self.UpperBound.y + self.LowerBound.y)/2, (self.UpperBound.z + self.LowerBound.z)/2  )

    def Add(self, point: Point) -> None:
        '''
            recursive function to add new point in the octree
        '''

        # print("Lower Bound ", self.LowerBound.x , self.LowerBound.y, self.LowerBound.z)
        # print("Upper Bound ", self.UpperBound.x , self.UpperBound.y, self.UpperBound.z)
        # print ("Point: ", point.x, point.y, point.z)
        # print("children: ",self.children)
        # print("level: ", self.lvl)
        # print("val: ", self.value)
        
       

        if ((point.x < self.LowerBound.x) or (point.x > self.UpperBound.x)
            or (point.y < self.LowerBound.y) or (point.y > self.UpperBound.y)
            or (point.z < self.LowerBound.z) or (point.z > self.UpperBound.z)):
            # print ("Here")
            # print(self.lvl)
            # print("Lower Bound ", self.LowerBound.x , self.LowerBound.y, self.LowerBound.z)
            # print("Upper Bound ", self.UpperBound.x , self.UpperBound.y, self.UpperBound.z)
            # print("children: ",self.children)
            return 

        position = None 

        if self.Center.x >= point.x:
            if self.Center.y >= point.y:
                if self.Center.z >= point.z:
                    position = 'TopLeftFront'
                else:
                    position = 'TopLeftBack'
            else:
                if self.Center.z >= point.z:
                    position = 'BottomLeftFront'
                else:
                    position = 'BottomLeftBack'
        else:
            if self.Center.y >= point.y:
                if self.Center.z >= point.z:
                    position = 'TopRightFront'
                else:
                    position = 'TopRightBack'
            else:
                if self.Center.z >= point.z:
                    position = 'BottomRightFront'
                else:
                    position = 'BottomRightBack'

        if (self.type == 'region' and self.children[position] != None and self.children[position].type == 'region'):
            #Region Node hai toh bs aage bhejdo
            self.children[position].Add(point)
            return

        elif (self.children[position] == None):
            #Empty Node hai yaha toh filhaal Point Node banado 
            self.children[position] = Octree(point.x , point.y, point.z)
            print('new point added')
            print('level: ',self.lvl )
            print(self.children[position].value.x,self.children[position].value.y,self.children[position].value.z)
            print(self.children)
            return 
        else:   
            if self.lvl == Octree.max_depth:
                return 
            else:   
                temp_point : Point = self.children[position].value 
                self.children[position] = None 
                self.type = 'region'
                if position == 'TopLeftFront':
                    self.children[position] = Octree(self.LowerBound.x, self.LowerBound.y, self.LowerBound.z,
                                                    self.Center.x, self.Center.y, self.Center.z, self.lvl)
                    

                elif position == 'TopLeftBack':
                    self.children[position] = Octree(self.LowerBound.x, self.LowerBound.y, self.Center.z,
                                                    self.Center.x , self.Center.y, self.UpperBound.z, self.lvl)  
                    

                elif position == 'BottomRightFront':
                    self.children[position] = Octree(self.Center.x, self.Center.y, self.LowerBound.z,
                                                    self.UpperBound.x , self.UpperBound.y, self.Center.z, self.lvl)
                    

                elif position == 'BottomLeftBack':
                    self.children[position] = Octree(self.LowerBound.x, self.Center.y, self.Center.z,
                                                    self.Center.x , self.UpperBound.y, self.UpperBound.z, self.lvl)
                    

                elif position == 'TopRightFront':
                    self.children[position] = Octree(self.Center.x, self.LowerBound.y, self.LowerBound.z,
                                                    self.UpperBound.x , self.Center.y, self.Center.z, self.lvl)
                    

                elif position == 'TopRightBack':
                    self.children[position] = Octree(self.Center.x, self.LowerBound.y, self.Center.z,
                                                    self.UpperBound.x , self.Center.y, self.UpperBound.z, self.lvl)
                    

                elif position == 'BottomRightBack':
                    self.children[position] = Octree(self.Center.x, self.Center.y, self.Center.z,
                                                    self.UpperBound.x , self.UpperBound.y, self.UpperBound.z, self.lvl)
                    

                elif position == 'BottomLeftFront':
                    self.children[position] = Octree(self.LowerBound.x, self.Center.y, self.LowerBound.z,
                                                    self.Center.x , self.UpperBound.y, self.Center.z, self.lvl)
                
                self.children[position].Add(temp_point)
                self.children[position].Add(point)




    def level_points(self, level:int, lst):
        '''
            returns a list of all the point nodes present in the tree up to the given level proivded in argumnet.
        '''
        
        if self.lvl <= level:
            if self.type == 'region':
                for key in self.children.keys():
                    try:
                        if self.children[key].type == 'point':
                            lst.append((self.children[key].value.x,self.children[key].value.y,self.children[key].value.z))
                        elif self.children[key].type == 'region':
                            self.children[key].level_points(level, lst)
                    except:
                        pass
        return lst 

    def getOctreeRegions(self, level: int, lst ):
        '''
            returns a list of all the region nodes present in the tree up to the given level proivded in argumnet.
        '''
        if self.lvl <= level:
            if self.type == 'region':
                lst.append(((self.LowerBound.x, self.LowerBound.y, self.LowerBound.z), (self.UpperBound.x, self.UpperBound.y, self.UpperBound.z)))
                for key in self.children.keys():
                    try:
                        if self.children[key].type == 'region':
                            self.children[key].getOctreeRegions(level, lst)
                    except:
                        pass 
        return lst 
    
    def getEmptyRegions(self, level: int = max_depth , lst = []):
        '''
            returns a list of all the empty nodes present in the tree up to the given level proivded in argumnet.
        '''
        if self.lvl <= level:
            for key in self.children.keys():
                if self.children[key] == None:
                    if key == 'TopLeftFront':
                        lst.append(((self.LowerBound.x, self.LowerBound.y, self.LowerBound.z),
                                    (self.Center.x, self.Center.y, self.Center.z)))

                    elif key == 'TopLeftBack':
                        lst.append(((self.LowerBound.x, self.LowerBound.y, self.Center.z),
                                    (self.Center.x , self.Center.y, self.UpperBound.z)))

                    elif key == 'BottomRightFront':
                        lst.append(((self.Center.x, self.Center.y, self.LowerBound.z), 
                                    (self.UpperBound.x , self.UpperBound.y, self.Center.z)))

                    elif key == 'BottomLeftBack':
                        lst.append(((self.LowerBound.x, self.Center.y, self.Center.z), 
                                    (self.Center.x , self.UpperBound.y, self.UpperBound.z)))

                    elif key == 'TopRightFront':
                        lst.append(((self.Center.x, self.LowerBound.y, self.LowerBound.z), 
                                    (self.UpperBound.x , self.Center.y, self.Center.z)))

                    elif key == 'TopRightBack':
                        lst.append(((self.Center.x, self.LowerBound.y, self.Center.z), 
                                    (self.UpperBound.x , self.Center.y, self.UpperBound.z)))

                    elif key == 'BottomRightBack':
                        lst.append(((self.Center.x, self.Center.y, self.Center.z), 
                                    (self.UpperBound.x , self.UpperBound.y, self.UpperBound.z)))

                    elif key == 'BottomLeftFront':
                        lst.append(((self.LowerBound.x, self.Center.y, self.LowerBound.z), 
                                    (self.Center.x , self.UpperBound.y, self.Center.z)))
                elif self.children[key].type == 'region':
                    self.children[key].getEmptyRegions(level, lst)

        return lst
         


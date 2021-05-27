#import bpy

def get_edges(length):
    edges = []
    for i in range(0,length-1):
        edges.append((i,i+1))
    return edges 

def get_Vertices_Faces(regions):
    region_vertices = []
    region_faces = []
    #region_edges = []
    
    ind = 0
            
    for region in regions:
        p1 = region[0]
        p8 = region[1]
        p2 = (p8[0],p1[1],p1[2])
        p3 = (p1[0],p8[1],p1[2])
        p4 = (p1[0],p1[1],p8[2])
        p5 = (p8[0],p8[1],p1[2])
        p6 = (p8[0],p1[1],p8[2])
        p7 = (p1[0],p8[1],p8[2])
                

        region_vertices.append(p1)
        region_vertices.append(p2)
        region_vertices.append(p3)
        region_vertices.append(p4)
        region_vertices.append(p5)
        region_vertices.append(p6)
        region_vertices.append(p7)
        region_vertices.append(p8)
                
                
        region_faces.append((ind, ind+1, ind+4, ind+2))
        region_faces.append((ind+1, ind+5, ind+7, ind+4))
        region_faces.append((ind, ind+3, ind+6, ind+2))
        region_faces.append((ind+5, ind+3, ind+6, ind+7))
        region_faces.append((ind+2, ind+4, ind+7, ind+6))
        region_faces.append((ind, ind+1, ind+5, ind+3))
                
        '''
        region_edges.append((ind, ind+1))
        region_edges.append((ind, ind+2))
        region_edges.append((ind, ind+3))
        region_edges.append((ind+1, ind+4))
        region_edges.append((ind+1, ind+5))
        region_edges.append((ind+2, ind+4))
        region_edges.append((ind+2, ind+7))
        region_edges.append((ind+3, ind+5))
        region_edges.append((ind+3, ind+6))
        region_edges.append((ind+4, ind+7))
        region_edges.append((ind+5, ind+7))
        region_edges.append((ind+6, ind+7))
                
        print(region_edges)
        '''

        ind += 8
    
    return (region_vertices,region_faces)

def display(vertices, edges = None, faces = None) -> None:
    mymesh = bpy.data.meshes.new("obj")
    myobj = bpy.data.objects.new("obj", mymesh)
    myobj.location = bpy.context.scene.cursor.location
    bpy.context.collection.objects.link(myobj)
   
    if (faces and edges):
        mymesh.from_pydata(vertices, edges, faces)
    elif faces:
        mymesh.from_pydata(vertices, [], faces)
    elif edges:
        mymesh.from_pydata(vertices, edges, [])
    else:
        mymesh.from_pydata(vertices, [], [])

    mymesh.update(calc_edges=True)
    values = [True] * len(mymesh.polygons)
    mymesh.polygons.foreach_set("use_smooth", values)

class obj:
    
    def __init__(self, path: str) -> None :
        self.vertices = []
        #self.faces = []
        
        source = open(path).readlines()

        for line in source:
            if line[0:2] == "v ":
                vertex = line.split()
                #print(vertex)
                self.vertices.append((float(vertex[1]), float(vertex[2]), float(vertex[3])))
            '''
            elif line[0:] == "f ":
                face = line.split()
                face_temp = []
                
                for ind in face[1:]:
                    face_temp.append(int(ind.split("/")[0]))
                
                self.faces.append(tuple(face_temp))
            '''

    
    def get_vertices(self):
        return self.vertices
    
    
    def store(self, tree: Octree) -> None :
        for vertex in self.vertices:
            tree.Add(Point(vertex[0], vertex[1], vertex[2]))
        
   
        
'''
oct = Octree(-10, -10, -10, 10, 10, 10)    
t1 = obj("C:\\Users\\batoo\\Documents\\HU\\DS2\\map_1.obj")
t1.store(oct)                        

EmptyRegions =  oct.getEmptyRegions(5,[]) #loading empty regions
Graph = createGraph(EmptyRegions) #creating graph of empty regions
#now defining starting and goal points in the form (x,y,z)

Starting = (10, -25, -50)
Goal = (80, 40, 50) 

x = getClosestEmptyRegion(Graph, Starting)
y = getClosestEmptyRegion (Graph, Goal) 

path = list()
path = FindShortestPath(Graph, x, y)

path2 = [((region[0][0] + region[1][0])/2 , (region[0][1] + region[1][1])/2, (region[0][2] + region[1][2])/2) for region in path]
path2.insert(0, Starting)
path2.append(Goal)

path_edges = get_edges(len(path2))

display(path2, path_edges)
path_vertices, path_faces = get_Vertices_Faces(path)
display(path_vertices, None, path_edges)
'''

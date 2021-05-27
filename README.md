# 3D-Optimal-Path-Planinng-and-Compression
Final Project repository of _team_ Data-Condtionals for the course CS-201
# [Final presentation of the Project](https://youtu.be/rSp-nERTqtY)

# Octree 
An octree is the natural generalization of a quadtree. An initial bounding cube is split into eight congruent cubes, each of which is split recursively until each minimal cube intersects the domain Ω in a simple wway (1). The structure is mostly used for 3D data compression, mesh generation, frustum culling, collision detection, path navigation in robotics, spatial indexing and other feilds where 3-dimensional data handling is significant. 

# Our Work
We aimed to execute 3D data compression using Octree Data Struture and implement 3D optimal path planning. 


# 3D Data Compression through Octrees
The increasing amount of geometric information acquired with 3D scanners gives rise to an equally growing demand for data representations that allow for efficient and compact storage as well as transfer of this data(2). Octrees allow significant compression of 3D data through repeated divisions of the space into 8 octants, untill the region optained has uniform/similar characteristics. So the nodes/leaf correspond to those blocks of the array for which no further subdivision is necessary. We came up with a program that takes in image mesh and stores it into Octrees and gives compressed data as the outcome. The image we used had 76000+ vertices, after compression the number dropped down to 46000 vertices. 

<img src="https://github.com/Adnan-Asif/3D-Optimal-Path-Planinng-and-Compression/blob/main/imgs/orignal.jpeg" alt="alt text" width="400" >
<img src="https://github.com/Adnan-Asif/3D-Optimal-Path-Planinng-and-Compression/blob/main/imgs/Octree_visualization.jpeg" alt="alt text" width="400" >
<img src="https://github.com/Adnan-Asif/3D-Optimal-Path-Planinng-and-Compression/blob/main/imgs/compressed.jpeg" alt="alt text" width="400" >

# 3D Optimal Path planning 
Path planning is a computational problem to find a sequence of valid configurations that moves the object from the source to destination. In our approach, we use octrees to represent every object in the environment and calculate the empty regions. We then use a complex version of Dijkstra Algorithm for the point to navigate through the nodes which contain empty regions. The program takes in the distance to every region and takes the shortest path for navigation. 
![Here, empty region image](image name)
![Here, path image](image name)

# Advantages/Significance of Our approach 
- Our approach results in better _memory management_ becuase of the compression of the 3D image through the octree structure.
- Leads to _fast access of data_ as the data is stored as regions instead of points so the nodes of the tree are reduced and since it is a tree so the time complexity in logarithimic and the tree here has 8 nodes so the time complexity is log base 8.
- enables us to _render a specific region_ instead of the entire octree e.g if we use octree for the area map in a 3D game, we can render a specific path within reach of the player instead of the entire area itself.
- It saves time and computing energy as through Octrees we get regions which are mostly a big group of points so going from one empty region to another  instead of traversing through points.
-  Our approach can be cost efficient for 3D data planning for navigating machines such as drones etc, as as the path planning for the machines would be easier when it has to navigate from one empty region to another as instead of calculating if every next point it moves to is empty or not, it just has to see if there is an empty region and can go through it without an hurdle in the way.  This reduces our need for complex mechanisms and huge computing power which basically saves us from using expensive hardware. 



# References 
1) Marshall Bern, Paul Plassmann, in Handbook of Computational Geometry, 2000
2) Ruwen Schnabel and Reinhard Klein, Octree-based Point-Cloud Compression, Institut für Informatik II, Universität Bonn, Germany.

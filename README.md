# **Algorithmic Art**
Art that is generated using principles of math, 
and tools from computer science. This art is 
often time-evolving and dynamic, or may be a 
static image which is the result of an algorithmic 
design. 

# Nature

## Evolution
Fractal Bacterial growth. 
[fractal_bacteria](https://www.youtube.com/watch?v=pnDPwoULIfM&feature=youtu.be)

Some water like annealing
[anneal](https://youtu.be/N-ijMS1R2_4)

## Fractal Fire
Generate fractal patterns with cellular automata that evolve from initial states 
like a solid square or a rectange(```python fractal_fire.py -coal ```). The location of this solid will greatly shape
the pattern created. 

For Example take the ``python fractal_fire.py -log`` command's output. Initially it
builds this state:    [fractal_firelog_youtube](https://youtu.be/fo_jFVEpBcQ)
![fire_place](https://raw.githubusercontent.com/TylersDurden/AlgorithmicArt/master/Nature/images/fireplace.png)
Which will eventually turn into:
![blazing](https://raw.githubusercontent.com/TylersDurden/AlgorithmicArt/master/Nature/images/pattern.png)

You can also run ```python fractal_fire.py -coal```, which seeds the same algorithm instead
with an initial state that has a solid block in the middle of some empty space. Here's a video
of it in action on youtube: 
[fractal_coal_youtube](https://youtu.be/t-aBd_ns2vs)

## Gravity 
Accumulate celestial bodies in space over time with diffusion limited aggregation. 
![galactic](https://raw.githubusercontent.com/TylersDurden/AlgorithmicArt/master/Nature/images/gen_galactic.png)

## Waves
This simulates hundreds of autonomous fireflies flying around. 

# Cellular

## Mazing 
Starting from an initially random state, the program attempts to build a maze like structure. 
Running ```python mazing.py``` will run through a series of increasingly sparser initially states
of randomly distributed points. 

![Example_Maze](https://raw.githubusercontent.com/TylersDurden/AlgorithmicArt/master/cellular/images/maze.png)

Eventually the sparsity becomes so great the crawling maze kernel can't actually reach the entirety of
the seed state. These are probably the more fascinating simulations to observe. 

![sparse_maze](https://raw.githubusercontent.com/TylersDurden/AlgorithmicArt/master/cellular/images/sparser_maze.png)

Even more frenzied are the initial seeds that are **mostly empty**. This ensures that no mazes can really be built,
so instead pockets of somewhat orderly grid structures are built out of fragmented sections on a chaotic bit plane. 

[Animated](https://www.youtube.com/watch?v=wTvIug3fsuY)

# Classic
## Game of Life **[GOL]**
Conway's game of Life: 
[GOL](https://raw.githubusercontent.con/TylersDurden/AlgorithmicArt/master/Classic/images/GOL.mp4)
Cellular Automata Fractal Art: 
[mosaic](https://raw.githubuser.content.com/TylersDurden/AlgorithmicArt/master/Classic/images/mosaic.mp4)

# imG

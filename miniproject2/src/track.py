from pylab import *
import matplotlib.image as im
import time

class track:
    
    def __init__(self):
        
        # setup the parameters
        
        self.accel_map = self.make_accelmap() # maps the action number to the correspondent acceleration vector
        
        # limits of the track
        self.xmax = 1.0 
        self.ymax = 1.0
        self.xmin = 0.0
        self.ymin = 0.0
        
        self.max_vel = 0.3          # maximum velocity
        self.accel_factor = 0.02    # acceleration per time step
        
        self.def_t_penty = 2        # time penalty for hitting a wall. the car stays still for this number of time steps.
        self.def_r_penty = -1.0     # reward penalty for hitting a wall.
        
        self.finish_line = array([[0.8,0.1],[1.,0.25]])
        
        self.max_rew = 8.
        
        self.set_walls()            # create the walls
        
        self.pos = array([0.3,0.3]) 
        self.vel = array([0,0])
        
        self.last_pos = self.pos
        self.history = [self.pos]
        
        self.t_penty = 0
        self.total_reward = 0       # total reward
        self.time = 0               # time steps
        
        self.finished = False
        self.message = 'Start the engine!'
        
        self.car_img = im.imread('carfig.jpg')
        
        
    def setup(self, plotting=False, level=1):
        # you may choose the difficulty level (0 or 1), with or without walls.
        
        self.pos = array([0.05,0.03])
        self.vel = array([0,0])
        
        self.last_pos = self.pos
        self.history = [self.pos]
        
        self.t_penty = 0
        self.total_reward = 0
        self.time = 0
        self.finished = False
        
        self.plotting = plotting
        
        if level == 1:
            self.set_walls()
        if level == 0:
            self.walls = []
        
        if self.plotting:
            figure(100)
            clf()
            self.plot_world()
            print 'Start race!'
        
        return self.pos, self.vel/self.max_vel
        
    def set_walls(self):
        # setup walls
        
        self.walls = []
        # set end points of each wall: [[x0,y0],[x1,y1]]
        self.walls.append([[0.4,0.64],[0.4,0.8]])
        self.walls.append([[0.5,0.85],[0.5,1.0]])
        self.walls = array(self.walls)
        
        self.contours = []
        # set the x axis support, the function y=f(x) and if is below (-1) or above (1) track.
        self.contours.append([linspace(0, 1.0, 1000), lambda x:sin(x*pi), 1])
        self.contours.append([linspace(0.1, 0.9, 1000), lambda x:sin(x*pi)-0.3, -1])
        
        
    def make_accelmap(self):
        self.acmap = {0:[0.,0.],1:[0.,1.],
                2:[1/sqrt(2),1/sqrt(2)],
                3:[1,0],4:[1/sqrt(2),-1/sqrt(2)],
                5:[0.,-1.],6:[-1/sqrt(2),-1/sqrt(2)],
                7:[-1,0],8:[-1/sqrt(2),1/sqrt(2)]}
        
        return lambda x:array(self.acmap[x])*self.accel_factor
        
    def crossed(self, wall, lastpos, pos):
        # check if crossed a wall.
        
        if cross(pos-lastpos,wall[0]-lastpos)*cross(pos-lastpos,wall[1]-lastpos) < 0 and \
           cross(wall[1]-wall[0],pos-wall[0])*cross(wall[1]-wall[0],lastpos-wall[0]) < 0:
           #print 'wall crash'
           return True
        return False
        
    def wall_crash(self,pos):
        # check if crossed boundaries
        if pos[0] <= self.xmin or pos[0] >= self.xmax or \
           pos[1] <= self.ymin or pos[1] >= self.ymax:
            return True
            
        for w in self.walls:
            if self.crossed(w,self.pos,pos): #gives last position and new one
                return True
                
        for c in self.contours:
            if pos[0] >= c[0][0] and pos[0] <= c[0][-1]: # x position is in the range of this contour
                if (pos[1]-c[1](pos[0]))*c[2] >= 0:         # y position should be above (or below) it
                    return True
                
        return False
        
    def crashed(self,pos):
        if self.wall_crash(pos):
            return True
        return False
        
    def finish(self,pos):    
        # check if goal was reached.
        
        if self.crossed(self.finish_line,self.pos,pos):
            return True
        return False
        
    def plot_world(self):
        # plots the track with the history of movements
        figure(100)
        clf()
        xlim(-0.1,1.1)
        ylim(-0.1,1.1)
        
        plot([0,0],[0,1],lw=2,c='k')
        plot([0,1],[1,1],lw=2,c='k')
        plot([1,1],[1,0],lw=2,c='k')
        plot([0,1],[0,0],lw=2,c='k')
        
        for wall in self.walls:
            plot([wall[0,0],wall[1,0]],
                 [wall[0,1],wall[1,1]],lw=2,c='k')
        
        for contour in self.contours:
            plot(contour[0],contour[1](contour[0]), color='k')
        
        for i in arange(len(self.history)-1): 
            plot([self.history[i][0],self.history[i+1][0]],
                [self.history[i][1],self.history[i+1][1]],lw=1,c='r')
            
        for i in arange(len(self.history)): 
            plot([self.history[i][0]],
                [self.history[i][1]],'r.',lw=0.2)
            
        plot([self.pos[0],self.pos[0]+self.vel[0]],
            [self.pos[1],self.pos[1]+self.vel[1]],lw=2,color='y')
        
        newp = self.pos+self.vel
        
        plot([self.finish_line[0,0], self.finish_line[1,0]], 
             [self.finish_line[0,1], self.finish_line[1,1]], color='black', ls='--', lw=5)
        
        figsize = 0.15
        imshow(self.car_img[:,::-1],extent=(self.pos[0]-figsize/2,self.pos[0]+figsize/2,self.pos[1]-figsize/2,self.pos[1]+figsize/2))
        
        title(self.message)
        
        draw()
        
    def update_world(self):
        self.time = self.time + 1
        
        if self.plotting:
            self.plot_world()
            time.sleep(0.03)         # slows down the simulation for watching the race
    
    def move(self,action): 
        # this is the main method, called when an action is taken.
        # the action should be a integer between 0 and 8, indicating the direction of acceleration.
           
        # updates velocity
        self.vel = self.vel + self.accel_map(action)
        
        rew = 0
        self.message = 'Time: %d' % self.time
            
        # check if there is a time penalty
        if self.t_penty>0:
            self.vel = array([0,0])
            self.t_penty -= 1
    
        # impose the maximum velocities
        self.vel[self.vel>self.max_vel] = self.max_vel
        self.vel[self.vel<-self.max_vel] = -self.max_vel
 
        # calculate new position
        new_pos = self.pos + self.vel  
        
        if self.crashed(new_pos):
            # if crashed a wall
            
            self.t_penty = self.def_t_penty # give time penalty
            rew = self.def_r_penty          # give reward penalty
            
            new_pos = self.pos              # return to previous position
            self.vel = array([0,0])         # set velocity to zero
        
            self.message = 'Crashed!'
            #print 'crashed!'
        
        if self.finish(new_pos):
            # if the goal was reached.

            # calculate the reward given
            rew = self.max_rew 

            print 'Finish line! Time steps:', self.time
            print 'Total reward:', self.total_reward
            self.message = 'Finish!'
            self.finished = True

            if self.plotting:
                self.plot_world()
        
        self.last_pos = self.pos
        self.pos = new_pos
        self.total_reward += rew
        
        self.history.append(self.pos)
        
        self.update_world()
        
        # the [vx,vy] velocity values are returned as a value between -1 and 1, where 1 means maximum velocity.
        # the [x,y] position values are always between 0 and 1.
        return self.pos, self.vel/self.max_vel, rew
        
        
    
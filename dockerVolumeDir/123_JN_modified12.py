import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.widgets import Slider

fig = plt.figure()
_3d_fig = fig.gca(projection='3d')


# Slider
initial_xx = 0.5
initial_zz = 0.5
#               x_start, y_start, x_end, y_end
axamp_xx = plt.axes([.07, 0.25, 0.02, 0.50])
axamp_zz = plt.axes([.17, 0.25, 0.02, 0.50])
samp_xx = Slider(axamp_xx, 'xx', 0, 0.5, valinit=initial_xx, orientation='vertical', valstep=0.05)
samp_zz = Slider(axamp_zz, 'zz', 0, 0.5, valinit=initial_zz, orientation='vertical', valstep=0.05)

#INITIALIZATION START
#==============================================================================================================
def plot_cube(_3d_fig):
    # plot the primitive cube's wire-frame. 
    #-------------------------------------------------------------------------------
    #     #0  , #1  , #2  , #3  , #4  , #5  ,  #6  , #7  , #8  , #9  , #10 , #11  
    x = [[0,1],[0,0],[0,0],[1,0],[1,1],[1,1], [1,0],[1,1],[1,1],[0,1],[0,0],[0,0]]
    y = [[0,0],[0,1],[0,0],[1,1],[1,0],[1,1], [0,0],[0,1],[0,0],[1,1],[1,0],[1,1]]
    z = [[0,0],[0,0],[0,1],[0,0],[0,0],[0,1], [1,1],[1,1],[1,0],[1,1],[1,1],[1,0]]
    for i in range(12):
        _3d_fig.plot(x[i], y[i], z[i], color="blue")
    #-------------------------------------------------------------------------------

#####################################################################################
plot_cube(_3d_fig)

# plot the mirror planes 
#==========================================================
# 3D plane formulation: aX + bY + cZ + d = 0
#       a, b, c, d
vp1 = [[-1], [ 0], [ 1], [ 0]]
vp2 = [[-1], [ 1], [ 0], [ 0]]
vp3 = [[ 0], [-1], [ 1], [ 0]]

vp4 = [[ 2], [ 0], [ 0], [-1]]
vp5 = [[ 0], [ 2], [ 0], [-1]]
vp6 = [[ 0], [ 0], [ 2], [-1]]
vp7 = [[ 2], [ 0], [ 0], [ 1]]

mirror_plane_list = [
     tuple(vp1),
     tuple(vp2),
     tuple(vp3),
     tuple(vp4),
     tuple(vp5),
     tuple(vp6),
     tuple(vp7)
]
print(mirror_plane_list)

def drawPlanes_tilt( xmi, ymi, zmi ):
    for i in range(len(xmi)):
        xvp, yvp, zvp = xmi[i], ymi[i], zmi[i]
        if zvp != 0:
            xv,yv = np.meshgrid(range(2), range(2))
            zv = (  -(xvp)*xv -(yvp)*yv )/(zvp)
        else:
            zv,xv = np.meshgrid(range(2), range(2))
            yv = ( -(xvp)*xv )/(yvp)
        _3d_fig.plot_surface(xv, yv, zv, alpha=0.5)

def drawPlanes_half( xmi, ymi, zmi ):
    for i in range(len(xmi)):
        xvp, yvp, zvp = xmi[i], ymi[i], zmi[i]
        if xvp == 2:
            yv,zv = np.meshgrid(range(2), range(2))
            xv = 0.5
        elif yvp == 2:
            xv,zv = np.meshgrid(range(2), range(2))
            yv = 0.5
        elif zvp == 2:
            xv,yv = np.meshgrid(range(2), range(2))
            zv = 0.5 + (xvp)*xv 
        _3d_fig.plot_surface(xv, yv, zv, alpha=0.5)

def plot_mirror_planes(mode):
    # plot the mirror planes 
    drawPlanes_tilt(
        vp1[0] + vp2[0] + vp3[0],
        vp1[1] + vp2[1] + vp3[1],
        vp1[2] + vp2[2] + vp3[2]
        )
    if mode:
        drawPlanes_half(
            vp4[0] + vp5[0] + vp6[0],
            vp4[1] + vp5[1] + vp6[1],
            vp4[2] + vp5[2] + vp6[2]
            )
    # plot the mirror planes 
    plot_mirror_planes(False)

def plot_red_lineSegment_structure(xx, zz):
    # plot the red line-segment structure -START-
    #================================================================================
    #================================================================================
    # update curve
    #==== START TO PREPARE FOR THE FIRST LINE SEGMENT =============================
    a_xyz =(0,    0,  0) 
    b_xyz =(xx, 0.5, zz) 

    point_set = {a_xyz, b_xyz}

    def distance_between_2_points(p1, p2):
        return abs(((p1[0]-p2[0])**2+(p1[1]-p2[1])**2+(p1[2]-p2[2])**2)**(1/2))

    distance_ab = distance_between_2_points(a_xyz, b_xyz)
    print("distance_ab=", distance_ab)
    #==== PREPARATION DONE ! ======================================================

    # Function to mirror image 
    def mirror_point(a, b, c, d, x1, y1, z1):
        t = (-a * x1-b * y1-c * z1-d)/float((a * a + b * b + c * c))
        x2 = a * t + x1
        y2 = b * t + y1
        z2 = c * t + z1
        x3 = 2 * x2-x1
        y3 = 2 * y2-y1
        z3 = 2 * z2-z1
        return [x3, y3, z3]

    mirror_plane_list = [
         tuple(vp1),
         tuple(vp2),
         tuple(vp3),
         tuple(vp4),
         tuple(vp5),
         tuple(vp6),
         #tuple(vp7)
    ]

    #============ MIRROR START ===========================================#
    for i in range(len(mirror_plane_list)):
        a = mirror_plane_list[i][0][0]
        b = mirror_plane_list[i][1][0]
        c = mirror_plane_list[i][2][0]
        d = mirror_plane_list[i][3][0]
        old_point_set_list = list(point_set)
        new_mirrored_point_set_list = []
        for i in range(len(point_set)):
            new_mirrored_point_set_list.append(
                mirror_point(
                    a, b, c,
                    d,
                    old_point_set_list[i][0],
                    old_point_set_list[i][1],
                    old_point_set_list[i][2]
                )
            )
        # add newlly mirrored points to the set
        #print("new_mirrored_point_set_list=", new_mirrored_point_set_list)
        for i in range(len(new_mirrored_point_set_list)):
            point_set.add( tuple(new_mirrored_point_set_list[i]) )
    #============ MIRROR END =============================================#

    #===============================================
    point_set_list = list(point_set)
    for i in range(len(point_set_list)):
        point_coo_list = list(point_set_list[i])
        for j in range(3):
            if point_coo_list[j] < 0.0:
                point_coo_list[j] = 0.0
        point_set_list[i] = tuple(point_coo_list)

    point_set = {a_xyz, b_xyz}
    for i in range(len(point_set_list)):
        point_set.add( tuple(point_set_list[i]) )
    #===============================================

    #================ Review All Possible Line-connections Between Any Point-pairs Start ================
    # after the mirror operations, now we may have all possible points created by this mirror operation.
    print("point_set=", point_set)

    import itertools
    possible_line_connections = list(itertools.combinations( range(len(point_set)), 2))
    #print("possible_line_connections       =", possible_line_connections)

    point_set_list = list(point_set)
    print("point_set_list=")
    for i in range(len(point_set_list)):
        print(point_set_list[i])

    possible_line_connections_keeped = []
    for i in range(len(possible_line_connections)):
        point_1 = point_set_list[ possible_line_connections[i][0] ]
        point_2 = point_set_list[ possible_line_connections[i][1] ]
        distance_between_1_and_2 = distance_between_2_points( point_1, point_2 )
        if ( float(abs( distance_between_1_and_2 - distance_ab )) < 0.001 ):
            possible_line_connections_keeped.append(possible_line_connections[i])
    print("possible_line_connections_keeped=", possible_line_connections_keeped)

    x, y, z = [], [], []
    for i in range(len(possible_line_connections_keeped)):
        point_a_xyz = list(point_set_list[possible_line_connections_keeped[i][0]])
        point_b_xyz = list(point_set_list[possible_line_connections_keeped[i][1]])

        x = x + [[point_a_xyz[0], point_b_xyz[0]]]
        y = y + [[point_a_xyz[1], point_b_xyz[1]]]
        z = z + [[point_a_xyz[2], point_b_xyz[2]]]

    #================ Review All Possible Line-connections Between Any Point-pairs End ==================

    for i in range(len(x)):
        _3d_fig.plot(x[i], y[i], z[i], color="red")

    # plot the red line-segment structure -END-
    #================================================================================
    #================================================================================


plot_red_lineSegment_structure(initial_xx, initial_zz)

#INITIALIZATION END
#==============================================================================================================


    #==========================================================
def update(val):
    _3d_fig.clear()
    plot_cube(_3d_fig)
    # plot the mirror planes 
    #plot_mirror_planes(False)

    # xx is the current value of the slider
    xx = samp_xx.val # paper's x
    zz = samp_zz.val # paper's y

    plot_red_lineSegment_structure(xx, zz)
            
    # redraw canvas while idle
    fig.canvas.draw_idle()
    #==========================================================


samp_xx.on_changed(update)
samp_zz.on_changed(update)
plt.show()




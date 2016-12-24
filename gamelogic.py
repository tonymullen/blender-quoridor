# This script must be assigned to a python controller
# where it can access the object that owns it and the sensors/actuators that it connects to.

from bge import logic as GL
import socket


# support for Vector(), Matrix() types and advanced functions like Matrix.Scale(...) and Matrix.Rotation(...)
# import mathutils

# for functions like getWindowWidth(), getWindowHeight()
# import Rasterizer


player = 2
players = ["RedPlayer", "GreenPlayer","YellowPlayer","BluePlayer"]


def move(direction, objectName):
    result = getattr(GL.players[objectName], direction)()
    print(result)

def main():
    scene = GL.getCurrentScene()
    for obj in scene.objects:
        if ('makeWall' in obj.getPropertyNames()):
            obj.setVisible(0)
    
    global player 
    the_player_name = players[player]
    the_actuators = {}
    cont = GL.getCurrentController()
    mouse = cont.sensors["mouse"]
    own = cont.owner
    
    #own_pos = own.worldPosition

    input = False
    
    for actu in cont.actuators:
        if (actu.owner.name == the_player_name):
            the_actuators[actu.name] = actu
            own_actu = actu.owner

    
    forward = cont.sensors['forward']
    back    = cont.sensors['back']
    right   = cont.sensors['right']
    left    = cont.sensors['left']
    if forward.positive:
        the_actuators['move'].dLoc = [0, 1, 0]
        cont.activate(the_actuators['move'])
        move('forward', the_player_name)
    else:
        cont.deactivate(the_actuators['move'])
    if back.positive:
        the_actuators['move'].dLoc = [0, -1, 0]
        cont.activate(the_actuators['move'])
        move('back', the_player_name)
    else:
        cont.deactivate(the_actuators['move'])
    if right.positive:
        the_actuators['move'].dLoc = [1, 0, 0]
        cont.activate(the_actuators['move'])
        move('right', the_player_name)
    else:
        cont.deactivate(the_actuators['move'])
    if left.positive:
        the_actuators['move'].dLoc = [-1, 0, 0]
        cont.activate(the_actuators['move'])
        move('left', the_player_name)
    else:
        cont.deactivate(the_actuators['move'])
        
    if mouse.positive:
        hit_object = mouse.hitObject
        print(mouse.hitPosition)
        print(GL.board)
        hit_object.setVisible(1)
        
            
    #   hit_object.setVisible(0)
        
    # actu_motion = cont.actuators["motion"]

    # Loop through all other objects in the scene
    #sce = GL.getCurrentScene()
    #print("Scene Objects:", sce.name)
    #for ob in sce.objects:
    #    print("   ", ob.name, ob.worldPosition)

    # Example where collision objects are checked for their properties
    # adding to our objects "life" property
    """
    actu_collide = cont.sensors["collision_sens"]
    for ob in actu_collide.objectHitList:
        # Check to see the object has this property
        if "life" in ob:
            own["life"] += ob["life"]
            ob["life"] = 0
    print(own["life"])
    """

main()


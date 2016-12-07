import argparse

parser = argparse.ArgumentParser(description='Playstation VR control utility')
parser.add_argument('--on', help='Turn on PS VR, defaults to 3D mode, no tracking', action='store_true')
parser.add_argument('--threed', help='Set 3D mode', action='store_true')
parser.add_argument('--cinematic', help='Set cinematic mode', action='store_true')
parser.add_argument('--off', help='Turn off PS VR', action='store_true')

args = parser.parse_args()

if args.on:
    print "Turning PS VR on"
    mode = "3D" # default mode
    
    if args.threed and args.cinematic:
        print "Please select only one mode, defaulting to 3D mode"
        mode = "3D"
    else:
        if args.threed:
            print "...into 3D mode"
            mode = "3D"
    
        if args.cinematic:
            print "...into cinematic mode"
            mode = "cinematic"

    print mode
else:
    if args.off:
        if args.threed or args.cinematic or args.tracking:
            print "Off command does not take any arguments... Ignoring"

        print "Turning PS VR off"        
    else:
        print "No command specified. --on or --off commands is required"

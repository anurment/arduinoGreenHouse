
import adsk.core, adsk.fusion, traceback, math

def run(context):
    ui = None
    try:
        app = adsk.core.Application.get()
        ui = app.userInterface

        doc = app.documents.add(adsk.core.DocumentTypes.FusionDesignDocumentType)

        design = app.activeProduct

        # Get the root component of the active design.
        rootComp = design.rootComponent

        # Create a new sketch on the xy plane.
        sketches = rootComp.sketches
        xyPlane = rootComp.xYConstructionPlane
        sketch = sketches.add(xyPlane)

        patternRadius = 110/2
        numLoops = 5
        minionRadius = 115/24
        baseCircNum = 6 # number of circles on each loop: 1. x. 2x, 3x
        index = 0
        circles = sketch.sketchCurves.sketchCircles
        for pos in range(0, int(patternRadius), int(patternRadius/(numLoops - 1))):
            if index == 0:
                circles.addByCenterRadius(adsk.core.Point3D.create(0, 0, 0), minionRadius/10)
                index += 1
                continue
            # for each offset-loop
            for degree in range(0, 360, int(360/(baseCircNum*index))):
                circles.addByCenterRadius(adsk.core.Point3D.create(math.cos(degree*math.pi/180)*pos/10,\
                 math.sin(degree*math.pi/180)*pos/10, 0), minionRadius/10)
            index += 1

    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))

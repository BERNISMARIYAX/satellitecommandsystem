class Satellite:
    def __init__(sate):
        # Initializing the satellite's attributes to their default initial state
        sate.orientation = "North"
        sate.solar_panels = "Inactive"
        sate.data_collected = 0

    def rotate(sate, direction):
        # Implementing the 'rotate' command for changing the satellite's orientation
        if direction in ["North", "South", "East", "West"]:
            sate.orientation = direction
        else:
            print("Invalid direction provided. Use 'North', 'South', 'East', or 'West'.")

    def activatePanels(sate):
        # Implementing the 'activatePanels' command to activate the solar panels
        sate.solar_panels = "Active"

    def deactivatePanels(sate):
        # Implementing the 'deactivatePanels' command to deactivate the solar panels
        sate.solar_panels = "Inactive"

    def collectData(sate):
        # Implementing the 'collectData' command to increment data collected by 10 units if solar panels are active
        if sate.solar_panels == "Active":
            sate.data_collected += 10
        else:
            print("Solar panels must be active to collect data.")

# Create a satellite object
satellite = Satellite()

# Examples
satellite.rotate("South")
satellite.activatePanels()
satellite.collectData()

# Display the satellite's state after executing the commands
print("Orientation:", satellite.orientation)
print("Solar Panels:", satellite.solar_panels)
print("Data Collected:", satellite.data_collected)

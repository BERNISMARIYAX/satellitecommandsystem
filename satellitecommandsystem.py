class Satellite:
    def __init__(sate):
        # Initializing attributes
        sate.orientation = "North"
        sate.solar_panels = "Inactive"
        sate.data_collected = 0

    def rotate(sate, direction):
        # Implementing rotate command
        if direction in ["North", "South", "East", "West"]:
            sate.orientation = direction
        else:
            print("Invalid direction provided. Use 'North', 'South', 'East', or 'West'.")

    def activatePanels(sate):
        # Implementing activatepanels command
        sate.solar_panels = "Active"

    def deactivatePanels(sate):
        # Implementing deactivatePanels command
        sate.solar_panels = "Inactive"

    def collectData(sate):
        # Implementing collectData command
        if sate.solar_panels == "Active":
            sate.data_collected += 10
        else:
            print("Solar panels must be active to collect data.")

satellite = Satellite()

# Examples
satellite.rotate("South")
satellite.activatePanels()
satellite.collectData()

# displaying states after executing the commands
print("Orientation:", satellite.orientation)
print("Solar Panels:", satellite.solar_panels)
print("Data Collected:", satellite.data_collected)

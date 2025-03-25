import unreal


# Set up the resolution multiplier for a high-resolution screenshot
resolution_multiplier = 2  # Change this value as needed (e.g., 2 for double resolution)

# Get the current screen resolution
#viewport = unreal.EditorLevelLibrary.get_all_viewports()[0]
current_resolution = viewport.get_size()

# Calculate the new resolution based on the multiplier
res_x = current_resolution * resolution_multiplier
res_y = current_resolution * resolution_multiplier

# Set the ScreenPercentage to the resolution multiplier (higher values = higher resolution)
#unreal.SystemLibrary.execute_console_command(None, f"r.ScreenPercentage {resolution_multiplier * 100}")

# Define the screenshot file path and filename
#screenshot_path = "C:/Games/HighResScreenshot.exr"  # Change to your desired path*

# Set the screenshot format to OpenEXR
unreal.SystemLibrary.execute_console_command(None, "sg.ExrEnable 1")

# Take the high resolution screenshot with explicit resolution arguments
unreal.AutomationLibrary.take_high_res_screenshot(res_x, res_y, filename="C:/Games/HighResScreenshot.exr")

# Optionally, reset ScreenPercentage back to 100 after taking the screenshot
#unreal.SystemLibrary.execute_console_command(None, "r.ScreenPercentage 100")

#print(f"High resolution screenshot saved as OpenEXR at: {screenshot_path}")

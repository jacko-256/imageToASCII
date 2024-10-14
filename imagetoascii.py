import os
import array
from PIL import Image

# Get the directory of the current script
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

# Define the image path and output files
image_path1 = os.path.join(SCRIPT_DIR, 'image.jpg')  # Default image name
html_file_path = os.path.join(SCRIPT_DIR, 'ImageToASCII.html')
txt_file_path = os.path.join(SCRIPT_DIR, 'ImageToASCII.txt')

# Ask for resolution input
user_input = input("Please select resolution. The value you input will be the width of the ASCII image.\nResolution: ")
user_input = int(user_input)
target_width = user_input

print("If your image is not named \"image.jpg\" or not in the same folder as this script, type its alternative file name. Write \"no\" if your image has the default filepath")
user_input = input("")
if user_input != "no":
    image_path1 = os.path.join(SCRIPT_DIR, user_input)

print("Select background color: \nRed, Green, Blue, Cyan, Magenta, Yellow, Black, White, Gray, DarkGray, Orange, Purple, Pink, \nBrown, Lime, Navy, DarkRed, LightGray, Tomato, SkyBlue, Olive, Teal, Coral, Gold")
user_input = input("Type exactly as stated: ")
if user_input == "DarkGray":
    user_input = "#171717"

input("Press enter to print...")
print("Printing...")

def resize_image(input_path, output_path, target_width=None, target_height=None):
    with Image.open(input_path) as img:
        original_width, original_height = img.size
        
        aspect_ratio = original_width / original_height
        
        if target_width and not target_height:
            target_height = int(target_width / aspect_ratio)
        elif target_height and not target_width:
            target_width = int(target_height * aspect_ratio)

        resized_img = img.resize((target_width, target_height), Image.LANCZOS)
        
        resized_img.save(output_path)

# Define the path for the resized image
image_path2 = os.path.join(SCRIPT_DIR, 'resizedImage.jpg')

# Resize the image
resize_image(image_path1, image_path2, target_width)

# Open the resized image
image = Image.open(image_path2)

pixels = image.load()
width, height = image.size

# ASCII characters and brightness values
chars = array.array('u', [' ', '`', '.', '-', '\'', ':', '_', ',', '^', '=', ';', '>', '<', '+', '!', 'r', 'c', '*', '/', 'z', '?', 's', 'L', 'T', 'v', ')', 'J', '7', '(', '|', 'F', 'i', '{', 'C', '}', 'f', 'I', '3', '1', 't', 'l', 'u', '[', 'n', 'e', 'o', 'Z', '5', 'Y', 'x', 'j', 'y', 'a', ']', '2', 'E', 'S', 'w', 'q', 'k', 'P', '6', 'h', '9', 'd', '4', 'V', 'p', 'O', 'G', 'b', 'U', 'A', 'K', 'X', 'H', 'm', '8', 'R', 'D', '#', '$', 'B', 'g', '0', 'M', 'N', 'W', 'Q', '%', '&', '@'])
brightnessVals = array.array('f', [0, 0.0751, 0.0829, 0.0848, 0.1227, 0.1403, 0.1559, 0.185, 0.2183, 0.2417, 0.2571, 0.2852, 0.2902, 0.2919, 0.3099, 0.3192, 0.3232, 0.3294, 0.3384, 0.3609, 0.3619, 0.3667, 0.3737, 0.3747, 0.3838, 0.3921, 0.396, 0.3984, 0.3993, 0.4075, 0.4091, 0.4101, 0.42, 0.423, 0.4247, 0.4274, 0.4293, 0.4328, 0.4382, 0.4385, 0.442, 0.4473, 0.4477, 0.4503, 0.4562, 0.458, 0.461, 0.4638, 0.4667, 0.4686, 0.4693, 0.4703, 0.4833, 0.4881, 0.4944, 0.4953, 0.4992, 0.5509, 0.5567, 0.5569, 0.5591, 0.5602, 0.5602, 0.565, 0.5776, 0.5777, 0.5818, 0.587, 0.5972, 0.5999, 0.6043, 0.6049, 0.6093, 0.6099, 0.6465, 0.6561, 0.6595, 0.6631, 0.6714, 0.6759, 0.6809, 0.6816, 0.6925, 0.7039, 0.7086, 0.7235, 0.7302, 0.7332, 0.7602, 0.7834, 0.8037, 0.9999])
prevYValue = 0

# Prepare HTML content
html_content = """
<!DOCTYPE html>
<html>
<head>
    <title>Image To ASCII Converter</title>
    <style>
    body {
        background-color: """ + user_input + """;
        color: white;
        font-family: "Courier New";
        white-space: pre;
        margin: 0; 
    }
    #ascii-art-container {
        width: 100%;
        height: 100vh;
        overflow: hidden;
        margin: auto; 
        display: flex;
        align-items: center;
        justify-content: center;
    }
    .ascii-art {
        font-size: 2px;
        line-height: .55;
    }
</style>
</head>
<body>
    <div id="ascii-art-container">
        <div class="ascii-art" id="asciiArt">
"""

# Write HTML file
with open(html_file_path, 'w') as file:
    file.write(html_content)

# Create the ASCII text file
with open(txt_file_path, 'w') as file:
    file.write("")

def asciiConverter(width, height, r, g, b):
    global prevYValue
    char = ''
    if prevYValue < height:
        prevYValue = height
        with open(html_file_path, 'a') as file:
            file.write('\n')
        with open(txt_file_path, 'a') as file:
            file.write('\n')
    
    brightness = 1 - (0.299 * r + 0.587 * g + 0.114 * b) / 256
    for i in range(len(brightnessVals)):
        if brightness < brightnessVals[i]:
            char = chars[i]
            break
    color = f'#{r:02X}{g:02X}{b:02X}'
    
    with open(html_file_path, 'a') as file:
        file.write(f'<span style="color: {color};">{char}</span>')
    with open(txt_file_path, 'a') as file:
        file.write(char)

# Generate ASCII art
for y in range(height):
    for x in range(width):
        r, g, b = image.getpixel((x, y))
        asciiConverter(x, y, r, g, b)

# Close HTML content
html_close = """</div>
    </div>

    <script>
        function resizeFont() {
            const container = document.getElementById('ascii-art-container');
            const asciiArt = document.getElementById('asciiArt');
            let fontSize = 1;
            asciiArt.style.fontSize = fontSize + 'px';
            
            while (asciiArt.offsetWidth <= container.offsetWidth && 
                   asciiArt.offsetHeight <= container.offsetHeight) {
                fontSize++;
                asciiArt.style.fontSize = fontSize + 'px';
            }

            asciiArt.style.fontSize = (fontSize - 1) + 'px';
        }

        // Resize font on page load
        window.onload = resizeFont;
        // Optionally, resize on window resize
        window.onresize = resizeFont;
    </script>
</body>
</html>"""

# Write the closing tags to the HTML file
with open(html_file_path, 'a') as file:
    file.write(html_close)

print("Printing completed!")
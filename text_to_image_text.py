from PIL import Image, ImageDraw, ImageFont
import textwrap

def create_image(slogan, features, company_name, background_color=(0, 0, 0, 0), font_color='white', image_size=(360, 600), text_box_size=(360, 200), text_margin_bottom=10):
    image = Image.new('RGBA', image_size, background_color)
    draw = ImageDraw.Draw(image)

    # Set maximum width and height for the text
    max_width = text_box_size[0]
    max_height = text_box_size[1]

    # Use the size of the current company name as a reference for font sizes
    reference_font_size = int(max_height * 0.1)  # 10% of maximum height for reference

    # Load fonts
    font_slogan = ImageFont.truetype("arial.ttf", int(reference_font_size * 0.8))  # 80% smaller than reference
    font_company = ImageFont.truetype("arialbd.ttf", reference_font_size)
    font_features = ImageFont.truetype("arial.ttf", int(reference_font_size * 0.7))  # 70% smaller than reference

    # Wrap text within the maximum width
    wrapped_slogan = textwrap.fill(slogan, width=30)
    wrapped_features = "\n".join(textwrap.wrap(", ".join(features), width=30))

    # Calculate text dimensions
    text_width_slogan, text_height_slogan = draw.textsize(wrapped_slogan, font=font_slogan)
    text_width_company, text_height_company = draw.textsize(company_name, font=font_company)
    text_width_features, text_height_features = draw.textsize(wrapped_features, font=font_features)

    # Calculate positions for center alignment within the text box
    position_features = ((max_width - text_width_features) // 2, image_size[1] - text_height_features - text_margin_bottom)
    position_slogan = ((max_width - text_width_slogan) // 2, position_features[1] - 10 - text_height_slogan)  # Add space
    position_company = ((max_width - text_width_company) // 2, position_slogan[1] - 10 - text_height_company)  # Add space

    # Draw text on image with justification
    draw.text(position_features, wrapped_features, font=font_features, fill=font_color, align="center", spacing=5)
    draw.text(position_slogan, wrapped_slogan, font=font_slogan, fill=font_color, align="center", spacing=5)
    draw.text(position_company, company_name, font=font_company, fill=font_color, align="center", spacing=5)

    image.save('output.png')

# Example usage
product_description = "A powerful laptop with a sleek design and long battery life."
user_provided_tagline = "Unleash your productivity with our cutting-edge technology."
language = 'fr'  # Change language as needed

# Dummy slogan and features (replace with actual OpenAI generated data)
slogan = "Empower your work with cutting-edge tech. Experience the future of productivity."
features = ["Sleek design", "Powerful performance", "Long battery life" ]
company_name = "MyTechCompany"  # Change company name as needed

# Create image with transparent background
create_image(slogan, features, company_name)

print("Image saved to output.png")

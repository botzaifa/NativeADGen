from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/save-data/<path:slug>', methods=['POST'])
def save_data(slug):
    # Extract values from the slug
    values = slug.split('/')
    companyName, productInfo, theme, adType, tagline = values[:5]

    # Perform actions with the extracted data (for example, store it in a dictionary)
    ad_data = {
        'companyName': companyName,
        'productInfo': productInfo,
        'theme': theme,
        'adType': adType,
        'tagline': tagline
    }

    # Print the received data (for demonstration purposes)
    print("Received Data:", ad_data)

    # You can perform further operations with the data here

    return jsonify({'message': 'Data received successfully'})

if __name__ == '__main__':
    app.run(debug=True)

import json

# Create a Python dictionary
data = {
    "name": "John Doe",
    "age": 30,
    "city": "Example City",
    "is_student": False,
    "grades": [90, 85, 92]
}

# Convert the dictionary to a JSON string
json_data = json.dumps(data, indent=2)  # The indent parameter adds indentation for better readability (optional)

# Display the JSON string
print(json_data)

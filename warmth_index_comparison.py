import matplotlib.pyplot as plt

def calculate_warmth(temperature, wind_speed, humidity, material='merino_wool'):
    base_warmth = 0

    if material == 'merino_wool':
        base_warmth = 10
    elif material == 'synthetic':
        base_warmth = 7
    elif material == 'cotton':
        base_warmth = 5

    warmth_index = base_warmth - (0.1 * wind_speed) + (0.05 * humidity) - (0.2 * (20 - temperature))

    return max(warmth_index, 0)

temperature = 5  # degrees Celsius
wind_speed = 10  # km/h
humidity = 80  # percent

materials = ['merino_wool', 'synthetic', 'cotton']
warmth_indices = []

for material in materials:
    warmth_index = calculate_warmth(temperature, wind_speed, humidity, material)
    warmth_indices.append(warmth_index)

plt.figure(figsize=(10, 6))
plt.bar(materials, warmth_indices, color=['green', 'blue', 'orange'])
plt.title('Comparison of Warmth Index by Material')
plt.xlabel('Material')
plt.ylabel('Warmth Index')
plt.ylim(0, max(warmth_indices) + 2)
plt.show()

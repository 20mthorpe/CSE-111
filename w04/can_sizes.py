import math

def main():
    radii = [6.83, 7.78, 8.73, 10.32, 10.79, 13.02, 5.40, 6.83, 15.72, 6.83, 7.62, 8.10]
    heights = [10.16, 11.91, 11.59, 11.91, 17.78, 14.29, 8.89, 7.62, 17.78, 12.38, 11.27, 11.11]

    for i in range(0, len(radii)):
        volume = compute_volume(radii[i], heights[i])
        surface_area = compute_surface_area(radii[i], heights[i])
        storage_efficiency = compute_storage_efficiency(volume, surface_area)

        print(f"\n Storage efficiency: {storage_efficiency:.2f}")

def compute_volume(radius, height):
    return math.pi * radius**2 * height

def compute_surface_area(radius, height):
    return 2 * math.pi * radius * (radius + height)

def compute_storage_efficiency(volume, surface_area):
    return volume / surface_area
    
main()
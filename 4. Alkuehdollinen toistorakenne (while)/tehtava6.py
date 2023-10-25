import random

def calculate_pi(num_points):
    points_inside_circle = 0

    for _ in range(num_points):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)

        if x**2 + y**2 < 1:
            points_inside_circle += 1

    estimated_pi = 4 * points_inside_circle / num_points
    return estimated_pi

def main():
    try:
        num_points = int(input("Syötä arvottavien pisteiden määrä: "))
    except ValueError:
        print("Virheellinen syöte. Syötä positiivinen kokonaisluku.")
        return

    if num_points <= 0:
        print("Arvottavien pisteiden määrän on oltava positiivinen kokonaisluku.")
        return

    estimated_pi = calculate_pi(num_points)

    print(f"Piin likiarvo arvotuilla {num_points} pisteellä on noin {estimated_pi:.6f}.")

if __name__ == "__main__":
    main()

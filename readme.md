# Program to Renderer Doughnut in Terminal

This is a Python program that renders a doughnut in a 3D space on the terminal using ASCII art. The program calculates the 3D coordinates of the doughnut using trigonometry and renders it using the terminal cursor and color control characters.

## Usage

To run the program, simply execute the `terminal_doughnut_renderer.py` file in your terminal. The doughnut will be rendered continuously until you stop the program using Ctrl + C. 

```bash
python terminal_doughnut_renderer.py

```

## Usage

Customization
You can customize the shape and animation of the doughnut by modifying the parameters in the code:

```python
# Define the parameters of the doughnut
R = 15
r = 7

# Render the doughnut
while True:
    render_doughnut(R, r, 5, 15)
```

The `R` and `r` parameters control the size of the doughnut, while the third and fourth arguments of the `render_doughnut()`  function control the increments for the theta and phi angles, respectively.



## Dependencies

This program has no external dependencies and can be run using only the Python Standard Library.

## License

[MIT](https://opensource.org/license/mit/)
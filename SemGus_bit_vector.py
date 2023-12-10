import random

def generate_dynamic_program():
    # Templates for various ways to flip bits in a bit vector
    templates = [
        "lambda x: [~bit & 1 for bit in x]",            # Corrected to flip bits
        "lambda x: [1 - bit for bit in x]",             # Correctly flips bits
        "lambda x: [bit ^ 1 for bit in x]",             # Using XOR to flip bits
        "lambda x: [0 if bit else 1 for bit in x]",     # Conditional flipping
        "lambda x: [int(not bit) for bit in x]",        # list comprehension with not operator
        "lambda x: [(-bit - 1) & 1 for bit in x]",      # bitwise NOT and limiting to 1 bit
        "lambda x: list(map(lambda bit: 1 if bit == 0 else 0, x))",  # map function with a lambda expression
        "lambda x: [(bit | 1) & ~(bit & 1) for bit in x]"            # bitwise OR and AND
    ]

    selected_template = random.choice(templates)

    # Generate the program string
    program_str = selected_template

    # Convert the string to a lambda function
    program = eval(program_str)
    return program, program_str

# Generate a dynamic program
# dynamic_program, program_code = generate_dynamic_program()
# print("Generated Program Code:", program_code)

def parse_specification(spec):
    # Split the specification into function part and mapping part
    func_part, map_part = spec.split(' -> ')

    # Extract the function name
    func_name = func_part.split('(')[0].strip()

    # Initialize default condition values
    condition_var = 'x'  # Default condition variable
    condition_value = None

    # Find the condition part using a more sophisticated method
    try:
        # Extract everything after the comma and before the arrow
        condition_str = func_part.split(',', 1)[1].split('->')[0].strip()
        if '==' in condition_str:
            condition_var, condition_value_str = condition_str.split('==')
            condition_var = condition_var.strip()
            condition_value_str = condition_value_str.strip()
            # Evaluate the condition value safely
            condition_value = eval(condition_value_str)
        else:
            print("Equality operator '==' not found in condition.")
    except Exception as e:
        print(f"Error parsing condition: {e}")

    # Parse the mapping part
    try:
        output_value = eval(map_part.strip())
    except Exception as e:
        print(f"Error evaluating output value: {e}")

    # Construct and return the parsed specification
    parsed_spec = {
        'function': func_name,
        'condition': {condition_var: condition_value},
        'output': output_value
    }
    return parsed_spec


def evaluate_program(program, spec, test_cases):
    # Initial score
    score = 0

    # Extract condition and expected output from specification
    condition_value = spec['condition']['x']
    expected_output = spec['output']

    # Iterate over test cases
    for input_vector, _ in test_cases:
        # Check if input_vector meets the specification condition
        if input_vector == condition_value:
            output = program(input_vector)
            # Increase score if output matches the expected output
            if output == expected_output:
                score += 1

    return score


def synthesize_program(specification, test_cases):
    spec = parse_specification(specification)
    best_program = None
    best_score = float('-inf')
    best_program_code = None  # To store the code of the best program

    generated_program_codes = set()  # Set to store generated program codes

    # Define a simple convergence condition (e.g., a fixed number of iterations)
    for _ in range(100):  # Example: 100 iterations
        program_tuple = generate_dynamic_program()  # Receive a tuple
        program = program_tuple[0]  # Extract the lambda function
        program_code = program_tuple[1]  # Extract the program code

        # Check if the program code is already generated
        if program_code not in generated_program_codes:
            generated_program_codes.add(program_code)  # Add new program code to the set
            score = evaluate_program(program, spec, test_cases)
            if score > best_score:
                best_program = program
                best_score = score
                best_program_code = program_code  # Store the best program code

    return best_program, best_program_code  # Return both the function and its code


# Example usage
specification = "flipBit(x), x == [0,1,0] -> [1,0,1]"
test_cases = [
    ([0, 1, 0], [1, 0, 1]),
    ([0, 1, 0, 1, 0], [1, 0, 1, 0, 1]),
    ([1, 0, 1, 0, 1], [0, 1, 0, 1, 0]),
    ([0, 0, 0, 0], [1, 1, 1, 1]),
    ([1, 1, 1, 1], [0, 0, 0, 0]),
    ([0], [1]),
    ([1], [0]),
    ([0] * 20, [1] * 20),
    ([1] * 20, [0] * 20),
    ([1, 0, 0, 1, 1, 0], [0, 1, 1, 0, 0, 1]),
    ([0, 1, 1, 0, 0, 1], [1, 0, 0, 1, 1, 0]),
    ([], [])
    # ... any additional test cases you wish to add
]

# Testing the function with the specification
specification = "flipBit(x), x == [0,1,0] -> [1,0,1]"
parsed_spec = parse_specification(specification)
print(parsed_spec)


result_program, result_program_code = synthesize_program(specification, test_cases)
print("Result Program Code:", result_program_code)
print("Result from Program:", result_program([0, 1, 1, 0]))









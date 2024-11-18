import random

def generate_bbs_bits(bit_length, p, q, seed):
    # Compute N = p * q
    N = p * q
    bits = []

    # Initialize the seed
    x = seed

    # Generate pseudorandom bits
    for _ in range(bit_length):
        # Compute X_{i+1} = (X_i * X_i) % N
        x = (x * x) % N
        # Extract the least significant bit as the pseudorandom bit
        bit = x & 1
        bits.append(bit)

    return bits

# Example usage
p = 107
q = 139
seed = 42
bit_length = 10  # Number of pseudorandom bits to generate

random_bits = generate_bbs_bits(bit_length, p, q, seed)
print("Generated pseudorandom bits:", random_bits)


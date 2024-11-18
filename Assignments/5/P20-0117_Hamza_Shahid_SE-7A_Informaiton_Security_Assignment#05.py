import hashlib

# Define the compression function (SHA-256 in this example)
def sha256_compress(block, state):
	sha256 = hashlib.sha256()
	sha256.update(block + state)
	return sha256.digest()
	
# Implement the Merkle-Damgård construction
def merkle_damgard(message, initial_state, block_size):
	state = initial_state
	# Pad the message to a multiple of the block size
	message += b'\x80' # Append 1 bit
	while len(message) % block_size != (block_size - 8):
		message += b'\x00' # Append 0 bits
		# Append the message length as a 64-bit big-endian integer
		message += (8 * len(message)).to_bytes(8, byteorder='big')
	# Process the message in blocks
	for i in range(0, len(message), block_size):
		block = message[i:i + block_size]
		state = sha256_compress(block, state)
		return state
# Example usage
if __name__ == "__main__":
	message = b"Hello, Merkle-Damgard!"
	initial_state = hashlib.sha256(b"Initial state").digest()
	block_size = 64 # SHA-256 block size in bytes
	result = merkle_damgard(message, initial_state, block_size)
	print("Hash result:", result.hex())

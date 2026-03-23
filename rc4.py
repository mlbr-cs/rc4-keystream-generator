def rc4(key, n_bytes):
    # Key Scheduling Algorithm (KSA)
    S = list(range(256))
    j = 0
    key = [ord(c) for c in key]

    for i in range(256):
        j = (j + S[i] + key[i % len(key)]) % 256
        S[i], S[j] = S[j], S[i]

    # Pseudo-Random Generation Algorithm (PRGA)
    i = 0
    j = 0
    keystream = []

    for _ in range(n_bytes):
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]

        K = S[(S[i] + S[j]) % 256]
        keystream.append(K)

    return keystream
def bytes_to_bits(byte_list):
    bits = ""
    for b in byte_list:
        bits += format(b, '08b')
    return bits

key = "crypto"# Define the key for RC4
stream = rc4(key, 10000)  # generate many bytes

# Save to file
with open("rc4_output.txt", "w") as f:
    f.write(str(stream))

print("Byte sequence saved to rc4_output.txt")

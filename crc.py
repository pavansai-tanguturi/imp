P = 0xD8
T = 0x80

def c(d):
    r = 0
    for byte in d:
        r ^= byte
        for b in range(8):
            if r & T:
                r = (r << 1) ^ P
            else:
                r = r << 1
    return r & 0xFF

def main():
    m = "Hello, CRC!"
    x = c([ord(c) for c in m])
    print(f"Message: {m}")
    print(f"CRC: 0x{x:02X}")

if __name__ == "__main__":
    main()
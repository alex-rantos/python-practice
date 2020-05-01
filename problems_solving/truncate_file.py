"""
You have a huge file named "data.bin" that does not fit in memory, 
code a program that deletes every 7th byte of it. truncate can be used to change its size.
"""
BUF_SIZE = 2**16
FILE_PATH = "./data.bin"
TO_WRITE_PATH = "./data_truncated.bin"
if __name__ == "__main__":
    with open(FILE_PATH, "rb") as f:
        with open(TO_WRITE_PATH, "w") as fw:
            # use buffer for faster digest calculation
            while buffer := f.read(BUF_SIZE):
                for x in range(7,len(buffer),7):
                    del buffer[x]
                fw.write(buffer)
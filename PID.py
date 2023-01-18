import os

def main():
    print("PID of current process is",os.getpid())
    print("Pid od parent process",os.getppid())

if __name__ == "__main__":
    main()
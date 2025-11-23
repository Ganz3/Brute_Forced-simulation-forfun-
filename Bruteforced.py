from email.mime import base
import itertools  # Untuk menghasilkan kombinasi karakter
import string  # Untuk mendapatkan kumpulan karakter
import random  # Untuk operasi acak
import time  # Untuk mengukur waktu eksekusi
import sys
from tkinter import ALL  # Untuk output ke console

# Misal password yang ingin dicari
target = "ganz"

# Configurasi/Menentukan karakter bruteforced
karakter = (
    string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
)
max_length = 4  # Panjang maksimal password

# Menghitung Total kombinasi password
total_combination = sum(len(karakter) ** i for i in range(1, max_length + 1))

start = time.time()
total = 0

# MATRIX COLOR
GREEN = "\033[92m"
CYAN = "\033[96m"
RED = "\033[91m"
MAGENTA = "\033[95m"
BRIGHT = "\033[1m"
RESET = "\033[0m"
YELLOW = "\033[93m"

# MEMBUAT ANIMASI SPINNER DENGAN DELAY
spinner_frames = ["◐", "◓", "◑", "◒"]
spin_index = 0
spin_delay = 0.08
last_spin = time.time()


def cyber_spinner():
    global spin_index, last_spin
    now = time.time()

    if now - last_spin >= spin_delay:
        spin_index = (spin_index + 1) % len(spinner_frames)
        last_spin = now

    return spinner_frames[spin_index]


# KARAKTER MATRIX
matrix_chars = (
    string.ascii_letters
    + string.digits
    + string.punctuation
    + "░▒▓█"
    + "!@#$%^&*()-_=+"
)


def random_matrix_line():
    return "".join(random.choice(matrix_chars) for _ in range(80))


def glitch():
    return (
        f"{CYAN}{BRIGHT}"
        + "".join(random.choice(matrix_chars) for _ in range(10))
        + RESET
    )


# MEMBUAT STYLE/UI LOADING ALA HACKER
glitch_frames = [
    "▓▓▓▒▒▒░░░░░░░░░░░░░░░░░░",
    "▓▓▒▒▒▒▒░░░░░░░░░░░░░░░░░",
    "▓▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░",
    "▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░",
    "▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░░",
    "▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░",
    "░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░",
    "░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░",
    "░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░",
    "░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒",
]
glitch_index = 0
last_glitch_time = time.time()


def glitch_load():
    global glitch_index, last_glitch_time
    speed = 0.05  # kecepatan glitch berubah

    if time.time() - last_glitch_time >= speed:
        glitch_index = (glitch_index + 1) % len(glitch_frames)
        last_glitch_time = time.time()

    # frame glitch
    base = glitch_frames[glitch_index]

    # tambahkan karakter acak di beberapa posisi
    glitched = ""
    for g in base:
        if random.random() < 0.08:  # 10% chance untuk mengganti karakter
            glitched += random.choice(ALL)
        else:
            glitched += g

    return glitched


# GASSKEUUUNN
for length in range(1, max_length + 1):
    for combo in itertools.product(karakter, repeat=length):
        total += 1
        guess = "".join(combo)

        # AGAR TIDAK LAMA DURASINYA
        if total % 100 == 0:
            bar = glitch_load()
            percent = (total / total_combination) * 1000
            matrix_line = random_matrix_line()

            # OUTPUT KE CONSOLE ALA HACKER
            sys.stdout.write(
                f"\n{GREEN}{cyber_spinner()} HACK IN PROGRESS... {RESET}"
                f"{RED}{bar}{percent:5.1f}%{RESET} "
                f"| {CYAN}{guess}{RESET} | "
                f"{RED}{glitch()}{RESET}\n"
                f" {MAGENTA}{BRIGHT} >TRIED COMBINATION ~> {total}/{total_combination}"
                f" {YELLOW}{BRIGHT}| ELAPSED TIME ~> {time.time() - start:.2f} SECONDS<{RESET}"
            )
            sys.stdout.flush()

        # JIKA COCOK/PASSWORD DITEMUKAN
        if guess == target:
            elapsed = time.time() - start
            print(f"\n\n{CYAN}{BRIGHT}==>| ACCESS GRANTED |<=={RESET}")
            print(f"PASSWORD DITEMUKAN: {CYAN}{guess}{RESET}")
            print(f"TOTAL PERCOBAAN: {total} KOMBINASI")
            print(f"WAKTU EKSEKUSI: {elapsed:.4f} DETIK")
            exit()

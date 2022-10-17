import string
import time
import ray


# Example Data
alphabet = list(string.ascii_uppercase)

# ===== Raw Python Version =====


def get_letter_by_id(idx):
    time.sleep(idx / 26)  # Simulates Computations
    letter = alphabet[idx]
    return idx, letter


start_time = time.time()
letters_by_id = [get_letter_by_id(i) for i in range(len(alphabet))]
print(f"Runtime without Ray: {time.time() - start_time} s.")
print(*letters_by_id, sep="\n")


# ===== Ray Version =====

ray.init()

alphabet_object_ref = ray.put(alphabet)  # To make data available for all workers in cluster


@ray.remote
def get_letter_by_id_as_task(idx):
    time.sleep(idx / 26)  # Simulates Computations
    letter = ray.get(alphabet_object_ref)[idx]
    return idx, letter


start_time = time.time()
data = [get_letter_by_id_as_task.remote(i) for i in range(len(alphabet))]
letters_by_id = ray.get(data)
print(f"Runtime with Ray: {time.time() - start_time} s.")
print(*letters_by_id, sep="\n")

import subprocess
subprocess.check_call(["pip", "install", "numpy"])
import numpy as np

msg = "Roll a dice"
print(msg)

print(np.random.randint(1,9))
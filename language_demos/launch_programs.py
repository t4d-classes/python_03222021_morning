import subprocess

# result = subprocess.run("where chkdsk12.exe")

# print(result.returncode)

p = subprocess.Popen(
    "where chkdsk12.exe",
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE)

for line in p.stdout.readlines():
    print(str(line, 'UTF-8'))

for line in p.stderr.readlines():
    print(str(line, 'UTF-8'))

retval = p.wait()
print(retval)

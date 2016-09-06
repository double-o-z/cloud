def copy_file(source, dest):
    with open(source) as f:
        with open(dest, "w") as f1:
            for line in f:
                f1.write(line)

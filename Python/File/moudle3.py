def backups():
    while True:
        old_name = input("Tell me the name of the file you want to backup: ")
        index = old_name.rfind('.')
        if index != -1 and index != len(old_name) - 1:
            break
        else:
            print("File format error!")
    prefix = old_name[:index]
    suffix = old_name[index:]
    new_name = prefix + '_copy' + suffix
    old_file = open(old_name, 'rb')
    new_file = open(new_name, 'wb')
    while True:
        data = old_file.read(1024)
        if not data:
            break
        else:
            new_file.write(data)
    old_file.close()
    new_file.close()
    print("Backup complete!")

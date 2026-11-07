with open("workflow.yml", encoding="utf-8") as f:
    for line in f.readlines():
        if "aws-access-key-id" in line.lower():
            print("STORED KEYS found")
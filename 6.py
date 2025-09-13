def longest_common_prefix(strs):
    if not strs:
        return ""

    prefix = strs[0]

    for s in strs:
        print(s)
        while not s.startswith(prefix):
            prefix = prefix[:-1]
            print("pre",prefix)
            if not prefix:
                return ""
    return prefix

# Example usage
words = ["flower", "flow", "flight"]
print("Longest Common Prefix:", longest_common_prefix(words))
        

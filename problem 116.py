def get_replacements(tile_length, row_length):
    if (tile_length, row_length) in replacements_dict:
        return replacements_dict[(tile_length, row_length)]
    
    ans = row_length - tile_length + 1

    for i in range(tile_length, row_length - tile_length + 1):
        ans += get_replacements(tile_length, row_length - i)

    replacements_dict[(tile_length, row_length)] = ans

    return ans


replacements_dict = {}

print(sum(get_replacements(tile_length, 50) for tile_length in range(2, 5)))

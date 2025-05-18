from knot_fence_ac import adjs

if __name__ == "__main__":
    for adj in adjs:
        output = ''
        output += '"/execute at @s if block '
        output += adj
        output += ' grindstone run tp @s '
        output += adj
        output += ' 0 0"'
        print(output)
    print()
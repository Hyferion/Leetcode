def threeSum(nums):
    matches = []
    if len(nums) < 3:
        return []
    else:
        for x in nums:
            for y in nums:
                for z in nums:
                    if x + y + z == 0:
                        if [x,y,z] in matches:
                            pass
                        else:
                            matches.append([x,y,z])
    print(matches)


threeSum([-1, 0, 1, 2, -1, -4])

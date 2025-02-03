# Volume of a Cuboid
def get_volume_of_cuboid(length, width, height):
    return length * width * height
# Grasshopper - Array Mean
def find_average(nums):
    if len(nums) == 0:
        return 0
    return sum(nums) / len(nums)
# No Zeros for Heroes
def no_boring_zeros(n):
    if n==0:
        return n
    while n%10==0:
        n=n/10
    return n
# Student's Final Grade
def final_grade(exam, projects):
  if exam > 90 or  projects > 10: return 100
  if exam > 75 and projects >= 5: return 90
  if exam > 50 and projects >= 2: return 75
  return 0
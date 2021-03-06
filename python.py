def calculate(min,max):
    n = max
    while min<n:
        max = max + min
        min+=1;
    print(max)
calculate(1,3)
calculate(4,8)
def avg(data):
    x = data['count']
    y = data['employees']
    z = 0
    arr = []
    for z in range(x):
        arr.append(y[z]['salary'])
        z+=1
        total = sum(arr)
        result = total/x
    print(result)
avg({
        "count":3,
        "employees":[
            {
                "name":"John",
                "salary":30000
            },
            {
                "name":"Bob",
                "salary":60000
            },
            {
                "name":"Jenny",
                "salary":50000
            }
        ]
})
def maxProduct(nums):
        result = []
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                maxproduct = nums[i]*nums[j]
                result.append(maxproduct)
                answer = max(result)
        print(answer)
maxProduct([5, 20, 2, 6])
maxProduct([10, -20, 0, 3])
def twoSum(nums, target):
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if(nums[i] + nums[j] == target):
                    return [i, j]
result=twoSum([2, 11, 7, 15], 9)
print(result)
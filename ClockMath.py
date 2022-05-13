def clockangles(hour, minute):
    ans = abs((hour * 30 + minute * 0.5) - (minute * 6))
    return min(360-ans,ans)

a,b = map(int, input().split())

print(clockangles(a,b))
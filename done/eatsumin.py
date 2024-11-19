import heapq

def find_min_stops(N, stores, L, P):
    stops = 0
    current_pos = 0
    fuel = P
    max_satisfaction = []

    stores.append((L, 0))  # 식당은 마지막 가게나 다름이 없는거다
    heapq.heapify(max_satisfaction) # 힙 생성

    for distance, satisfaction in stores:
        dist_to_store = distance - current_pos

        while fuel - dist_to_store < 0:  # 어어 이거 들러야돼요 선생님
            if not max_satisfaction:  # 으앙 쥬금
                return -1

            max_fuel = -heapq.heappop(max_satisfaction)
            fuel += max_fuel
            stops += 1

        fuel -= dist_to_store
        current_pos = distance
        heapq.heappush(max_satisfaction, -satisfaction)  # Use negative value for max heap

    if fuel >= L:
        return stops

    return -1

#INPUT
N = int(input())
stores = [list(map(int, input().split())) for _ in range(N)]
# print(stores)
L, P = map(int, input().split())

#해치우자
result = find_min_stops(N, stores, L, P)
print(result)
def solution(emergency):
    # 인덱스로 정렬
    index_sort = sorted(range(len(emergency)),key=lambda i: -emergency[i])
    # range(len(emergency))는 [0,1,2] 임 0부터 그냥 1,2,3 .. 순으로 초깃값 세팅
    # 위의 결과는 배열
    # 위로인해서 만들어지는 배열의 인덱스는 위급도 순서이고, 안의 값은 원본배열의 인덱스로
    # 따라간 값 즉 76이  인덱스 첫번째 이고 새로만들어진 배열에서 맨앞에 옴
    # ===> 숫자높은대로 인덱스값 정렬
    
    ranks = [0]*len(emergency)
    # 초깃값 0의 emergency길이만큼의 배열 생성
    
    for index , value in enumerate(index_sort,start=1): #[1 2 0]
        ranks[value] = index
    # 인덱스 숫자는 순위매기기용
    # 1등은 기존배열의 1번째 인덱스에 있던값 76, 2등은 2번째 인덱스에 있던 24, 3등은 0번째 인덱스에 있던 3
    return ranks
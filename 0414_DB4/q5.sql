-- WITH RECURSIVE 를 이용하여 계층형 질의를 작성해보세요.
with RECURSIVE cte(mentee_id, mento_id, lvl)
as(
    select mentee_id, mento_id, 0 as lvl
    from MEMBER
    union all
    select a.mentee_id, a.mento_id, b.lvl+1
    from MEMBER as a
    join cte as b
    on b.mentee_id=a.mento_id

)
select mentee_id, mento_id, lvl
from cte
ORDER by lvl, mentee_id;



'''
## 5. 멘토와 멘티, 정리해보자

엘리스 스쿨의 학생들은 멘토와 멘티 프로그램에 참여하고 있습니다.
멘토이면서 멘티인 학생도 있고, 멘토만 또는 멘티만 하는 학생도 있습니다.
(그림으로 그려보면 계층형이 될 것 같아요!)

어느 날, 엘리스 스쿨의 담당 선생님은 멘토와 멘티 정보가 담겨있는 `MEMBER` 테이블을 통해 누가 첫 번째 멘토인지, 누가 몇 번째 멘토인지, **계층적으로** 확인해보려고 합니다.

`MEMBER` 테이블의 정보는 다음과 같습니다.

![image](https://cdn-api.elice.io/api-attachment/attachment/c9dee2267caa4792a8ad34c047f5eb4d/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA%202021-04-14%20%E1%84%8B%E1%85%A9%E1%84%8C%E1%85%A5%E1%86%AB%201.52.18.png)

## 지시사항

`MEMBER` 테이블에 대해서 `WITH RECURSIVE` 절을 이용하여 데이터를 계층형으로 출력하는 쿼리를 작성해봅시다.

- 이때 출력하고자 하는 컬럼은, **mentee_id, mento_id, lvl** 이고, **가장 최상단에 있는 멘토는 lvl = 0 이고, 한 계층마다 1씩 증가하는 것** 으로 설정합시다.

### Tips!

> - 결과에 대해 `ORDER BY` 를 이용하여 lvl 오름차순, mentee_id 오름차순으로 정렬해주세요.
> - 데이터 조회순서는 지시사항에서 언급하고 있는 순서대로 정확히 작성하세요.'''
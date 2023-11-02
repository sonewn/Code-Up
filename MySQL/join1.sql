-- 주문량이 많은 아이스크림 조회하기
-- 7월 아이스크림 총 주문량과 상반기의 아이스크림 총 주문량을 더한 값이 큰 순서대로 
-- 상위 3개의 맛을 조회하는 SQL 문을 작성해주세요.

-- TRY 1
WITH JOI AS (
    SELECT
        a.FLAVOR,
        SUM(b.TOTAL_ORDER) JU_OD, -- b.JU_OD ,
        SUM(a.TOTAL_ORDER) FH_OD 
    FROM
        FIRST_HALF a
    LEFT JOIN
        JULY b
        # (
        #     SELECT FLAVOR, SUM(TOTAL_ORDER) JU_OD
        #     FROM JULY
        #     GROUP BY 1
        # ) b
    ON
        a.FLAVOR=b.FLAVOR
    GROUP BY
    1
)
, RNK AS (
    SELECT
        FLAVOR,
        ROW_NUMBER() OVER(ORDER BY FH_OD+JU_OD DESC) RNK_N
    FROM
        JOI
)
SELECT FLAVOR FROM RNK WHERE RNK_N < 4;



-- TRY 2
SELECT 
    a.flavor as flavor
FROM 
    first_half as a
INNER JOIN 
    july as b
ON a.flavor = b.flavor
GROUP BY flavor
ORDER BY sum(a.total_order) + sum(b.total_order) DESC
LIMIT 3
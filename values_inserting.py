import pymysql
from db_password import password


conn = password()
cur = conn.cursor()

def insert_values():
    cur.execute("""insert into category VALUES
    (1, '콜드브루'),
    (2, '에스프레스'),
    (3, '프라푸치노')""")
    conn.commit()
    cur.execute("""insert into drinks VALUES
    (1,'콜드브루 커피', 1, 0, 1),
    (2,'아이스카페아메리카노', 2, 0, 1),
    (3, '모카 프라푸치노', 3, 0, 1),
    (4, '콜드브루 몰트', 1, 0, 1),
    (5, '제주크림프라푸치노', 3, 0, 0);""")
    conn.commit()
    cur.execute("""insert into drink_allergies VALUES
    (1, 1, '-'),
    (2, 2, '-'),
    (3, 3, '우유'),
    (4, 1, '대두/우유'),
    (5, 3, '땅콩/대두/우유');""")
    conn.commit()
    cur.execute("""insert into nutrition VALUES
    (1, 1, 5, 11, 0, 0, 0, 155),
    (2, 2, 10, 5, 0, 0, 1, 150),
    (3, 3, 280, 180, 6, 36, 5, 0),
    (4, 1, 505, 150, 20, 41, 7, 190),
    (5, 3, 600, 330, 7, 79, 9, 0);""")
    conn.commit()
    cur.execute("""insert into size VALUES
    (1, 1, 12, 3500),
    (2, 2, 12, 3000),
    (3, 3, 12, 4000),
    (4, 1, 12, 5000),
    (5, 3, 16, 6000);""")
    conn.commit()
    cur.execute("""insert into img VALUES
    (1, 1, 1, 'https://image.istarbucks.co.kr/upload/store/skuimg/2021/04/[9200000000038]_20210430113202595.jpg'),
    (2, 2, 2, 'https://image.istarbucks.co.kr/upload/store/skuimg/2021/04/[110563]_20210426095937947.jpg'),
    (3, 3, 3, 'https://image.istarbucks.co.kr/upload/store/skuimg/2021/04/[168004]_20210415134634879.jpg'),
    (4, 4, 1, 'https://image.istarbucks.co.kr/upload/store/skuimg/2021/02/[9200000001636]_20210225093600541.jpg'),
    (5, 5, 3, 'https://image.istarbucks.co.kr/upload/store/skuimg/2021/04/[9200000002502]_20210426100408048.jpg');""")
    conn.commit()
    cur.execute("""insert into drink_des VALUES
    (1, 1, '콜드 브루 전용 원두를 차가운 물로 14시간동안 추출'),
    (2, 2, '진한 에스프레소에 시원한 정수물과 얼음을 더함'),
    (3, 3, '초콜릿과 커피가 어우러진 프라푸치노'),
    (4, 1, '바닐라 아이스크림, 몰트가 블렌딩'),
    (5, 3, '제주 쑥쑥 라떼의 시원한 버전');""")
    conn.commit()